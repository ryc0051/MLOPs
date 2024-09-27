PYTHON = python3
SCRIPT = test.py

.PHONY: run lint env clean install

install:
	$(PYTHON) -m venv env && \
	. env/bin/activate && \
	pip install -r requirements.txt
run:
    OPENAI_API_KEY=$(OPENAI_API_KEY) env/bin/$(PYTHON) $(SCRIPT)
lint:
	env/bin/$(PYTHON) -m pylint $(SCRIPT)
clean:
	rm -rf env
