import requests, json

# list all services in this org/env
def list_services(auth, org, env):

	services = []
	message = "ok"
	headers = {
		'Authorization': 'giantswarm %s' % auth['token']
	}

	try:
		# call the list applications method
		# GET /v1/org/{org}/env/{env}/service/
		url = "https://%s/v1/org/%s/env/%s/service/" % (
			auth['server'],
			org,
			env
		)

		# fetch the response
		result = requests.get(url, headers=headers)
		data = json.loads(result.text)['data']

		# .data is the json object holding our app list
		for item in data:
			# .service is the giantswarm service name object
			services.append({'name': item['service']})

	except Exception as ex:
		message = "caught exception calling API: %s" % ex

	# return some json
	return {'services': services, 'response': message}

# list all services in this app
def get_service_status(auth, org, env, service):

	components = []
	message = "ok"
	headers = {
		'Authorization': 'giantswarm %s' % auth['token']
	}

	try:
		# call the list applications method
		# GET /v1/org/{org}/env/{env}/app/
		url = "https://%s/v1/org/%s/env/%s/service/%s/status" % (
			auth['server'],
			org,
			env,
			service
		)

		# fetch the response
		result = requests.get(
			url,
			headers=headers
		)
	
		data = json.loads(result.text)['data']

		# pull services
		components = data['components']
	
	except Exception as ex:
		print "caught exception calling API: %s" % ex

	# return some json
	return {'components': components, 'response': "ok"}

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
