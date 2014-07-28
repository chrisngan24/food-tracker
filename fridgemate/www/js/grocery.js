var Grocery = Grocery || {};

Grocery.initialize = function(){
	var user = Model.user.getUser();
	var inventory = Model.inventory.getInventory();	

	var groceryList = Grocery.generateGroceryList(user, inventory);
	Grocery.renderList(groceryList);

};

Grocery.generateGroceryList = function(user, inventory){
	var wishList = user['grocery_list'];	
	var inventoryList = {};
	for(var i = 0; i < inventory.length; i++) {
		inventoryList[(inventory[i]['item_name'])] = 1;
	}
	var groceryList = []
	for (var i =0; i < wishList.length; i++){
		if (inventoryList[wishList[i]] == null){
			groceryList.push(wishList[i]);
		}
	}

	return groceryList;
};

Grocery.renderList = function(groceryList){
 	$('#groceryList').empty();
	for(var i = 0; i < groceryList.length; i++){
		Grocery.appendGroceryItem(groceryList[i], i);
	}
	$("#groceryList").trigger('create'); 
  
};

Grocery.appendGroceryItem = function(groceryItem, i){
	$('#groceryList').append(
    "<input type='checkbox' id='checkbox-"+i+"'>"+
    "<label class='groceryItem' for='checkbox-"+i+"'>"+ groceryItem +"</label>");
}