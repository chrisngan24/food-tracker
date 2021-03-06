var Model = {};
Model.inventory = Model.inventory || {}; 
Model.user = Model.user || {}; 
/*
	Inventory Model layer
 */
Model.INVENTORY_KEY = 'inventory';
Model.inventory.getInventory = function(){
	return JSON.parse(localStorage.getItem(Model.INVENTORY_KEY));
}

Model.inventory.setInventory = function(inventory){
	localStorage.setItem(Model.INVENTORY_KEY, JSON.stringify(inventory));
}

/*
	User Model Layer
 */

Model.USER_KEY = 'user';
Model.user.getUser = function(){
	return JSON.parse(localStorage.getItem(Model.USER_KEY));
} 

Model.user.setUser = function(user){
	localStorage.setItem(Model.USER_KEY, JSON.stringify(user));
}
