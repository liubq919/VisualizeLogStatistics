/**
 * Created by liubq on 1/15/2016.
 */
$(document).ready(function(){

    $("#side-nav-bar-ul").find("a").bind("click", function(){
        // add class active to the link
        $("#side-nav-bar-ul").find("a").removeClass("active");
        $(this).addClass("active");

        var menu = $(this).find("p").text();
        var operationType = $(this).parent().attr("id");
        draw_map_charts(operationType, menu);

    });

    $('#lecai1').click();

});