$(document).ready(function(){
    $("#subscribed").hover(function(){
    	$("#subscribed").removeClass("btn-success subscribe-d");
    	$("#subscribed").addClass("btn-danger");
    	$("#subscribed").html("<svg class=\"icon icon-cancel-circle\"><use xlink:href=\"#icon-cancel-circle\"></use></svg>&nbsp;Unsubscribe");
    },function(){
        $("#subscribed").removeClass("btn-danger");
        $("#subscribed").addClass("btn-success subscribe-d");
        $("#subscribed").html("<svg class=\"icon icon-checkmark\"><use xlink:href=\"#icon-checkmark\"></use></svg>&nbsp; Subscribe");
    });
    $(".errorlist").addClass('alert alert-danger mb-1');
    $("input[id=\"id_title\"]").addClass("form-control");
    $("#id_section").addClass("form-control");
    $("#id_content").addClass("form-control");
});