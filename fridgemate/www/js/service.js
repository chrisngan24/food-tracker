var Service = {};

Service.loadData = function(BASE_URL, userId, callback){
  Service.loadInventory(BASE_URL, userId, function(){
    Service.loadUser(BASE_URL, userId, callback);
  })
};

Service.loadInventory = function(BASE_URL, userId, callback){
  $.ajax({
    url: BASE_URL + '/api/v1/inventory?user_id='+userId,
    type: 'GET',
    success: function(data){
      Model.inventory.setInventory(data);
      if (callback) callback();
    }
  });	
};

Service.loadUser = function(BASE_URL, userId, callback){
	$.ajax({
		url: BASE_URL + '/api/v1/user?user_id=' + userId,
		type: 'GET',
		success: function(data){
      Model.user.setUser(data);
      if (callback) callback();
		}
	});
};