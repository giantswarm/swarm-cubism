from flask import Flask, render_template

app = Flask(__name__)

# we'll create a few routes now...
@app.route('/')
@app.route('/hello/')
@app.route('/hello/<name>')

# now the main function...
def hello(name=None):
	try:
		return render_template('index.html', name=name)
	except Exception as e:
		print "an error occured: %s" % e

# finally, our entrypoint...
if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=False)


