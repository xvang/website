
import praw
import time
import datetime
from datetime import date




def utc_to_string(utc):
    return time.strftime("%b  %d, %Y", date.timetuple(date.fromtimestamp(utc)))
        
    
def string_to_utc(string):
    return time.mktime(datetime.datetime.strptime(string, "%b  %d, %Y").timetuple())
        
        
    
    
    
    
r = praw.Reddit("/u/habnpam testing stufffffff")

s = r.get_redditor("drewiepoodle").get_comments(limit=None, sort='top')

total = 0

counter = 0
for submission in s:
    total = total + submission.ups
    counter = counter + 1

print(total, counter)
print(total / counter)
    
    