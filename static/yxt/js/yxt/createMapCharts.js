/**
 * Created by liubq on 1/15/2016.
 */
function draw_map_charts(operation, menu){
    //clear current content
    $(".specific-chart-div").empty();
    $(".chart-content-div").hide();
    $.getJSON("/static/yxt/js/yxt/dist_menu.json", function(data){
        $.each(data[operation][menu].charts, function(n, value){
            show_map_charts(value);
        });
    });
}

function show_map_charts(chartInfo){
    if ( !chartInfo || 2 != chartInfo.divID.length || 2 != chartInfo.ajaxURL.length ){
        return
    }

    $('#'+chartInfo.divID[0]).parent().parent().parent().show();


    var myChart = echarts.init(document.getElementById(chartInfo.divID[0]));
    $.ajax({
        type: 'POST',
        url: chartInfo.ajaxURL[0],
        data: 'type=' + chartInfo.postData.type,
        success: function (data){
            if ( 200 == data.status ){
                var ajax_data = JSON.parse(data.content);
                if ( ajax_data.date && ajax_data.provinces ) {

                    var option = {
                        "title": {
                            "text": ajax_data.date,
                            "left": "center"
                        },
                        "tooltip": {
                            "trigger": "item"
                        },
                        "legend": {
                            "orient": "vertical",
                            "left": "left",
                            "data":['访问人数']
                        },
                        "visualMap": {
                            "min": 0,
                            "max": ajax_data.provinces[0].value,
                            "left": "left",
                            "top": "bottom",
                            "color":["#CD0000", "#EE2C2C", "#EE4000", "#FFEC8B", "#FFF68F", "#FFFACD", "#FFFFE0"],
                            "text":["高", "低"],           // 文本，默认为数值文本
                            "calculable": true
                        },
                        "toolbox": {
                            "show": true,
                            "orient": "vertical",
                            "left": "right",
                            "top": "center",
                            "feature": {
                                "mark": {
                                    "show": true
                                },
                                "dataView":
                                {
                                    "show": true,
                                    "readOnly": false
                                },
                                "restore":
                                {
                                    "show": true
                                },
                                "saveAsImage":
                                {
                                    "show": true
                                }
                            }
                        },
                        "series": [
                            {
                                "name": "访问人数",
                                "type": "map",
                                "mapType": "china",
                                "roam": false,
                                "label": {
                                    "normal":{
                                        "show":true,
                                        "textStyle": {
                                            "fontWeight": "normal",
                                            "fontSize": 12
                                        }
                                    },
                                    "emphasis": {
                                        "show": true
                                    }
                                },
                                "itemStyle": {
                                    "emphasis": {
                                        "borderWidth": 1.5
                                    }
                                },
                                data: ajax_data.provinces
                            }
                        ]
                    };
                    myChart.setOption(option);

                }
            }
            else{
                console.log("Failed to load data...");
            }
        }
    });

    myChart.dispatchAction({
        'type': 'click'
    });

    myChart.on('click', function(event){
        var provinceName = event.name;
        if (provinceName && '' != provinceName ){
            $.ajax({
                type: 'POST',
                url: chartInfo.ajaxURL[1],
                data: 'type=' + chartInfo.postData.type + ';province=' + provinceName,
                success: function (data){
                    if ( 200 == data.status ){
                        var ajax_data = JSON.parse(data.content);
                        var mapCities = echarts.init(document.getElementById(chartInfo.divID[1]));
                        var citiesOption = {
                            "title" : {
                                "text": provinceName,
                                "left": "center"
                            },
                            "tooltip": {
                                "trigger": "item"
                            },
                            "visualMap": {
                                "min": 0,
                                "max": ajax_data.cities[0].value,
                                "left": "left",
                                "top": "bottom",
                                "color":["#CD0000", "#EE2C2C", "#EE4000", "#FFEC8B", "#FFF68F", "#FFFACD", "#FFFFE0"],
                                "text":["高","低"],
                                "calculable": true
                            },
                            "series" : [
                                {
                                    "type": "map",
                                    "name": "访问人数",
                                    "mapType": provinceName,
                                    "roam": false,
                                    "label": {
                                        "normal":{
                                            "show":true,
                                            "textStyle": {
                                                "fontWeight": "normal",
                                                "fontSize": 12
                                            }
                                        },
                                        "emphasis": {
                                            "show": true
                                        }
                                    },
                                    "itemStyle": {
                                        "emphasis": {
                                            "borderWidth": 1.5
                                        }
                                    },
                                    "data": ajax_data.cities
                                }
                            ]
                        };
                        mapCities.setOption(citiesOption);
                    }
                    else{
                        console.log("Failed to load data...");
                    }
                }
            });
        }
    });
}