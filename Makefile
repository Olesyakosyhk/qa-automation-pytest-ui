#!make

# Lint...
.PHONY: clean
clean:
	rm -rf `find . -name __pycache__`
	rm -rf `find . -name .pytest_cache`
	rm -rf `find . -name allure_results`
	rm -f `find . -type f -name '*.py[co]' `
	rm -f `find . -type f -name '*~' `
	rm -f `find . -type f -name '.*~' `
	rm -rf dist *.egg-info
	rm -rf .cache
	rm -rf htmlcov
	rm -f .coverage
	rm -f .coverage.*
	rm -rf artefacts/{htmlcov,test_report.xml}

.PHONY: format
format:
	isort .

.PHONY: lint
lint:
	flake8 .