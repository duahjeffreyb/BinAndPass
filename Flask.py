from flask import Flask, render_template, url_for
app = Flask(__name__)


@app.route('/')
@app.route('/binary')
def binary():
	return render_template("binary.html")
@app.route('/passwords')
def passwords():
	return render_template("passwords.html")
if __name__ == '__main__':
	app.run()