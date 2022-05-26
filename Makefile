# enable BASH-specific features
SHELL := /bin/bash

SOURCE_DIR := $(shell pwd)
REMOTE_DIR := /home/david/Documents/code/chengjied/leetcode-py

.PHONY: test
test:
	@echo "Run unit tests"
	@tox

.PHONY: sync
sync:
	@for local_dir in tests leetcode; do \
		rsync -auz ${SOURCE_DIR}/$$local_dir debian:${REMOTE_DIR}/; \
		done

.PHONY: clean
clean:
	@echo "Clean temp files"
	@rm -rf htmlcov/
	@find . -type d -path ./.tox -prune -false -o -name '__pycache__' -print0 | xargs -0 rm -rf
