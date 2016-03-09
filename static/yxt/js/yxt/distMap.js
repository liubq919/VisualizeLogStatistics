/**
 * Created by liubq on 1/12/2016.
 */
$(document).ready(function(){

    var myChart = echarts.init(document.getElementById('mapProvinces1'));

    $.ajax({
        type: 'POST',
        url: '/lecai/index_login_distribution_provinces/',
        data: 'type=1',
        success: function (data){
            if ( 200 == data.status ){
                //console.log(data.content);
                var ajax_data = JSON.parse(data.content);
                if ( ajax_data.date && ajax_data.provinces ) {

                    var option = {
                        title : {
                            text: ajax_data.date,
                            left: 'center'
                        },
                        tooltip : {
                            trigger: 'item'
                        },
                        legend: {
                            orient: 'vertical',
                            left: 'left',
                            data:['访问人数']
                        },
                        visualMap: {
                            min: 0,
                            max: 200,
                            left: 'left',
                            top: 'bottom',
                            color:['#016D6D', '#DEECEC'],
                            text:['高','低'],           // 文本，默认为数值文本
                            calculable : true
                        },
                        toolbox: {
                            show: true,
                            orient : 'vertical',
                            left: 'right',
                            top: 'center',
                            feature : {
                                mark : {show: true},
                                dataView : {show: true, readOnly: false},
                                restore : {show: true},
                                saveAsImage : {show: true}
                            }
                        },
                        series : [
                            {
                                name: '访问人数',
                                type: 'map',
                                mapType: 'china',
                                roam: false,
                                itemStyle:{
                                    normal:{
                                        label:{show:true}
                                    },
                                    emphasis:{
                                        label:{show:true}
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
                url: '/lecai/index_login_distribution_cities/',
                data: 'type=1;province=' + provinceName,
                success: function (data){
                    if ( 200 == data.status ){
                        var ajax_data = JSON.parse(data.content);
                        var mapCities = echarts.init(document.getElementById('mapCities1'));
                        var citiesOption = {
                            tooltip : {
                                trigger: 'item'
                            },
                            visualMap: {
                                min: 0,
                                max: 80,
                                left: 'left',
                                top: 'bottom',
                                color:['#016D6D', '#DEECEC'],
                                text:['高','低'],           // 文本，默认为数值文本
                                calculable : true
                            },
                            series : [
                                {
                                    type: 'map',
                                    mapType: provinceName,
                                    roam: false,
                                    itemStyle:{
                                        normal:{label:{show:true}},
                                        emphasis:{label:{show:true}}
                                    },
                                    data: ajax_data.cities
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
});
