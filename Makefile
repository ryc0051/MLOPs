PYTHON = python3
SCRIPT = test.py

.PHONY: run lint env clean

install:
	$(PYTHON) -m venv env && \
	. env/bin/activate && \
	pip install -r requirements.txt
run:
	env/bin/$(PYTHON) $(SCRIPT)
lint:
	env/bin/$(PYTHON) -m pylint $(SCRIPT)
clean:
	rm -rf env
