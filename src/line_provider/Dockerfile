FROM python:3.10
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY ./src/line_provider /src/line_provider
CMD ["uvicorn", "src.line_provider.main:app", "--host", "0.0.0.0", "--port", "8080"]