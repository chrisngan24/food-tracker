var userId='012';
var BASE_URL = "http://shrouded-beyond-1547.herokuapp.com";

$(document).on('pageinit', '#index', function(){
  Service.loadData(BASE_URL, userId);
  $.mobile.changePage("#inventory");
});
$(document).on('pageshow','#inventory', function () {
  data = Model.inventory.getInventory(); 
  renderList(data)

  $.get("footer.html", function(data){
    $("[data-role='footer']").empty();
    $("[data-role='footer']").append(data).trigger("create"); 
  });
  
  $(".inventoryItem").click(function(){
    itemId = $(this).data('item-id');
    itemStatus = $(this).data('status');
    itemDays = $(this).data('days');
    setRecordPopup(data, itemId, itemStatus, itemDays);
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
    insertDefaultDate();
    $('#puSubmit').on('tap', function(){
      manualAdd(BASE_URL);
    });
  });
}); 


