/* TODO
- function for plural, add s for days or inventory name (since we are just doing carrots and apples
- set default date for entering food items as today
 */

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
    $('.inventoryItem').last().data('item-id', data[i]['id']);
    $('.inventoryItem').last().data('status', status);
    $('.inventoryItem').last().data('days', daysInFridge);
  }
  $("#inventoryTable").listview('refresh'); 
}
function manualAdd(){
  sendStuff={
    item_name: String($('#foodItem').val()),
    time_in:setDate($("#dateIn").val()),
    camera_id : userId,
    count: parseInt($('#numOfItem').val()),
  };
  $.ajax({
    url:"http://shrouded-beyond-1547.herokuapp.com/api/v1/add_entry",
    type: "POST",
    data:JSON.stringify(sendStuff),
    dataType: 'json',
    contentType: 'application/json',
  });
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
  if (status =="eatSoon")
    return 'fa fa-meh-o';
  else if (status=="spoiled")
    return 'fa fa-frown-o';
  else
    return 'fa fa-smile-o';
}
function insertDefaultDate(){
	date = new Date();
	d = date.getDate();
	m = date.getMonth()+1;
	y = date.getFullYear();

  if(m < 10) 
    m = "0" + m;
  if(d < 10) 
    d = "0" + d;
  $("#dateIn").val(y+'-'+m+'-'+d);
}
function setDate(timeIn){
  now = new Date();
  hours = now.getUTCHours()*3600*1000;
  minutes = now.getUTCMinutes()*60*1000;
  seconds = now.getUTCSeconds()*1000;
  d = new Date(timeIn);
  newTime=(d.getTime()+ hours+minutes+seconds)/1000;
  return String(newTime);
}
function setRecordPopup(itemId, itemStatus, itemDays){
  $("#itemRecord").popup("open");
  record = listOfFood.filter(function(el){return (el.id==itemId);});
  
  $('#recFoodItem').empty();
  $('#recFoodItem').append(record[0].item_name);
  
  $('#recStatus').empty();
  $('#recStatus').append(itemStatus);
  
  $('#recDays').empty();
  $('#recDays').append(itemDays);
  
  $('#recNumOfItem').val(record[0].count);
}
function sendUpdate(){
  sendThings={
    id:String(record[0].id),
    count: parseInt($('#recNumOfItem').val()),
  };
  $.ajax({
    url:'http://29432714.ngrok.com/api/v1/update_entry',
    type:'POST',
    data:JSON.stringify(sendThings),
    dataType: 'json',
    contentType: 'application/json',
  });
}