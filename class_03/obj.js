function Fruit(name='', color='') {
	this.name = name;
	this.color = color;

	this.getColor = function () {
		return this.color;
	}
}

var a = new Fruit(name='apple', color='red');

console.log(a);
console.log(a.name);

//EventListeners