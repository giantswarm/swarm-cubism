import os

_basedir = os.path.abspath(os.path.dirname(__file__))

# swarm cubism settings
class Base(object):

	API_SERVER = "api.giantswarm.io"
	TOKEN = "%TOKEN%"
	ORG = "%ORG%"
	ENV = "%ENV%"

	API_SERVER = "api.giantswarm.io"
	TOKEN = "fcdf2138-6919-453b-af1d-08a0a19a1ecc"
	ORG = "startup"
	ENV = "dev"