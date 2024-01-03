.PHONY: clean system-packages python-packages install tests run all

clean:
	find . -type f -name '*.pyc' -delete
	rm -rf __pycache__

python-packages:
	pip install -r requirements.txt

install: python-packages

run:
	python3 flaskr/app.py

all: clean install run