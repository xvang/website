





google.load("visualization", "1", {packages:["corechart"]});
google.setOnLoadCallback(drawAllChart);



function drawAllChart() {
    for (var i = googleChartStack.length - 1; i >= 0; i--) {
        googleChartStack[i]();
    }
}
function createCharts() {
    
    googleChartStack.push(function() {
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
            bubble: {textStyle: {fontSize: 11}}
          };

          var chart = new google.visualization.BubbleChart(document.getElementById('calendarChart'));
          chart.draw(data, options);
    });
    
    
    googleChartStack.push(function() {
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
            bubble: {textStyle: {fontSize: 11}}
          };

          var chart = new google.visualization.BubbleChart(document.getElementById('regions_div'));
          chart.draw(data, options);
    });
  
}















$(document).ready(function () {
    
    createCharts();
    
    drawAllChart();
});
