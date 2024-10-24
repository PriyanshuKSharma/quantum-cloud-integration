# Use official Python base image
FROM python:3.9-slim

# Set up working directory
WORKDIR /app

# Copy the project files
COPY . /app

# Install Python dependencies
RUN pip install -r requirements.txt

# Install Docker CLI (needed for cloud interaction)
RUN apt-get update && apt-get install -y docker.io

# Set entry point
CMD ["python", "src/quantum_cloud.py"]