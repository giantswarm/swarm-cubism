import requests, json

# list all apps in this org/env
def list_apps(auth, org, env):

	apps = []
	message = "ok"
	headers = {
		'Authorization': 'giantswarm %s' % auth['token']
	}

	try:
		# call the list applications method
		# GET /v1/org/{org}/env/{env}/app/
		url = "https://%s/v1/org/%s/env/%s/app/" % (
			auth['server'],
			org,
			env
		)
		
		# fetch the response
		result = requests.get(url, headers=headers)
		data = json.loads(result.text)['data']

		# .data is the json object holding our app list
		for item in data:
			# .app is the giantswarm app name object
			apps.append({'name': item['app']})
	
	except Exception as ex:
		message = "caught exception calling API: %s" % ex

	# return some json
	return {'apps': apps, 'response': message}

# list all services in this app
def get_app_status(auth, org, env, app):

	services = []
	message = "ok"
	headers = {
		'Authorization': 'giantswarm %s' % auth['token']
	}

	try:
		# call the list applications method
		# GET /v1/org/{org}/env/{env}/app/
		url = "https://%s/v1/org/%s/env/%s/app/%s/status" % (
			auth['server'],
			org,
			env,
			app
		)
		
		# fetch the response
		result = requests.get(url, headers=headers)
		data = json.loads(result.text)['data']

		# pull services
		services = data['services']
	
	except Exception as ex:
		print "caught exception calling API: %s" % ex

	# return some json
	return {'services': services, 'response': "ok"}

# get an instance's stats
def instance_stats(auth, org, instance):

	stats = {}
	message = "ok"
	headers = {
		'Authorization': 'giantswarm %s' % auth['token']
	}

	try:
		# call the instance stats
		# GET /v1/org/{org}/instance/{instance}/stats
		url = "https://%s/v1/org/%s/instance/%s/stats" % (
			auth['server'],
			org,
			instance
		)
		
	
		# fetch the response
		result = requests.get(url, headers=headers)
		data = json.loads(result.text)
		stats = data['data']

	except Exception as ex:
		print "caught exception calling API: %s" % ex

	# return some json
	return {'stats': stats, 'response': "ok"}
