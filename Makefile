setup:
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt
clean:
	rm -rf venv
	rm -rf __pycache__
test:
	./venv/bin/pytest
run:
	./venv/bin/python app.py

