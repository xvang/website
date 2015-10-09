from django.shortcuts import render

from redditManager import RedditManager


try:
    import json
except:
    import django.utils.simplejson as json
# Create your views here.



redditManager = RedditManager()




from wordbank.models import Word





def index(request):
    context_dict = {'message':''}
    return render(request, 'index.html', context_dict)



def search(request):
    
    context_dict = {}
    
    #If input was blank, it is handled here.
    try:
        if request.GET['username'] == '':
            index(request)
    except:
        return render(request, 'error.html', {})
        
    
    #if username did not exist, it is handled here.
    context_dict['user_exists'] = redditManager.user_exists(request.GET['username'])
    if not (context_dict['user_exists']):
        context_dict['message'] = "User does not exist."
        return render(request, 'index.html', context_dict)
        
    #<<<<<------------------------------------------------------------->>>>>
    #If we get to here, then the user exists.
    context_dict['username'] = request.GET['username']
    
    #get a random word that describes the user.
    word = Word()
    context_dict['adjective'] = word.get_random_adjective()
    
    
    context_dict['reddit'] = redditManager.gather_info(username=request.GET['username'])

    #context_dict['flot_line'] = chartManager.flot_line_chart()

    #Gather all the stats.
    redditManager.gather_data()
    
    context_dict['subreddit_counter'] =redditManager.subreddit_pie_chart()
    
    context_dict['karma_counter'] = redditManager.karma_counter_pie_chart()
    
    context_dict['karma_progression'] = redditManager.karma_progression_line_chart()

    
    context_dict['xengxeng'] = "xeng was here"
    
    context_dict['pie_subreddit'] = json.dumps(redditManager.subreddit_pie_chart())
    return render(request, 'search_results.html', context_dict)
  

  

def test_func(request):
    
    context_dict = {}
    
    context_dict['values'] = [['foo', 32], ['bar', 64], ['baz', 96], ['dd', 100]]
    
    
    return render(request, 'test.html', context_dict)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    