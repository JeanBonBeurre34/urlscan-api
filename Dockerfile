# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the script and requirements file into the container
COPY urlscan-api.py .
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run script_name.py when the container launches
CMD ["python", "./urlscan-api.py"]
