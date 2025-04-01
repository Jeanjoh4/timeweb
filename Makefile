setup:
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt
clean:
	rm -rf venv
	rm -rf __pycache__
test:
	pytest test_app.py
run:
	./venv/bin/python app.py

