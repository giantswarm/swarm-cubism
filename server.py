from flask import Flask, render_template, jsonify
from flask.ext.cache import Cache
from giantswarm import list_services, get_service_status, instance_stats
import json

# create webapp and load config
webapp = Flask(__name__)
webapp.config.from_object('config.Base')
auth = {
	"token": webapp.config['TOKEN'],
	"server": webapp.config['API_SERVER']
}

# redis cache
webapp.cache = Cache(webapp, config={
    "CACHE_TYPE": "redis",
    "CACHE_REDIS_HOST": "redis",
    "CACHE_REDIS_PORT": 6379
})

# index handler
@webapp.route('/')
@webapp.cache.cached(timeout=20)
def index():
	# fetch org and env from config here
	try:
		return render_template(
			'index.html',
			org=webapp.config['ORG'],
			env=webapp.config['ENV']
		)
	except Exception as ex:
		return render_template('error.html', ex=ex)

# APIs paths
# get application list for <org>/<env>
@webapp.route('/org/<org>/env/<env>/service/list')
@webapp.cache.cached(timeout=10)
def servicelist(org=None, env=None):

	services = {'services': []}

	# get our list of apps with servcies, components, instances
	result = list_services(auth, org, env)

	if result['response'] == "ok":

		for service in result['services']:
			# get our list of services for each app
			status = get_service_status(
				auth, 
				org, 
				env, 
				service['name']
			)

			# update the result into a unified view
			services['services'].append(
				{
					'name': service['name'],
					'components': status['components']
				}
			)

		return jsonify(services)
	else:
		# got an error, return an error
		return jsonify(services), 500

# application stat
@webapp.route('/org/<org>/instance/<instance>/stats')
@webapp.cache.cached(timeout=10)
def stats(org=None, instance=None):
	# get an instance's stats
	result = instance_stats(auth, org, instance)

	if result['response'] == "ok":
		return jsonify(result)
	else:
		# got an error, return an error
		return jsonify(result), 500

# entrypoint
if __name__ == "__main__":
	webapp.run(host="0.0.0.0", debug=True)


