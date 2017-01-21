var canvas = document.getElementById('space');
var ctx = canvas.getContext('2d');

var x = canvas.width/2;
var y = canvas.height/2;
var radius = 30;

var dx = 1;
var dy = 1;

function drawRect(x, y, w, h, color='#ff0000') {
	ctx.beginPath();
	ctx.rect(x, y, w, h);
	ctx.fillStyle = color;
	ctx.fill();
	ctx.closePath();
}

function drawCircle(x, y, r, color='#00ff00') {
	ctx.beginPath();
	ctx.arc(x, y, r, 0, Math.PI*2);
	ctx.fillStyle = color;
	ctx.fill();
	ctx.closePath();
}

function draw() {
	ctx.clearRect(0, 0, canvas.width, canvas.height);
	drawCircle(x, y, radius);
	x += dx;
	y += dy;

	if (x + dx < radius || x + dx > canvas.width - radius) {
		dx = -dx;
	}
	if (y + dy < radius || y + dy > canvas.height - radius) {
		dy = -dy;
	}
}

function startSimulation(frameInterval=10) {
	var sim = setInterval(draw, frameInterval);
}

//---------------- start -------------//
startSimulation(10);