from flask import Flask, render_template, jsonify
from giantswarm import list_apps, get_app_status, instance_stats

# create webapp and load config
webapp = Flask(__name__)
webapp.config.from_object('config.Base')
auth = {
	"token": webapp.config['TOKEN'],
	"server": webapp.config['API_SERVER']
}

# index handler
@webapp.route('/')
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
@webapp.route('/org/<org>/env/<env>/app/list')
def applist(org=None, env=None):

	apps = {'apps': []}

	# get our list of apps with servcies, components, instances
	result = list_apps(auth, org, env)

	if result['response'] == "ok":

		for app in result['apps']:
			# get our list of services for each app
			status = get_app_status(
				auth, 
				org, 
				env, 
				app['name']
			)

			# update the result into a unified view
			apps['apps'].append(
				{
					'name': app['name'],
					'services': status['services']
				}
			)

		return jsonify(apps)
	else:
		# got an error, return an error
		return jsonify(apps), 500

# application stat
@webapp.route('/org/<org>/instance/<instance>/stats')
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


