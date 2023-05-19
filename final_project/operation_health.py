#!/usr/bin/env python3
import shutil
import psutil
import socket
import emails
import os

def check_disk_usage(sender, receiver, body):
    du = shutil.disk_usage("/")
    du_percent = du.free / du.total * 100
    if du_percent < 20:
        subject = "Error - Available disk space is less than 20%"
        message = emails.generate_error_email(sender, receiver, subject, body)
        emails.send_email(message)

def check_cpu_usage(sender, receiver, body):
    cpu_percent = psutil.cpu_percent(1)
    if cpu_percent > 80:
        subject = "Error - CPU usage is over 80%"
        message = emails.generate_error_email(sender, receiver, subject, body)
        emails.send_email(message)

def check_memory_availability(sender, receiver, body):
    mem = psutil.virtual_memory()
    threshold = 500 * 1024 * 1024  # 500MB
    if mem.available < threshold:
        subject = "Error - Available memory is less than 500MB"
        message = emails.generate_error_email(sender, receiver, subject, body)
        emails.send_email(message)

def check_hostname_resolution(sender, receiver, body):
    hostname = socket.gethostbyname('localhost')
    if hostname != '127.0.0.1':
        subject = "Error - localhost cannot be resolved to 127.0.0.1"
        message = emails.generate_error_email(sender, receiver, subject, body)
        emails.send_email(message)

if __name__ == "__main__":
    sender = "automation@example.com"
    receiver = "<USERNAME>@example.com".format(os.environ.get('USER'))
    body = "Please check your system and resolve the issue as soon as possible."

    check_disk_usage(sender, receiver, body)
    check_cpu_usage(sender, receiver, body)
    check_memory_availability(sender, receiver, body)
    check_hostname_resolution(sender, receiver, body)
