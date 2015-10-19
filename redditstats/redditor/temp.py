
import praw
import time
import datetime
from datetime import date


def utc_to_string(utc):
    return time.strftime("%b  %d, %Y", date.timetuple(date.fromtimestamp(utc)))
        
    
def string_to_utc(string):
    return time.mktime(datetime.datetime.strptime(string, "%b  %d, %Y").timetuple())
        
        
    
    
    
    
r = praw.Reddit("/u/habnpam testing stufffffff")

s = r.get_redditor("habnpam")



defaults = ['announcements', 'Art', 'AskReddit', 'askscience',
                    'aww', 'blog', 'books', 'creepy', 'dataisbeautiful',
                    'DIY', 'Documentaries', 'EarthPorn', 'explainlikeimfive',
                    'Fitness', 'food', 'funny', 'Futurology', 'gadgets',
                    'gaming', 'GetMotivated', 'gifs', 'history', 'IAmA',
                    'InternetIsBeautiful', 'Jokes', 'LifeProTips', 'listentothis',
                    'mildlyinteresting', 'movies', 'Music', 'news', 'nosleep',
                    'nottheonion', 'OldSchoolCool', 'personalfinance',
                    'philosophy', 'photoshopbattles', 'pics', 'science',
                    'Showerthoughts', 'space', 'sports', 'television', 'tifu',
                    'todayilearned', 'TwoXChromosomes', 'UpliftingNews',
                    'videos', 'worldnews', 'WritingPrompts']
                    
                    
                    




mod_dict = {}
mod_array = []

exempt = ['multi-mod', 'Automoderator', 'botwatchman'
'raddit-bot', 'Mod_Button_Bot', 'roger_bot', 'imalittleteabot']
for d in defaults:
    subreddit = r.get_subreddit(subreddit_name=d)
    
    mods = subreddit.get_moderators()
    
    print("Checking /r/" + d + ", " + str(len(mods)))
    for m in mods:
        name = str(m.name)
        if (str(name) not in exempt) and ("bot" not in name):
            try:
                mod_dict[str(m.name)].append(d)
            except:
                mod_dict[str(m.name)] = [d]
                


for m in mod_dict:
    if len(mod_dict[m]) > 2:
        print(m, mod_dict[m])
        
        

        
    
    
    
    
    
    
    
    
    
    
    
    
    
    