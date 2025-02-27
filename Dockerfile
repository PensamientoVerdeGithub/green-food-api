# Use a lightweight Python base image
FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y ghostscript

# Set the working directory in the container
WORKDIR /app

# Copy the project files into the container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the application port
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "app.py"]
