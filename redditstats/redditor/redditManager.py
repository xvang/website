import praw
import time
import json

class RedditManager():
    
    
    def __init__(self):
        self.r = praw.Reddit("/u/habnpam testing stuff")

    
    def fetch_user(self, username):
        dd= 33
        
    
    def user_exists(self, username):
        
        try:
            birthday_utc = self.r.get_redditor(username).created_utc
        except:
            print("False")
            return False
        
        print("True")
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
        
        
    def subreddit_counter_pie_chart(self):
            
        comments = self.redditor.get_comments(time='all', limit=1000)
        self.karma_total = 0
        
        subreddit_dict = {}
        self.karma_dict = {}
        try:
            for c in comments:
                str_sub = str(c.subreddit) 
                
                #Counts subreddit posts.
                if not str_sub in subreddit_dict:
                    subreddit_dict[str_sub] = 1
                    
                else:
                    subreddit_dict[str_sub] = subreddit_dict[str_sub]  + 1
                    
                
                #Counts karma by subreddit
                if not str_sub in self.karma_dict:
                    self.karma_dict[str_sub] = int(c.ups)
                else:
                    self.karma_dict[str_sub] = self.karma_dict[str_sub] + int(c.ups)
                
                self.karma_total = self.karma_total + int(c.ups)
                
                
                
                #Above, I count the comment karma. So this function does 2 things.
                #I don't want make API calls twice to get the same thing. 
                
                

        except:
            print("nogo")
            pass
        
        return subreddit_dict.items()
        
        
    
    def karma_counter_pie_chart(self):
        
        print(self.karma_dict.keys())
        
        
        for key in self.karma_dict:
            if self.karma_dict[key] < 0:
                self.karma_dict[key] = 1
        return self.karma_dict.items()
        
        
        
        
        
    def karma_progression_line_chart(self):
        
        start = self.redditor.created_utc
        self.progression_dict = {}
        
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        