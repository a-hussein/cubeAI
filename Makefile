# Python tooling
UV=uv run

.PHONY: fmt lint test check visual

# Auto-format code (will make changes)
fmt:
	$(UV) ruff format .
	$(UV) black .

# Static checks (won't make changes)
lint:
	$(UV) ruff check .
# 	$(PYTHON) .

# Run test suite
test:
	$(UV) pytest

clean: fmt lint test

visual:
	$(UV) python src/cube/visualizer.py $(a) # args


