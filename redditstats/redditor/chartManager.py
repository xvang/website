# -*- coding: utf-8 -*-
"""

"""
from chartit import PivotDataPool, PivotChart
from django.db.models import Sum, Avg

from flot.models import Flot

class ChartManager():
    
    
    
    def __init__(self, reddit):
        
        self.redditPointer = reddit
        
        
    
    
    def flot_line_chart(self):
        rainpivotdata = \
        PivotDataPool(
           series =
            [{'options': {
               'source': Flot.objects.all(),
               'categories': ['month']},
              'terms': {
                'avg_rain': Avg('rainfall'),
                'top_n_per_cat': 3}}
             ])

        #Step 2: Create the PivotChart object
        rainpivcht = \
            PivotChart(
                datasource = rainpivotdata,
                series_options =
                  [{'options':{
                      'type': 'column',
                      'stacking': True},
                    'terms':[
                      'avg_rain']}],
                chart_options =
                  {'title': {
                       'text': 'Rain by Month in top 3 cities'},
                   'xAxis': {
                        'title': {
                           'text': 'Month'}}})
                           
        
        return rainpivcht
