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
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        