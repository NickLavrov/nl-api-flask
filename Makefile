# Name of the project, used in docker-compose
PROJECT_NAME=nl-api-flask

# Makefile commands
.PHONY: dev tests build-dev

# Run the development environment
dev:
	docker-compose up web_dev

# Run tests
tests:
	docker-compose run --rm web_dev python -m pytest

# Build the development image
build-dev:
	docker-compose build web_dev

