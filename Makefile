.PHONY: build test run

build:
	python -m compileall apps packages scripts

test:
	pytest -q

run:
	uvicorn apps.api.main:app --host 0.0.0.0 --port 8000 --reload
