import threading
from concurrent.futures.thread import ThreadPoolExecutor

import requests

results =[]


def fetch_data(url:str):
    response = requests.get(url)

    return response.status_code

urls = [
"http://httpbin.io/delay/5",
"http://httpbin.io/delay/2",
"http://httpbin.io/delay/1",
]

with ThreadPoolExecutor(max_workers=5) as executor:
    futures = []

    for url in urls:
        future = executor.submit(fetch_data,url)
        futures.append(future)

    for f in futures:
        results.append(f)

print(results)

print("hello world")