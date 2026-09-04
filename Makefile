.PHONY: docs index check
docs:
	mkdocs serve -a 0.0.0.0:8000
index:
	python scripts/build_index.py
check:
	python scripts/consistency_check.py
