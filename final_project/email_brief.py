#!/usr/bin/env python3
import email.message
import mimetypes
import os.path
import smtplib

class Email:
    def __init__(self, sender, recipient, subject, body):
        self.message = email.message.EmailMessage()
        self.message["From"] = sender
        self.message["To"] = recipient
        self.message["Subject"] = subject
        self.message.set_content(body)

    def add_attachment(self, attachment_path):
        attachment_filename = os.path.basename(attachment_path)
        mime_type, _ = mimetypes.guess_type(attachment_path)
        mime_type, mime_subtype = mime_type.split('/', 1)

        with open(attachment_path, 'rb') as ap:
            self.message.add_attachment(ap.read(),
                                        maintype=mime_type,
                                        subtype=mime_subtype,
                                        filename=attachment_filename)

    def send(self):
        mail_server = smtplib.SMTP('localhost')
        mail_server.send_message(self.message)
        mail_server.quit()

def generate_email(sender, recipient, subject, body, attachment_path=None):
    email_obj = Email(sender, recipient, subject, body)
    if attachment_path:
        email_obj.add_attachment(attachment_path)
    return email_obj

def generate_error_email(sender, recipient, subject, body):
    return Email(sender, recipient, subject, body)

def send_email(message):
    message.send()
