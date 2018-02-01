SOURCE := main.py
PYTHON := python

run:
	$(PYTHON) $(SOURCE)

clean:
	rm -rf images/

.PHONY: clean run
