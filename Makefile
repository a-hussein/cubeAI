# Python tooling
PYTHON=uv run

.PHONY: fmt lint test check

# Auto-format code (will make changes)
fmt:
	$(PYTHON) ruff format .
	$(PYTHON) black .

# Static checks (won't make changes)
lint:
	$(PYTHON) ruff check .
# 	$(PYTHON) .

# Run test suite
test:
	$(PYTHON) pytest

check: fmt lint test