# standard info
REGISTRY = registry.giantswarm.io
PROJECT = cubism
USERNAME :=  $(shell swarm user)
ORG := $(shell swarm env | cut -d"/" -f1)
DOMAIN = cubism-$(USERNAME).gigantic.io
TOKEN := $(shell cat ~/.swarm/token)

# local info
MY_IP = $(shell boot2docker ip)

test:
	@echo "Please run 'make run' to run locally or 'make up' to deploy."

build:
	docker build -t $(REGISTRY)/$(ORG)/$(PROJECT) .

run: build
	@echo "####################################################"
	@echo "Your app is running at http://$(MY_IP):5000"
	@echo "####################################################"

	docker run --rm -ti \
		-e "TOKEN=$(TOKEN)" \
		-p 5000:5000 \
		$(REGISTRY)/$(ORG)/$(PROJECT)
	
push: build
	docker push $(REGISTRY)/$(ORG)/$(PROJECT)

pull:
	docker pull $(REGISTRY)/$(ORG)/$(PROJECT)

up: push
	swarm up \
	  --var=token=$(TOKEN) \
	  --var=domain=$(DOMAIN) \
	  --var=app=$(APP) \
	@echo "####################################################"
	@echo "Your app is running at http://$(domain)"
	@echo "####################################################"