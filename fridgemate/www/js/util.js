/* TODO
- function for plural, add s for days or inventory name (since we are just doing carrots and apples
- set default date for entering food items as today
 */
$(document).on('pageshow','#inventory', function () {
  $.get("footer.html", function(data){
    $("[data-role='footer']").append(data).trigger("create");
  });
  $.ajax({
    url:"http://shrouded-beyond-1547.herokuapp.com/api/v1/get_inventory?user_id=012",
    type: "GET",
    success: function (data){
      renderList(data)
    },
  });
  $('#addItem').bind('popupbeforeposition', function(){
    insertDefaultDate();
  });
}); 

function renderList(data){
  for (i=0; i<data.length; i++){
    daysInFridge = getDaysInFridge(parseInt(data[i]['time_in']));
    status = getStatus (daysInFridge);
    face = getFace (status);
    $('#inventoryTable').append(
      "<li class='inventoryItem'><a><div class='ui-block-a'><i class='face'></i></div>"+
      "<div class='ui-block-b numOfFruit'><h1>"+data[i]['count']+
      "</h1></div><div class='ui-block-c fruit'><h1>"+data[i]['item_name']+
      "</h1></div><div class='ui-block-d numOfDays'><p>"+daysInFridge+
      "</p><p>days</p></div></a></li>");
    $('.inventoryItem').last().addClass(status);
    $('.face').last().addClass(face);
    $("#inventoryTable").listview('refresh'); 
  }
}

function getDaysInFridge(dateIn){
  today = new Date();
  UTCtoday = today.getTime();
  diff = UTCtoday - (dateIn*1000);
  days = diff/(5*60*1000);
  //(24*60*60*1000);
  return parseInt(days);
}
function getStatus (diff){
  THREE_DAYS = 3;
  FIVE_DAYS = 5;
  if (diff>=THREE_DAYS && diff<FIVE_DAYS)
    return "eatSoon";
  else if (diff>= FIVE_DAYS)
    return "spoiled";
  else
    return "normal";
}
function getFace (status){
  if (status ="eatSoon")
    return 'fa fa-meh-o';
  else if (status="spoiled")
    return 'fa fa-frown-o';
  else
    return 'fa fa-smile-o';
}

function insertDefaultDate(){
  today=getToday();
  $("#dateIn").val(today[0]+'-'+today[1]+'-'+today[2]);
}

function getToday(){	
	date = new Date();
	d = date.getDate();
	m = date.getMonth()+1;
	y = date.getFullYear();

  if(m < 10) 
    m = "0" + m;
  if(d < 10) 
    d = "0" + d;
  
  return [y,m,d];
}