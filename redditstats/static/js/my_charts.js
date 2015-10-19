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
        var options = {
          title: 'Karma Progression',
          
          legend: { position: 'bottom' },
          width: 600,
          height: 480
          
        };

        var chart = new google.visualization.LineChart(document.getElementById('karma-progression'));

        chart.draw(data, options);

    });
    
    /*WordCloud2 Chart*/
    googleChartStack.push(function (){

      
    });
    
    
    /* 
    googleChartStack.push(function() {
        
    });*/
    
    
    
  
}



function drawWordCloud(){
    
    listt = []
      
    for (i = 0; i < cloud_list.length; i++){
        listt.push(cloud_list[i]);
    }
    
    
	
    var docWidth = $(document).width();  
    /*$('#word-cloud').width(docWidth * 5 / 6);*/

    
    var options = {
        
        list: listt,
        click: clickedWordCloud,
        color: "random-dark",
        shuffle: true,
        gridSize: Math.round(16 * $('#word-cloud').width() / 1024),
        
        
    }
    WordCloud(document.getElementById('word-cloud'), options );



}

function clickedWordCloud(item, dimension, event){
    alert(item);
}
$(document).ready(function () {
    
    createCharts();

    drawAllChart();
    
    drawWordCloud();
});
