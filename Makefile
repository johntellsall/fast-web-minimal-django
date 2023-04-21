REVERSE := $(shell tput -Txterm rev)
NORM := $(shell tput -Txterm sgr0)

all:

# SOURCE LAYER ::::::::::::::::::::

check:
	ruff check .
	venv/bin/django-admin check --pythonpath=. --settings=tinyapp

list:
	git ls-files '*.html' '*.py' | grep -v step | wc -l
	wc -l $$(git ls-files '*.html' '*.py' | grep -v step) | tail -n 1

# PYTHON LAYER ::::::::::::::::::::

setup-venv:
	test -d venv || python3 -m venv venv
	venv/bin/pip install -r requirements.txt

# APP LAYER ::::::::::::::::::::

minimal: setup-venv
	venv/bin/django-admin runserver --pythonpath=. --settings=tinyapp

stop:
	kill $$(lsof -t -i:8000)

smoke-test:
	curl -s localhost:8000 | grep -E '(title.*worked|Welcome)'

# PROJECT LAYER ::::::::::::::::::::

watch:
	while sleep 10 ; do date '+$(REVERSE)%X$(NORM)' ; curl --location http://localhost:8000/ ; done

loop-minimal:
	git ls-files | entr -r make minimal

test-minimal: stop
	@echo '$(REVERSE)RUNNING SERVER$(NORM)'
	make minimal &
	sleep 3
	@echo '$(REVERSE)CHECKING SERVER$(NORM)'
	make smoke-test
