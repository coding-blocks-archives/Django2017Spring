var canvas = document.getElementById('space');
var ctx = canvas.getContext('2d');

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