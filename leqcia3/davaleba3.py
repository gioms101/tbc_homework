from concurrent.futures import ThreadPoolExecutor
import requests
import threading
import json
import os

lock = threading.Lock()

def writing_to_file(page):
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{page}')
    data = response.json()
    with lock:
        if os.path.exists("data.json"):
            with open("data.json", 'a') as f:
                f.write(",\n")
                json.dump(data, f, indent=2)
        else:
            with open("data.json", 'w') as f:
                f.write("[\n")
                json.dump(data, f, indent=2)

with ThreadPoolExecutor() as executor:
    futures = [executor.submit(writing_to_file, i) for i in range(1, 78)]

with open("data.json", 'a') as f:
    f.write("\n]")

