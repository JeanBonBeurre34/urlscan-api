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


