/* Code to animate logo on mouse hover */
$(function () {
    $(".playgif").hover(function () {
        var stat = $(this).find("img").attr("src");
        $(this).find("img").attr("src", $(this).find("img").data("swap"));
        $(this).find("img").data("swap", stat);
    })
});


/*Code to expand images on click*/
$(document).ready(function(){
    $('.materialboxed').materialbox({
        inDuration:275,
        outDuration:200,
        onOpenStart: function() {console.log("onOpenStart");},
        onOpenEnd: function() {console.log("onOpenEnd");},
        onCloseStart: function() {console.log("onCloseStart");},
        onCloseEnd: function() {console.log("onCloseEnd");}
    });
});
