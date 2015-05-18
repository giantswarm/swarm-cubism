from flask import Flask, render_template, jsonify
from giantswarm import listapps, instancestats

# create app and load config
app = Flask(__name__)
app.config.from_object('config.Base')

# index handler
@app.route('/')
def index():
	try:
		return render_template('index.html')
	except Exception as e:
		print "an error occured: %s" % ex

@app.route('/org/<org>/env/<env>/app/list')
def applist(org=None, env=None):
	print "wtf"
	response = listapps(org, env)
	try:
		print "hi"
		return jsonify(response)
	except Exception as ex:
		print "an error occured: %s" % ex

# json stats handler
@app.route('/app/<instance>/stats.json')
def stats(instance=None):
	response = instancestats(instance)
	try:
		return jsonify(response)
	except Exception as ex:
		print "an error occured: %s" % ex

# finally, our entrypoint...
if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=False)


