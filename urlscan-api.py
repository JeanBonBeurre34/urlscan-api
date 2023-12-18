import requests
import time
import argparse

def scan_url(api_key, url):
    headers = {
        'API-Key': api_key,
        'Content-Type': 'application/json'
    }
    data = {
        'url': url,
        'public': 'on'
    }
    response = requests.post('https://urlscan.io/api/v1/scan/', headers=headers, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error scanning URL: {response.status_code}")

def get_scan_result(api_key, uuid, max_wait_time=300):
    headers = {
        'API-Key': api_key
    }
    start_time = time.time()
    while time.time() - start_time < max_wait_time:
        response = requests.get(f'https://urlscan.io/api/v1/result/{uuid}/', headers=headers)
        if response.status_code == 200:
            return response.json()
        elif response.status_code != 404:
            raise Exception(f"Error getting scan result: {response.status_code}")
        time.sleep(5)  # Polling interval
    raise TimeoutError("Maximum wait time for scan result exceeded.")

def main():
    parser = argparse.ArgumentParser(description='Scan a URL using URLScan.io API')
    parser.add_argument('url', help='The URL to scan')
    args = parser.parse_args()

    # Replace 'your_api_key_here' with your actual API key
    api_key = 'your_api_key_here'
    url_to_scan = args.url

    # Scan a URL
    scan_response = scan_url(api_key, url_to_scan)
    uuid = scan_response['uuid']
    print(f"Scan submitted. UUID: {uuid}")

    # Initially wait for 10-30 seconds
    time.sleep(20)  # You can adjust this initial wait time

    # Retrieve the scan result with polling
    try:
        result = get_scan_result(api_key, uuid)
        print(result)
    except TimeoutError as e:
        print(str(e))

if __name__ == '__main__':
    main()
