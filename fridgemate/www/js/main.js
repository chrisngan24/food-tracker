var userId='012';
  var listOfFood;
  $(document).on('pageinit', '#index', function(){
    $.get("footer.html", function(data){
      $("[data-role='footer']").append(data).trigger("create");
    });
    $('fa-list').click();
  });
  $(document).on('pageshow','#inventory', function () {
    $.ajax({
      url:"http://shrouded-beyond-1547.herokuapp.com/api/v1/inventory?user_id="+userId,
      type: "GET",
      success: function (data){
        renderList(data)
        listOfFood = data;
        $(".inventoryItem").click(function(){
          itemId = $(this).data('item-id');
          itemStatus = $(this).data('status');
          itemDays = $(this).data('days');
          setRecordPopup(itemId, itemStatus, itemDays);
        });
        //change taphold to swipe
        $('.inventoryItem').on('taphold',function(){
          console.log('yooo');
          $(this).hide();
        });
        $("#itemRecord").bind('popupbeforeposition', function(){
          $("#recSubmit").on('click', function(){
            sendUpdate();
          });
        });
      },
    });
    //adding item popup
    $('#addItem').bind('popupbeforeposition', function(){
      insertDefaultDate();
      $('#puSubmit').on('tap', function(){
        manualAdd();
      });
    });
  }); 