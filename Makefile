PYTHON = python3
SCRIPT = test.py

.PHONY: run lint env clean

env:
	$(PYTHON) -m venv env
	. env/bin/activate && pip install -r requirements.txt

run:
	$(PYTHON) $(SCRIPT)
lint:
	$(PYTHON) -m pylint $(SCRIPT)
clean:
	rm -rf env
