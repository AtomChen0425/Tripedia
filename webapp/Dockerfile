
FROM python:3.11-slim-bullseye

WORKDIR /app


COPY . /app


RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt


EXPOSE 6666


CMD ["python", "app.py"]