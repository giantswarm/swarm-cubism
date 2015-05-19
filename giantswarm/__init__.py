
import requests, json

# authorization token
headers = {'Authorization': 'giantswarm %s' % app.config['TOKEN']}
	
# list all apps in this org/env
def list_apps(webapp, org, env):

	apps = []

	try:
		# call the list applications method
		# GET /v1/org/{org}/env/{env}/app/
		url = "https://%s/v1/org/%s/env/%s/app/" % (
			webapp.config['API_SERVER'],
			org,
			env
		)
		
		# fetch the response
		response = requests.get(url, headers=headers)
		data = json.loads(response.text)

		# .data is the json object holding our app list
		for item in data['data']:
			# .app is the giantswarm app name object
			apps.append(item['app'])
	
	except Exception as ex:
		print "caught exception calling API: %s" % ex

	# return some json
	return {'apps': apps, 'response': "ok"}

# list all services in this app
def list_services(webapp, app):

	services = []

	try:
		pass
	except:
		pass
		
# list all instances in this service
def list_instances(webapp, service):

	instances = []

	try:
		# call the list applications method
		# GET /v1/org/{org}/env/{env}/app/
		url = "https://%s/v1/org/%s/env/%s/app/" % (
			webapp.config['API_SERVER'],
			org,
			env
		)
		
		# fetch the response
		response = requests.get(url, headers=headers)
		data = json.loads(response.text)

		# .data is the json object holding our app list
		for item in data['data']:
			# .app is the giantswarm app name object
			apps.append(item['app'])
	
	except Exception as ex:
		print "caught exception calling API: %s" % ex

	# return some json
	return {'apps': apps, 'response': "ok"}