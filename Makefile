install:
	pip install -r requirements.txt

install-test:
	pip install -r requirements-test.txt

lint:
	pylint --recursive=y wrapper tests service

black:
	black wrapper tests

test:
	python -m unittest discover -s tests