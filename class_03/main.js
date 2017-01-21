var canvas = document.getElementById('space');
var ctx = canvas.getContext('2d');

var x = canvas.width/2;
var y = canvas.height/2;
var radius = 100;
var scaleFactor = 2.0;

var dx = 1;
var dy = 1;

function drawRect(x, y, w, h, color='#ff0000') {
	ctx.beginPath();
	ctx.rect(x, y, w, h);
	ctx.fillStyle = color;
	ctx.fill();
	ctx.closePath();
}

function drawCircle(x, y, r, color='#00ff00', fill=true) {
	ctx.beginPath();
	ctx.arc(x, y, r, 0, Math.PI*2);
	if (fill==true) {
		ctx.fillStyle = color;
		ctx.fill();
	}
	ctx.strokeStyle = color;
	ctx.stroke();
	ctx.closePath();
}

function randomRange(low=0, high=1) {
	var range = high - low;
	return Math.random()*range + low;
}

function draw() {
	ctx.clearRect(0, 0, canvas.width, canvas.height);
	//drawCircle(x, y, 50, color='#0000ff', fill=false);

	var dth = 0.001;
	var dr = 0.01;
	var ang = 0.0;
	var r = 1;

	while (r < 200) {
		ctx.beginPath();
		ctx.arc(x, y, r, ang, ang+dth)
		ctx.strokeStyle = '#0000ff';
		ctx.stroke();
		ctx.closePath();
		ang += dth;
		r += dr;
	}

	/*dx = randomRange(-2, 2);
	dy = randomRange(-2, 2);

	x += dx;
	y += dy;

	if (x + dx < radius || x + dx > canvas.width - radius) {
		dx = -dx;
	}
	if (y + dy < radius || y + dy > canvas.height - radius) {
		dy = -dy;
	}*/
}

function startSimulation(frameInterval=10) {
	var sim = setInterval(draw, frameInterval);
}

//---------------- start -------------//
startSimulation(10);