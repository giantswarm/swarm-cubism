# standard info
REGISTRY = registry.giantswarm.io
PROJECT = cubism
USERNAME :=  $(shell swarm user)
TOKEN := $(shell cat ~/.swarm/token)
ORG := $(shell swarm env | cut -d"/" -f1)
ENV := $(shell swarm env | cut -d"/" -f2)
DOMAIN = $(PROJECT)-$(ORG)-$(ENV).gigantic.io

# local development IP
MY_IP = $(shell docker-machine ip docker-vm)
# MY_IP = $(shell boot2docker ip)

test:
	@echo "Please run 'make run' to run locally or 'make up' to deploy."

build:
	docker build -t $(REGISTRY)/$(ORG)/$(PROJECT) .

cache-up:
	-docker stop redis
	-docker rm redis
	docker run --name=redis -d redis

cache-down:
	-docker stop redis
	-docker rm redis

dev: build cache-up
	@echo "##########################################################################"
	@echo "Your service $(PROJECT) will be running at http://$(MY_IP):5000"
	@echo "##########################################################################"

	docker run --rm -ti \
		-e "TOKEN=$(TOKEN)" \
		-e "ORG=$(ORG)" \
		-e "ENV=$(ENV)" \
		-e "PROJECT=$(PROJECT)" \
		-p 5000:5000 \
		--link redis:redis \
		-v `pwd`:/app -w /app $(REGISTRY)/$(ORG)/$(PROJECT)
	
run: build
	@echo "##########################################################################"
	@echo "Your service $(PROJECT) will be running at http://$(MY_IP):5000"
	@echo "##########################################################################"

	docker run --rm -ti \
		-e "TOKEN=$(TOKEN)" \
		-e "ORG=$(ORG)" \
		-e "ENV=$(ENV)" \
		-p 5000:5000 \
		--link redis:redis \
		$(REGISTRY)/$(ORG)/$(PROJECT)
	
push: build
	docker push $(REGISTRY)/$(ORG)/$(PROJECT)

pull:
	docker pull $(REGISTRY)/$(ORG)/$(PROJECT)

up: push
	swarm up \
	  --var=token=$(TOKEN) \
	  --var=domain=$(DOMAIN) \
	  --var=org=$(ORG) \
	  --var=env=$(ENV) \
	  --var=name=$(PROJECT)

	@echo "####################################################"
	@echo "Your service '$(PROJECT)'' is running at http://$(DOMAIN)"
	@echo "####################################################"
