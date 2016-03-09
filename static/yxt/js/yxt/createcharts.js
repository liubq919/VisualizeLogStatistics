/**
 * Created by liubq on 12/18/2015.
 */

function draw_charts(operation, menu){
    //clear current content
    $(".specific-chart-div").empty();
    $(".chart-content-div").hide();
    $.getJSON("/static/yxt/js/yxt/menu.json", function(data){
        $.each(data[operation][menu].charts, function(n, value){
            show_charts(value);
        });
    });
}

function show_charts(chartInfo){
    if (!chartInfo || !chartInfo.divID || !chartInfo.ajaxURL || !chartInfo.graphInfo || !chartInfo.graphInfo.type) {
        if ( "pie" == chartInfo.graphInfo.type &&( !chartInfo.graphInfo.titleField || !chartInfo.graphInfo.valueField) ) {
            return;
        }
    }
    var chartDiv = get_chartDiv(chartInfo);
    var divID = chartInfo.divID;
    $('#'+divID).parent().show();

    if ( !chartDiv ){
        return;
    }
    $.ajax({
        type: 'POST',
        url: chartInfo.ajaxURL,
        data: get_postData(chartInfo),
        success: function (data){
            if ( 200 == data.status ){
                //console.log(data.content);
                var ajax_data = JSON.parse(data.content);
                if ( ajax_data.date && ajax_data.info ) {
                    chartDiv.dataProvider = ajax_data.info;
                    var title = ( "" == chartInfo.graphInfo.title || !chartInfo.graphInfo.title)? ajax_data.date: chartInfo.graphInfo.title;
                    chartDiv.addTitle(title, 16);
                    chartDiv.validateData();
                }
            }
            else{
                console.log("Failed to load data...");
            }
        }
    });
}

function get_chartDiv(chartInfo){
    var chartType = chartInfo.graphInfo.type;
    var chartDiv = null;
    switch(chartType){
        case "pie":
            chartDiv = create_pie_chart(chartInfo);
            break;
        case "serial":
            chartDiv = create_a_serial_chart(chartInfo);
            break;
        case "funnel":
            chartDiv = createFunnelChart(chartInfo);
            break;
        case "curve":
            chartDiv = create_a_curved_line_chart(chartInfo);
            break;
        case "curve7":
            chartDiv = create_a_curved_line_chart_with_seven_data(chartInfo);
            break;
        default :
            return;
    }
    return chartDiv;
}

function get_postData(chartInfo){

    var csrftoken = Cookies.get('csrftoken');

    var postData = null;
    if ( chartInfo.postData ){
        postData = JSON.stringify(chartInfo.postData).replace("}", ", \"csrfmiddlewaretoken\":\"" + csrftoken + "\"}");
    }
    else{
        postData = "{\"csrfmiddlewaretoken\":" + csrftoken + "}";
    }

    return JSON.parse(postData);
}

function create_pie_chart( chartInfo ){

    if ( !chartInfo.divID || !chartInfo.graphInfo){
        return;
    }

    var divID = chartInfo.divID;
    var graphInfo = chartInfo.graphInfo;

    var chartDivWithID = AmCharts.makeChart(divID,{
        "type" : 'pie',
        'theme': 'light',
        "titleField"  : graphInfo.titleField,
        "valueField"  : graphInfo.valueField,
        "outlineColor": "#FFFFFF",
        "outlineAlpha": 0.8,
        "outlineThickness": 2,
        "balloonText": "[[title]]<br><span style='font-size:14px'><b>[[counter]]</b> ([[percents]]%)</span>",
        "depth3D": 15,
        "angle": 30,
        "dataProvider"  : []
    });

    return chartDivWithID
}

function create_a_serial_chart(chartInfo){

    if ( !chartInfo.divID || !chartInfo.graphInfo){
        return;
    }

    var divID = chartInfo.divID;
    var graphInfo = chartInfo.graphInfo;

    var chartDivWithID = AmCharts.makeChart(divID,{
        "type": "serial",
        'theme': 'light',
        "categoryField": "time",
        "startDuration": 1,
        "marginRight": -10,
        "sequencedAnimation": false,
        "categoryAxis": {
            "gridAlpha": 0,
            "axisAlpha": 0,
            "gridPosition": "start",
            "title": graphInfo.categoryAxis_title
        },
        "valueAxes":[
            {
                "axisAlpha": 0,
                "gridAlpha": 0,
                "unit": graphInfo.valueAxes_unit
            }
        ],
        "graphs": [
        {
            "valueField": "times",
            "colorField": "color",
            "balloonText": "<b>[[category]]: [[value]]</b>",
            "type": "column",
            "lineAlpha": 0.5,
            "lineColor": "#FFFFFF",
            "topRadius": 1,
            "fillAlphas": 0.9,
            "color": "#FF6600"
        }
        ],
        "chartCursor": {
            "cursorAlpha": 0,
            "zoomable": false,
            "categoryBalloonEnabled": false,
            "valueLineEnabled": true,
            "valueLineBalloonEnabled": true,
            "valueLineAlpha": 1
        },
        "creditsPosition":"top-right"
    });

    return chartDivWithID;
}

