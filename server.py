from flask import Flask, render_template, jsonify
from giantswarm import listapps, instancestats

# create webapp and load config
webapp = Flask(__name__)
webapp.config.from_object('config.Base')

# index handler
@webapp.route('/')
def index():
	try:
		return render_template('index.html')
	except Exception as e:
		print "an error occured: %s" % ex

@webapp.route('/org/<org>/env/<env>/app/list')
def applist(org=None, env=None):
	response = listapps(webapp, org, env)
	try:
		return jsonify(response)
	except Exception as ex:
		print "an error occured: %s" % ex

# json stats handler
@webapp.route('/app/<instance>/stats.json')
def stats(instance=None):
	response = instancestats(webapp, instance)
	try:
		return jsonify(response)
	except Exception as ex:
		print "an error occured: %s" % ex

# finally, our entrypoint...
if __name__ == "__main__":
	webapp.run(host="0.0.0.0", debug=False)


