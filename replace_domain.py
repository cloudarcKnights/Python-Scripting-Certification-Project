#!/usr/bin/env python3 
import csv
import re

def contains_domain(address, domain):
  """Returns True if the email address contains the given domain,
  in either the domain or subdomain."""
  domain_pattern = r'[\w\.-]+@'+ domain +'$'
  if re.match(domain_pattern, address):
    return True
  return False

def replace_domain(address, old_domain, new_domain):
  """Replaces the old domain with the new domain in the
  provided email address."""
  old_domain_pattern = r'' + old_domain + '$'
  address = re.sub(old_domain_pattern, new_domain, address)
  return address

def main():
  # Declare old and new domains
  old_domain, new_domain = 'abc.edu', 'xyz.edu'

  # Declare file paths
  csv_file_location = '/home/<username>/data/user_emails.csv'
  report_file = '/home/<username>/data/updated_user_emails.csv'

  # Initialize lists to store email addresses
  user_email_list = []
  old_domain_email_list = []
  new_domain_email_list = []

  # Read data from CSV file and store email addresses in a list
  with open(csv_file_location, 'r') as f:
    user_data_list = list(csv.reader(f))
    user_email_list = [data[1].strip() for data in user_data_list[1:]]

  # Find email addresses with old domain and replace with new domain
  for email_address in user_email_list:
    if contains_domain(email_address, old_domain):
      old_domain_email_list.append(email_address)
      replaced_email = replace_domain(email_address, old_domain, new_domain)
      new_domain_email_list.append(replaced_email)

  # Update the email addresses in the user_data_list
  email_key = ' ' + 'Email Address'
  email_index = user_data_list[0].index(email_key)
  for user in user_data_list[1:]:
    for old_domain, new_domain in zip(old_domain_email_list, new_domain_email_list):
      if user[email_index] == ' ' + old_domain:
        user[email_index] = ' ' + new_domain

  # Write the updated user_data_list to a new CSV file
  with open(report_file, 'w') as output_file:
    writer = csv.writer(output_file)
    writer.writerows(user_data_list)

if __name__ == '__main__':
  main()