function createFunnelChart(chartInfo){
    if ( !chartInfo.divID || !chartInfo.graphInfo){
        return;
    }

    var divID = chartInfo.divID;
    var graphInfo = chartInfo.graphInfo;

    var chartDivWithID = AmCharts.makeChart(divID, {
        'type': 'funnel',
        'theme': 'light',
        'rotate': true,
        'titleField': graphInfo.titleField,
        'valueField': graphInfo.valueField,
        'balloon': {
            'fixedPosition': true
        },
        'marginRight': 210,
        'marginLeft': 15,
        'labelPosition': "right",
        'funnelAlpha': 0.9,
        'startX': -500,
        'startAlpha': 0,
        'neckWidth': '10%',
        'neckHeight': '30%'
    });

    return chartDivWithID;
}

function create_a_curved_line_chart(chartInfo){
    if ( !chartInfo.divID || !chartInfo.graphInfo){
        return;
    }

    var divID = chartInfo.divID;
    var graphInfo = chartInfo.graphInfo;

    var chartDivWithID = AmCharts.makeChart(divID, {
        'type': 'serial',
        'categoryField': 'time',
        'startDuration': 0.5,
        'balloon': {
            'color': "#000000"
        },
        "categoryAxis": {
            'fillAlpha': 1,
            'fillColor': '#FAFAFA',
            'gridAlpha': 0,
            'axisAlpha': 0,
            'gridPosition': 'start',
            'title': graphInfo.categoryAxis_title

        },
        "valueAxes": [
            {
                'dashLength': 5,
                'axisAlpha': 0,
                'minimum': 1,
                'integersOnly': true,
                'gridCount': 10,
                'reversed': false,
                'unit': graphInfo.valueAxes_unit
            }
        ],
        'graphs': [
            {
                'valueField': 'value',
                'balloonText': "[[category]]: [[value]]",
                'lineAlpha': 1,
                'bullet': "round"
            }
        ],
        'chartCursor':{
            'cursorPosition': 'mouse',
            'zoomable': false,
            'cursorAlpha': 0
        }
    });

    return chartDivWithID;
}

function create_a_curved_line_chart_with_seven_data(chartInfo){
    if ( !chartInfo.divID || !chartInfo.graphInfo){
        return;
    }

    var divID = chartInfo.divID;
    var graphInfo = chartInfo.graphInfo;

    var weekList = get_a_week();

    var chartDivWithID = AmCharts.makeChart(divID, {
        'type': 'serial',
        'categoryField': 'time',
        'balloon':{
            'borderAlpha': 0.8,
            'borderThickness': 0.5,
            'color': '#999999'
        },
        "categoryAxis": {
            'fillAlpha': 1,
            'fillColor': '#FAFAFA',
            'gridAlpha': 0,
            'axisAlpha': 0,
            'gridPosition': 'start',
            'title': graphInfo.categoryAxis_title

        },
        "valueAxes": [
            {
                'dashLength': 5,
                'axisAlpha': 0,
                'minimum': 1,
                'integersOnly': true,
                'gridCount': 10,
                'reversed': false,
                'unit': graphInfo.valueAxes_unit
            }
        ],
        'graphs': [
            {
                'id': weekList[0],
                'title': weekList[0],
                'valueField': 'value1',
                'balloonText': "[[title]]:[[category]]: [[value]]",
                'lineThickness': 3
            }
        ],
        'chartCursor':{
            'cursorPosition': 'mouse',
            'zoomable': false,
            'cursorAlpha': 0
        },
        'legend':{
            'useGraphSettings': true
        }
    });

    for (var i = 1; i < 7; i ++ ){
        var graph = new AmCharts.AmGraph();

        graph.id = weekList[i];
        graph.title =  weekList[i];
        graph.valueField = "value" + ( i + 1 );
        graph.lineThickness= 1;
        graph.lineAlpha = 0.5;
        graph.balloonText = "[[title]]: [[category]]: [[value]]";
        if (isOnWeekend(weekList[i])){
            graph.hidden = true;
        }
        chartDivWithID.addGraph(graph);
    }

    return chartDivWithID;
}

function isOnWeekend(date){
    var index = Date.parse(date).getDay();

    return ( index == 6 || index == 0);
}

function get_a_week(){
    var weekList = new Array();
    for ( var i =1; i < 8; i ++){
        weekList.push((i).days().ago().toString('yyyy-MM-dd'));
    }
    return weekList;
}
