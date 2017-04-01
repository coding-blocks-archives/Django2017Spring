from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html', nums=range(10), msg='This is a message! From Server!')


if __name__ == '__main__':
	pass