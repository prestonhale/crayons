SHELL := /bin/bash
.SUFFIXES:


# all configuration outside of the source files is handled using environment
# variables; here we set reasonable development defaults if they are not set
export DJANGO_CONFIGURATION ?= Dev
export DJANGO_SETTINGS_MODULE ?= markers.settings
export BACKEND_PORT ?= 5000
export FRONTEND_PORT ?= 8000

PYTEST_BIN := py.test

.PHONY: devsetup pythondeps checkversions clean runserver tests coveragereport

devsetup: checkversions pythondeps

pythondeps:
	cd markers && pip install -r requirements.txt

checkversions:
	@python --version | grep -q 3.5. || { echo "Need Python 3.5" && exit 1; }

tests:
	cd markers && echo "UNIT TESTS" && $(PYTEST_BIN)  -m "not integration and not endtoend" --ignore=env
	cd markers && echo "INTEGRATION TESTS" && $(PYTEST_BIN)  -m "integration"

endtoendtests:
	@echo "END TO END TESTS" && $(PYTEST_BIN) -m "endtoend"

coveragereport:
	$(PYTEST_BIN) --cov

runserver:
	cd markers && gunicorn -b "0.0.0.0:$(BACKEND_PORT)" --error-logfile - markers.wsgi

devserver:
	cd markers && python manage.py runserver $(BACKEND_PORT)

clean:
	find . -type f -name '*.py[co]' -delete
	find . -name '__pycache__' -type d -exec rm -rf "{}" +
	find . -name '.cache' -type d -exec rm -rf "{}" +
	rm -f .coverage

