var Model = {};
Model.inventory = Model.inventory || {}; 

Model.INVENTORY_KEY = 'inventory';
Model.inventory.getInventory = function(){
	return JSON.parse(localStorage.getItem(Model.INVENTORY_KEY));
}

Model.inventory.setInventory = function(inventory){
	localStorage.setItem(Model.INVENTORY_KEY, JSON.stringify(inventory));
}