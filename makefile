install:
	source venv/bin/activate && pip install -r requirements.txt

run: install
	uvicorn src.api:app --reload