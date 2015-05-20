# standard info
REGISTRY = registry.giantswarm.io
PROJECT = cubism
USERNAME :=  $(shell swarm user)
ORG := $(shell swarm env | cut -d"/" -f1)
ENV := $(shell swarm env | cut -d"/" -f2)
DOMAIN = cubism-$(ORG)-$(ENV).gigantic.io
TOKEN := $(shell cat ~/.swarm/token)

# local info
MY_IP = $(shell boot2docker ip)

test:
	@echo "Please run 'make run' to run locally or 'make up' to deploy."

build:
	docker build -t $(REGISTRY)/$(ORG)/$(PROJECT) .

dev: build 
	docker run --rm -ti \
		-e "TOKEN=$(TOKEN)" \
		-e "ORG=$(ORG)" \
		-e "ENV=$(ENV)" \
		-e "PROJECT=$(PROJECT)" \
		-p 5000:5000 \
		-v `pwd`:/$(PROJECT) -w /$(PROJECT) $(REGISTRY)/$(ORG)/$(PROJECT)
	
run: build
	@echo "####################################################"
	@echo "Your app $(APP) is running at http://$(MY_IP):5000"
	@echo "####################################################"

	docker run --rm -ti \
		-e "TOKEN=$(TOKEN)" \
		-e "ORG=$(ORG)" \
		-e "ENV=$(ENV)" \
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
	  --var=org=$(ORG) \
	  --var=env=$(ENV) \
	  --var=app=$(APP) \
	@echo "####################################################"
	@echo "Your app $(APP) is running at http://$(domain)"
	@echo "####################################################"
