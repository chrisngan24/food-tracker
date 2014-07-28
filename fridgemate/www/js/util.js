var Util = Util || {};

Util.appendFooter = function(){
	$.get("footer.html", function(data){
    $("[data-role='footer']").empty();
    $("[data-role='footer']").append(data).trigger("create"); 
  });
};