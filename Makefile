PYTHON = python3
SCRIPT = test.py

.PHONY: run lint env clean install

env:
    export OPENAI_API_KEY=your_secret_key; command

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
