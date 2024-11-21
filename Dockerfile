FROM python:3.11-slim
ENV PYTHONPATH=/app/backend/services/cards-service/src

WORKDIR /app/services/cards-service/src

COPY requirements.txt /app/
COPY . /app/

RUN pip install --no-cache-dir -r /app/requirements.txt

EXPOSE 2470

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]