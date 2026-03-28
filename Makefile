.PHONY: build test run

build:
	python -m compileall apps packages scripts

test:
	pytest -q

run:
	uvicorn apps.api.main:app --host 0.0.0.0 --port ${PORT:-8080} --reload
