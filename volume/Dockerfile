FROM python:3.9-slim

WORKDIR /app

# Copy the Python script to the container
COPY app.py /app/

# Install necessary packages
#RUN pip install --no-cache-dir logging
RUN mkdir -p /logs 
# Define the command to run the application
CMD ["python", "app.py"]