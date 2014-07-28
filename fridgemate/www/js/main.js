var userId='012';
var BASE_URL = "http://shrouded-beyond-1547.herokuapp.com";
// var BASE_URL = "http://29432714.ngrok.com";

$(document).on('pageinit', '#index', function(){
  Service.loadData(BASE_URL, userId, function(){
    $.mobile.changePage("#inventory");
  });
});
$(document).on('pageshow','#inventory', function () {
  data = Model.inventory.getInventory(); 
  renderList(data)

  $.get("footer.html", function(data){
    $("[data-role='footer']").empty();
    $("[data-role='footer']").append(data).trigger("create"); 
  });
  

  $('.inventoryItem').on('taphold',function(){
    console.log('yooo');
    $(this).hide();
  });
  $("#itemRecord").bind('popupbeforeposition', function(){
    $("#recSubmit").on('click', function(){
      sendUpdate();
    });
  });
  //adding item popup
  $('#addItem').bind('popupbeforeposition', function(){
    $('input').val('');
    
    insertDefaultDate();
    $('#dateHide').hide();
    $('#puSubmit').unbind();
    $('#puSubmit').on('tap', function(){
      manualAdd(BASE_URL);
    });
  });
}); 


$(document).on('pageshow','#grocery', function () {
  Grocery.initialize();
  Util.appendFooter();
});


