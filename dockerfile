# Use an official Python runtime as a parent image
FROM python:3

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 80

#CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
CMD ["uvicorn", "app:app"]
