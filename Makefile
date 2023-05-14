#!/usr/bin/make

.DEFAULT_GOAL := help

help: ## Show this help
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)
	@echo "\n  Allowed for overriding next properties:\n\n\
	    Usage example:\n\
	        make run"

requirements: ## Install requirements
	python3 -m pip install -r requirements.txt

app-help: ## Help
	python3 ctl/main.py apply --help

say-hello-v1: ## Say hello v1
	python3 -m ctl.main apply -f configs/say-hello-v1.yaml

say-hello-v2: ## Say hello v2
	python3 -m ctl.main apply -f configs/say-hello-v2.yaml

say-hello-v2-spanish: ## Say hello v2 spanish
	python3 -m ctl.main apply -f configs/say-hello-v2-spanish.yaml

say-hello-v2-unsupported: ## Say hello v2 unsupported
	python3 -m ctl.main apply -f configs/say-hello-v2-unsupported.yaml

say-yes: ## Say yes
	python3 -m ctl.main apply -f configs/say-yes.yaml

say-yes2: ## Say yes
	python3 bin/ctl apply -f configs/say-yes.yaml

