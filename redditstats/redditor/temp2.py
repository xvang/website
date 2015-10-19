# -*- coding: utf-8 -*-
"""

"""

import praw
import re
import operator

r = praw.Reddit("nana")



redditor = r.get_redditor("habnpam")


comments = redditor.get_comments(limit=100, sort='top')


impact_dict = {}

for c in comments:
    string = str(c.body)
    
    string = re.sub(r'([^\s\w]|_)+', '', string)
    
    string = string.split()
    
    for word in string:
        if word in impact_dict:
            impact_dict[word] = impact_dict[word] + 1
        else:
            impact_dict[word] = 1


xx = sorted(impact_dict.items(), key=operator.itemgetter(1))[-100:]

print(type(xx))

for x in range(0, len(xx)):
    xx[x] = list(xx[x])
    
    
print(xx)