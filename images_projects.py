#!/usr/bin/env python3

from PIL import Image
import os

input_folder = 'images/'
output_folder = '/opt/icons/'


for filename in os.listdir(input_folder):
    if filename != ('.DS_Store'):
        image_path = os.path.join(input_folder, filename)
        with Image.open(image_path) as img:
            # Rotate the image 90° clockwise
            rotated_img = img.rotate(-90, expand=True)

            # Resize the image from 192x192 to 128x128
            resized_img = rotated_img.resize((128, 128))

            # Convert the image to JPEG format
            if resized_img.mode != 'RGB':
                resized_img = resized_img.convert('RGB')

            # Save the image to the output folder in .jpeg format
            output_path = os.path.join(output_folder, filename[:-5] + '.jpeg')
            resized_img.save(output_path, 'JPEG')

            print(f'Saved updated image: {output_path}')

