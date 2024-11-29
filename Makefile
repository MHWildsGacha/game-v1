SHELL := /bin/bash

install:
	source bin/activate && pip install -r requirements.txt

run: install
	uvicorn backend.services.cards-service.src.api:app --reload
