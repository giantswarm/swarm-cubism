# standard info
PROJECT = app
REGISTRY = registry.giantswarm.io
USERNAME :=  $(shell swarm user)
ORG := $(shell swarm env | cut -d"/" -f1)
DOMAIN = cubism-$(USERNAME).gigantic.io
TOKEN := $(shell cat ~/.swarm/token)

# local info
MY_IP = $(shell boot2docker ip)

test:
	echo $(TOKEN)

docker-build:
	docker build -t $(REGISTRY)/$(ORG)/$(PROJECT) .

docker-run: docker-build
	@echo "Your app is running at http://$(MY_IP):5000"
	docker run --rm -ti \
		-e "TOKEN=$(TOKEN)" \
		-p 5000:5000 \
		$(REGISTRY)/$(ORG)/$(PROJECT)

docker-push: docker-build
	docker push $(REGISTRY)/$(ORG)/$(PROJECT)

docker-pull:
	docker pull $(REGISTRY)/$(ORG)/$(PROJECT)

swarm-up: docker-push
	swarm up \
	  --var=token=$(TOKEN) \
	  --var=domain=$(DOMAIN)
	@echo "Your app is running at http://$(domain)"
