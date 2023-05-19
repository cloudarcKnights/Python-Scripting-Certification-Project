#!/usr/bin/env python3
from PIL import Image
import os

path = "./supplier-data/images/"
for filename in os.listdir(path):
    if filename.endswith(".tiff"):
        name = os.path.splitext(filename)[0] + ".jpeg"
        image_path = os.path.join(path, filename)
        image = Image.open(image_path).convert("RGB")
        resized_image = image.resize((600, 400))
        save_path = os.path.join(path, name)
        resized_image.save(save_path, "JPEG")
