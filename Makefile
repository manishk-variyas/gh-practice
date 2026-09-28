APP := app/main.py
HOST := 0.0.0.0
PORT := 8000

.PHONY: help install dev run stop test lint format clean

help: ## Show available commands
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-10s %s\n", $$1, $$2}'

install: ## Install dependencies with uv
	uv sync

dev: stop ## Start dev server with reload (http://localhost:8000)
	@uv run fastapi dev $(APP) --host $(HOST) --port $(PORT) || true

run: stop ## Start prod server (http://localhost:8000)
	@uv run fastapi run $(APP) --host $(HOST) --port $(PORT) || true

stop: ## Kill whatever is listening on $(PORT)
	-@lsof -ti :$(PORT) | xargs kill -9 2>/dev/null || true

test: ## Run tests
	uv run pytest -q

lint: ## Lint with ruff
	uvx ruff check .

format: ## Format with ruff
	uvx ruff format .

clean: ## Remove caches and venv
	rm -rf .pytest_cache .ruff_cache __pycache__ app/__pycache__ tests/__pycache__ .venv
