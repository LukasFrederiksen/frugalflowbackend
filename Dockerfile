# Use the official Python base image
FROM python:latest

LABEL Name="FrugalFlow Rest" Version=1.4.2
LABEL org.opencontainers.image.source="https://123.com"

# Set the container's working directory to /app
WORKDIR /app

# Copy the entire project directory into the container
COPY . /app/

# Copy the requirements.txt file to the container
COPY requirements.txt /app/

# Install the project dependencies
RUN pip install -r requirements.txt

# Expose the port that the Django development server will run on
EXPOSE 8000

# Run the Django development server when the container starts
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]