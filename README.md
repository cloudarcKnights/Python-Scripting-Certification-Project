# A collection of Python Scripts I wrote for the Google Automation certificate: [link](https://github.com/cloudarcKnights/Python-Scripting-Certification-Project/tree/master/final_project)

# Project 1: Image Conversion Script

This script is used to convert TIFF images to JPEG format in a specified directory.

## Usage

1. Place the script file (`convert_images.py`) in the desired directory.
2. Create a subdirectory named `supplier-data` in the same directory.
3. Inside the `supplier-data` directory, create an `images` subdirectory and place the TIFF images to be converted inside it.
4. Open a terminal or command prompt and navigate to the directory containing the script.
5. Run the following command to execute the script:
6. The script will search for TIFF images in the `./supplier-data/images/` directory and convert them to JPEG format.
7. The converted JPEG images will be saved with the same filename but with the extension changed to `.jpeg` in the same directory.

# Project 2: Image Conversion Script

# Email Sender

This script provides a simple interface to send emails with attachments using the SMTP protocol.

## Usage

1. Ensure that you have the necessary email server settings configured. By default, the script assumes that the email server is running on `localhost`. If you are using a different email server, update the `mail_server` variable in the `send()` method accordingly.

2. Import the script into your Python project:
3. Create an email message using the `Email` class constructor:

   ```python
   email = Email(sender, recipient, subject, body)
   ```

   - `sender`: Email address of the sender.
   - `recipient`: Email address of the recipient.
   - `subject`: Subject of the email.
   - `body`: Content of the email.

4. Add an attachment (optional) using the `add_attachment()` method:

   ```python
   email.add_attachment(attachment_path)
   ```

   - `attachment_path`: Path to the file to be attached.

5. Send the email using the `send()` method:

   ```python
   email.send()
   ```

