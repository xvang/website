





google.load("visualization", "1", {packages:["corechart", "calendar"]});
google.setOnLoadCallback(drawAllChart);



function drawAllChart() {
    for (var i = googleChartStack.length - 1; i >= 0; i--) {
        googleChartStack[i]();
    }
}
function createCharts() {
    
    /* SUBREDDIT SUBMISSIONS PIE CHART*/
    googleChartStack.push(function() {
        
        
        /* For some reason the array from Django doesn't work, so we have
           to make an array here. The array is suppose to look like this: [[1,2],[1,2],[1,2]]
           But when passed to HTML and Javascript it probably becomes this: [1,2,1,2,1,2]
           But when I alert the 1st element of the array from django, I still get 1,2 
           So I don't know anymore, but the way below works, so I'm going with that.*/
           
        data_copy = [];
        data_copy.push(['Subreddit', 'Number of Posts']);
        for (i = 0; i < pie_submission_subreddit.length; i++) {
            data_copy.push(pie_submission_subreddit[i]);
            
        }

        var data = google.visualization.arrayToDataTable(data_copy);

        
        var options = {
          title: 'Submissions by Subreddits',
          width: 600,
          height: 480
        };

        var chart = new google.visualization.PieChart(document.getElementById('pie-submission'));

        chart.draw(data, options);

    });
    
    /* SUBREDDIT KARMA PIE CHART*/
    googleChartStack.push(function() {
        
        
        /* For some reason the array from Django doesn't work, so we have
           to make an array here. The array is suppose to look like this: [[1,2],[1,2],[1,2]]
           But when passed to HTML and Javascript it probably becomes this: [1,2,1,2,1,2]
           But when I alert the 1st element of the array from django, I still get 1,2 
           So I don't know anymore, but the way below works, so I'm going with that.*/
           
        data_copy = [];
        data_copy.push(['Subreddit', 'Number of Posts']);
        for (i = 0; i < pie_karma_subreddit.length; i++) {
            data_copy.push(pie_karma_subreddit[i]);
            
        }

        var data = google.visualization.arrayToDataTable(data_copy);

        
        var options = {
          title: 'Karma by Subreddits',
          width: 600,
          height: 480
        };

        var chart = new google.visualization.PieChart(document.getElementById('pie-karma'));

        chart.draw(data, options);

    });
    
   
    
    
    /* KARMA PROGRESSION DOUBLE LINE CHART */
    googleChartStack.push(function (){
        
        
        data_copy = []
        
        
        
        
        data_copy.push(['Date', 'Comment Karma', 'Link Karma']);
        for (i = 0; i < karma_progression.length; i++){
            data_copy.push(karma_progression[i]);
        }
        
        
        var data  = google.visualization.arrayToDataTable(data_copy);
        /*var data = google.visualization.arrayToDataTable([
          ['Year', 'Sales', 'Expenses'],
          ['2004',  1000,      400],
          ['2005',  1170,      460],
          ['2006',  660,       1120],
          ['2007',  1030,      540]
        ]);*/

        var options = {
          title: 'Karma Progression',
          curveType: 'function',
          legend: { position: 'bottom' },
          width: 600,
          height: 480
          
        };

        var chart = new google.visualization.LineChart(document.getElementById('karma-progression'));

        chart.draw(data, options);

    });
    
    
    googleChartStack.push(function (){

        data_copy = [];
    
        /*data from django is stored: [ [1,2,3,4],[1,2,3,4],[1,2,3,4] ]
          1 is the year, 2 is the month, 3 is the day, 4 is the karma count.
          
          data_copy is stored: [ Date(year, month, day), karma_count ]
          */
        
      
        for (i = 0; i < calendar_act.length; i++){
            
            var date = new Date(calendar_act[i][0], calendar_act[i][1], calendar_act[i][2]);
            
           
            data_copy.push([ date, calendar_act[i][3]]);
        }
        

        /*d = new Date(calendar_act[1][0], calendar_act[1][1], calendar_act[1][2]);
        alert(new Date(calendar_act[1][0], calendar_act[1][1], calendar_act[1][2]););
       */
        var dataTable = new google.visualization.DataTable();
       dataTable.addColumn({ type: 'date', id: 'Date' });
       dataTable.addColumn({ type: 'number', id: 'Karma That Day' });
       /*dataTable.addRows([
          [ new Date(2012, 0, 13), 37032 ],
          [ new Date(2012, 0, 14), 38024 ],
          [ new Date(2012, 0, 15), 38024 ],
          [ new Date(2012, 0, 16), 38108 ],
          [ new Date(2012, 0, 17), 38229 ],
          // Many rows omitted for brevity.
          [ new Date(2013, 10, 4), 38177 ],
          [ new Date(2013, 10, 5), 38705 ],
          [ new Date(2013, 10, 12), 38210 ],
          [ new Date(2013, 10, 13), 38029 ],
          [ new Date(2013, 10, 19), 38823 ],
          [ new Date(2013, 10, 23), 38345 ],
          [ new Date(2013, 10, 24), 38436 ],
          [ new Date(2013, 10, 30), 38447 ]
        ]);*/
        
        dataTable.addRows(data_copy);

       var chart = new google.visualization.Calendar(document.getElementById('calendar-submission-frequency'));

       var options = {
         title: "Posts per day Calendar"
         
       }
        chart.draw(dataTable, options);
    });
     /*
    googleChartStack.push(function() {
        
        
        data_copy = []
        
        data_copy.push(['ID', '1', '2', '3', '4', '5']);
        for (i = 0; i < karma_progression.length; i++){
            data_copy.push(karma_progression[i]);
        }
   
        var data = google.visualization.arrayToDataTable([
            ['ID', 'Life Expectancy', 'Fertility Rate', 'Region',     'Population'],
            ['CAN',    80.66,              1.67,      'North America',  33739900],
            ['DEU',    79.84,              1.36,      'Europe',         81902307],
            ['DNK',    78.6,               1.84,      'Europe',         5523095],
            ['EGY',    72.73,              2.78,      'Middle East',    79716203],
            ['GBR',    80.05,              2,         'Europe',         61801570],
            ['IRN',    72.49,              1.7,       'Middle East',    73137148],
            ['IRQ',    68.09,              4.77,      'Middle East',    31090763],
            ['ISR',    81.55,              2.96,      'Middle East',    7485600],
            ['RUS',    68.6,               1.54,      'Europe',         141850000],
            ['USA',    78.09,              2.05,      'North America',  307007000]
          ]);
            
         

          var options = {
            title: 'Correlation between life expectancy, fertility rate and population of some world countries (2010)',
            hAxis: {title: 'Life Expectancy'},
            vAxis: {title: 'Fertility Rate'},
            bubble: {textStyle: {fontSize: 11}},
            width: 600,
            height: 480
          };

          var chart = new google.visualization.BubbleChart(document.getElementById('chart2'));
          chart.draw(data, options);
    });*/
  
}



$(document).ready(function () {
    
    createCharts();

    drawAllChart();
});
