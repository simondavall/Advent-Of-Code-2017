.PHONY: test

test: ./Runner/runner.py
	pypy3 ./Runner/runner.py
