# URLScan.io Python Script

## Overview
This Python script provides a command-line interface for scanning URLs using the URLScan.io API. It submits URLs for scanning and retrieves the scan results, handling the polling process until the scan is completed or a timeout is reached.

## Prerequisites
- Python 3.x
- `requests` library (Install using `pip install requests`)
- An API key from URLScan.io

## Setting Up the API Key
Before running the script, set the URLScan.io API key as an environment variable:
- Linux/macOS:
  ```bash
  export URLSCAN_API_KEY=your_api_key_here
```
- windows command prompt
```bash
set URLSCAN_API_KEY=your_api_key_here
```
- windows powershell
```bash
$env:URLSCAN_API_KEY="your_api_key_here"
```
Replace **your_api_key_here** with your actual API key from URLScan.io.

## Installation
First clone the repository locally on your device
```bash
git clone https://github.com/JeanBonBeurre34/urlscan-api
```

## Usage
To use the script, run it from the command line, passing the URL to be scanned as an argument:

```bash
python urlscan-api.py [URL]
```
**[URL]** with the actual URL you want to scan.
The script will submit the URL to URLScan.io for scanning and then periodically poll for the results. Once the scan is complete, the results will be displayed in the console in json format.

## Example
To scan the website https://example.com, run:
```bash
python urlscan-api.py https://example.com
```

## Using Docker
You can also run the script inside a Docker container. This approach ensures that the script runs in a consistent environment.

**Building the Docker Image**

First, build the Docker image from the Dockerfile in your project directory:
```bash
docker build -t urlscan-api .
```
This command builds a Docker image and tags it as **urlscan-api**.


**Running the Docker Container**

To run the script inside a Docker container, use the following command:
```bash
docker run -e URLSCAN_API_KEY=your_api_key -e URLSCAN_URL=[URL] urlscan-api
```
Replace your_api_key_here with your actual URLScan.io API key and [URL] with the URL you want to scan.


**Example**

Simple example to run a container targeting the url https://example.com
```bash
docker run -e URLSCAN_API_KEY=4b223e6f-d523-5445-1028-36750df152a2 -e URLSCAN_URL=https://example.com urlscan-api
```

