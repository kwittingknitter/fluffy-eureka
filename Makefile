install:
	pip install -r requirements.txt

lint:
	pylint --recursive=y wrapper tests

black:
	black wrapper tests

test:
	python -m unittest discover -s tests