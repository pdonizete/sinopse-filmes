.PHONY: install lint test fmt

VENV ?= .venv
PYTHON := $(VENV)/bin/python
PIP := $(PYTHON) -m pip

install:
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	$(PIP) install pytest ruff pip-audit

lint:
	@if [ -x "$(PYTHON)" ] && $(PYTHON) -m ruff --version >/dev/null 2>&1; then \
		$(PYTHON) -m ruff check .; \
	elif python3 -m ruff --version >/dev/null 2>&1; then \
		python3 -m ruff check .; \
	else \
		python3 -m compileall -q .; \
	fi

test:
	@if [ -x "$(PYTHON)" ] && $(PYTHON) -m pytest --version >/dev/null 2>&1; then \
		$(PYTHON) -m pytest -q; \
	elif python3 -m pytest --version >/dev/null 2>&1; then \
		python3 -m pytest -q; \
	else \
		python3 -m unittest discover -s tests -p 'test_*.py' -q; \
	fi

fmt:
	@if [ -x "$(PYTHON)" ] && $(PYTHON) -m ruff --version >/dev/null 2>&1; then \
		$(PYTHON) -m ruff format .; \
	elif python3 -m ruff --version >/dev/null 2>&1; then \
		python3 -m ruff format .; \
	else \
		echo "ruff not available; skipping format"; \
	fi
