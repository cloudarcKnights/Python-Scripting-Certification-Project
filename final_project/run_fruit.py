#!/usr/bin/env python3
import os
import requests

fruits = {}
keys = ["name", "weight", "description", "image_name"]
path = "./supplier-data/descriptions/"
img_path = "./supplier-data/images/"

for file in os.listdir(path):
    with open(os.path.join(path, file)) as f:
        index = 0
        for ln in f:
            line = ln.strip()
            if "lbs" in line:
                nline = line.split()
                wght = int(nline[0])
                fruits["weight"] = wght
                index += 1
            else:
                try:
                    fruits[keys[index]] = line
                    index += 1
                except IndexError:
                    fruits[keys[2]] = line

        split_f = file.split(".")
        name = split_f[0] + ".jpeg"
        for fle in os.listdir(img_path):
            if fle == name:
                fruits["image_name"] = name

        response = requests.post("http://<External_IP>/fruits/", json=fruits)
        fruits.clear()
