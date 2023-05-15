# Use an official Python runtime as a parent image
FROM python:3

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Establece el puerto de escucha
ENV PORT=8080

# Expone el puerto en el que se ejecuta la aplicación
EXPOSE $PORT

# Establece el comando para ejecutar la aplicación
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "$PORT"]
