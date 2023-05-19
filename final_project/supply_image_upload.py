#!/usr/bin/env python3
import requests
import os

url = "http://localhost/upload/"
image_dir = "./supplier-data/images"
for filename in os.listdir(image_dir):
    if filename.endswith(".jpeg"):
        image_path = os.path.join(image_dir, filename)
        with open(image_path, 'rb') as file:
            response = requests.post(url, files={'file': file})
