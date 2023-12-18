# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the script into the container
COPY urlscan-api.py .

# Install any needed packages specified in requirements.txt
# Assuming you have a requirements.txt file with 'requests' listed
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Define environment variable
ENV NAME World

# Run script_name.py when the container launches, URL argument is expected
CMD ["python", "./urlscan-api.py", "url_placeholder"]
