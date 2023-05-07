#!/usr/bin/env python3

import re
import csv

error = {}
per_user = {}

# Open and read syslog.log file
with open("syslog.log") as file:
    for line in file:
        # Extracting username from the log
        username = re.search(r"\((.*)\)", line).group(1)
        # Extracting log type (ERROR/INFO)
        log_type = re.search(r"(ERROR|INFO)", line).group(1)
        # Counting errors
        if log_type == "ERROR":
            error_msg = re.search(r"ERROR (.*) ", line).group(1)
            if error_msg not in error.keys():
                error[error_msg] = 0
            error[error_msg] += 1
        # Counting number of logs per user
        if username not in per_user.keys():
            per_user[username] = {"INFO": 0, "ERROR": 0}
        per_user[username][log_type] += 1

# Sorting dictionaries
error_sorted = sorted(error.items(), key=lambda x: x[1], reverse=True)
per_user_sorted = sorted(per_user.items())

# Inserting column names
error_sorted.insert(0, ("Error", "Count"))
per_user_sorted.insert(0, ("Username", "INFO", "ERROR"))

# Writing data to csv files
with open("error_message.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerows(error_sorted)
with open("user_statistics.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerows(per_user_sorted)
