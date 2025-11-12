.PHONY: help install install-dev run test format lint clean setup

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-15s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

setup: ## Run the setup script
	./setup.sh

install: ## Install production dependencies
	pip install -r requirements.txt

install-dev: ## Install development dependencies
	pip install -r requirements.txt -r requirements-dev.txt

run: ## Run the application
	python main.py

test: ## Run tests
	pytest

format: ## Format code with black and isort
	black main.py
	isort main.py

lint: ## Run linting checks
	flake8 main.py
	mypy main.py

clean: ## Clean up build artifacts and cache
	rm -rf __pycache__/
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/

venv: ## Create virtual environment
	python3 -m venv .venv
	@echo "Virtual environment created. Activate with: source .venv/bin/activate"

env: ## Copy environment template
	cp .env.example .env
	@echo "Environment file created. Please edit .env with your credentials."