#!/usr/bin/env python3

import os
import requests

# Get the list of .txt files in the /data/feedback directory
feedback_dir = '/data/feedback'
feedback_files = os.listdir(feedback_dir)
feedback_files = [file for file in feedback_files if file.endswith('.txt')]

# Process each feedback file and upload the contents as a dictionary
for file in feedback_files:
    feedback_path = os.path.join(feedback_dir, file)
    with open(feedback_path, 'r') as f:
        lines = f.readlines()
        feedback = {
            'title': lines[0].strip(),
            'name': lines[1].strip(),
            'date': lines[2].strip(),
            'feedback': lines[3].strip()
        }

        # Set host URL
        url = "http://localhost/feedback/"

        # Post feedback entries
        response = requests.post(url, data=feedback)
        if response.ok:
            print("Loaded entry")
        else:
            print(f"Load entry error: {response.status_code}")