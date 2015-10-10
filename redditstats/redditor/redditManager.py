import praw
import time
import json
import datetime
from datetime import date

class RedditManager():
    
    
    def __init__(self):
        self.r = praw.Reddit("/u/habnpam testing stuff")

    
    def fetch_user(self, username):
        dd= 33
        
    
    def user_exists(self, username):
        
        try:
            birthday_utc = self.r.get_redditor(username).created_utc
        except:
           
            return False
        
       
        return True
        
    
    def gather_info(self, username):
 
        self.redditor = self.r.get_redditor(username)
        reddit_dict = {}
        
        reddit_dict['date_joined'] = self.get_date_joined()  
        
        
        reddit_dict['quotes'] = self.get_quotes()
        reddit_dict['quotes_length'] = len(reddit_dict['quotes'])
        
        
        
        
        
        return reddit_dict
    
    def get_date_joined(self):
        
        birthday_utc = self.redditor.created_utc
        
        return time.strftime('%B %d, %Y', time.gmtime(birthday_utc))
        
    
    
    def stringify(self, phrase):
        
        new_phrase = "\"" + str(phrase.encode('ascii', 'ignore')) + "...\""

        return new_phrase
        
        
        
        
    def get_quotes(self):
        
        q = self.redditor.get_comments(sort='top', time='all', limit=10)
        
        quotes = []        
        for a in q:
            quotes.append(self.stringify(a.body[:140]))
        
        quotes_json = json.dumps(quotes);
        return quotes_json
        
        
    def gather_data(self):
            
        comments = self.redditor.get_comments(time='all', limit=1000)
        self.karma_total = 0
        
        self.subreddit_dict = {}
        self.karma_dict = {}
        try:
            for c in comments:
                str_sub = str(c.subreddit) 
                
                #Counts subreddit posts. For subreddit pie chart.
                if not str_sub in self.subreddit_dict:
                    self.subreddit_dict[str_sub] = 1
                    
                else:
                    self.subreddit_dict[str_sub] = self.subreddit_dict[str_sub]  + 1
                    
                
                #Counts karma by subreddit. For karma pie chart.
                if not str_sub in self.karma_dict:
                    self.karma_dict[str_sub] = int(c.ups)
                else:
                    self.karma_dict[str_sub] = self.karma_dict[str_sub] + int(c.ups)
                
                self.karma_total = self.karma_total + int(c.ups)
                
                
                #For karma progression line chart.
                
                
                #Above, I count the comment karma. So this function does 2 things.
                #I don't want make API calls twice to get the same thing. 
                
                

        except:
            print("nogo")
            pass
        
        
        
        
    def subreddit_pie_chart(self):
        return self.subreddit_dict.items()
        
    
    def karma_counter_pie_chart(self):
        
        for key in self.karma_dict:
            if self.karma_dict[key] < 0:
                self.karma_dict[key] = 1
        return self.karma_dict.items()
        
        
        
        
        #The age of the redditor is broken down into 10 parts.
        #the 10 will be utc times. They will then get changed into their
        #word form (May, June, etc). They will be the x-coordinates.
    def karma_progression_line_chart(self):
        
        start = self.redditor.created_utc
        
        end = time.time()
        
        interval = (end - start) / 20
        
        
        progression_array = []
        
        
        #progression_array is a list of pairs[[x,y],[x,y][x,y]]
        #'x' is the date, and 'y' is the total karma at that date.
        progression_array.append([self.utc_to_string(start), 0, 0])
        for x in range(0, 21):
            
            progression_array.append([self.utc_to_string(start + (interval * x)), 0, 0])
            
        
        
        comments = self.redditor.get_comments(time='all', limit=1000, sort='top')
        
        
        for c in comments:
            
            utc = c.created_utc
            
            for x in progression_array:
                if utc < self.string_to_utc(x[0]):
                    x[1] = x[1] + c.ups
           
        
        
        submissions = self.redditor.get_submitted(time='all', limit=1000, sort='top')
        
        for s in submissions:
            
            utc = s.created_utc
            
            for x in progression_array:
                if utc < self.string_to_utc(x[0]):
                    x[2] = x[2] + s.ups

        return progression_array
        
    
  
    def calendar_chart(self):
        calendar_array = []
        
        
        comments = self.redditor.get_comments(time='all', limit=1000, sort='top')
        
        counter = 0
        for c in comments:
            counter = counter + 1
            c_uct = c.created_utc
            
            date = self.utc_to_struct(c_uct)
            
            #Data has to be in format: year, month, day , karma_count
            date_array = [date.tm_year, date.tm_mon - 1, date.tm_mday, c.ups]
            
            calendar_array.append(date_array)
            
        print(calendar_array)
        return calendar_array
    
    
    
    
    def utc_to_struct(self, utc):
        return date.timetuple(date.fromtimestamp(utc))
        
        
    def utc_to_string(self, utc):
        return time.strftime("%b  %d, %Y", date.timetuple(date.fromtimestamp(utc)))
        
    
    def string_to_utc(self, string):
        return time.mktime(datetime.datetime.strptime(string, "%b  %d, %Y").timetuple())
        
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        