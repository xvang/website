from django.conf.urls import patterns, url
from redditor import views



urlpatterns = patterns('',

    url(r'^index', views.index, name='index'),
    
    url(r'^search/$', views.search, name='search'),
    url(r'test', views.test_func, name='test_func'),
    url(r'', views.index, name='index'),
    
                       



)
