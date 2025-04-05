# Makefile

.PHONY: format lint typecheck all

format:
	poetry run black .
	poetry run ruff format .

lint:
	poetry run ruff check . --fix

typecheck:
	poetry run mypy gemini25/

all: format lint typecheck
