window.onload = function () {
	cal = document.getElementById('buttons')

	for(var i=0; i<10; i++) {
		b = document.createElement('button')
		b.id = i.toString()
		b.innerHTML = i.toString()
		b.style.width = '50px';
		b.style.height = '50px';
		b.style.margin = '5px';
		b.value = i;
		b.onclick = call_func;
		cal.appendChild(b)
		console.log(b)
	}
}

function call_func() {
	sc = document.getElementById('screen');

	sc.value += this.value;
}

function inc() {
	sc = document.getElementById('screen');

	v = parseInt(sc.value);

	v += 1;
	sc.value = v;
}