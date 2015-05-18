import os

_basedir = os.path.abspath(os.path.dirname(__file__))

# swarm cubism settings
class Base(object):

	API_SERVER = "api.giantswarm.io"
	TOKEN = "%TOKEN%"
	ORG = "%ORG%"
	ENV = "%ENV%"
