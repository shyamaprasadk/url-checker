#!/usr/bin/env python3
import requests
import sys
import time

def check_url(url):
    try:
        start = time.time()
        response = requests.get(url, timeout=5)
        end = time.time()
        print(f"\033[92m[✔] {url}\033[0m - {response.status_code} - {round(end - start, 2)}s")
    except requests.exceptions.RequestException as e:
        print(f"\033[91m[✘] {url}\033[0m - DOWN ({e.__class__.__name__})")

def main():
    if len(sys.argv) < 2:
        print("Usage: url-checker <url1> <url2> ...")
        sys.exit(1)

    urls = sys.argv[1:]
    for url in urls:
        if not url.startswith("http"):
            url = "http://" + url
        check_url(url)

if __name__ == "__main__":
    main()
