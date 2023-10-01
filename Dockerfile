# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app

# Install the required packages using the requirements file
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app into the container at /app
COPY . /app

# Define the environment variable
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expose port 5000 for the Flask app to listen on
EXPOSE 5000

# Run app.py when the container launches
CMD ["flask", "run"]

