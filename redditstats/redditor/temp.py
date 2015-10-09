
import praw
import time
import datetime
from datetime import date




def utc_to_string(utc):
    return time.strftime("%b  %d, %Y", date.timetuple(date.fromtimestamp(utc)))
        
    
def string_to_utc(string):
    return time.mktime(datetime.datetime.strptime(string, "%b  %d, %Y").timetuple())
        
        
    
    
    
    
r = praw.Reddit("/u/habnpam testing stuff")


me = r.get_redditor("habnpam")


t = me.comment_karma

print(t)