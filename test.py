name = 'manny'
number = len(name) * 3
print("hello {}, your lucky number is {}".format(name, number))

animals = ["lion", "Zebra", "Dolphin", "Monkey"]
chars = 0
for animal in animals:
    chars += len(animal)
    print(chars)

print("Total characters: {}, Average length: {}".format(chars, chars/len(animals)))

winners = ["ashley", "kylan", "Reese"]
for index, person in enumerate(winners):

    print("{} - {}".format(index + 1, person))

def full_emails(people):
    result = []
    for email, name in people:
        result.("{} <{}>".format(name, email))
    return result
print(full_emails([("alex@example.com", "Alex Diego"), ("shay@example.com", "Shay Brandt")]))

multiples = []
for x in range(1,11):
    multiples.append(x*7)
     
print(multiples)

multiples = [x*7 for x in range(1,11)]
print(multiples)

languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
lengths = [len(language) for language in languages]
print(lengths)


z = [x for x in range(0, 101) if x % 3 == 0]
print(z)def odd_numbers(n):


def odd_numbers(n):
    return [x for x in range(1, n+1) if x % 2 != 0]

def list_elements(list_name, elements):

    return "The " + list_name + " list includes: " + ", ".join(elements)

print(list_elements("Printers", ["Color Printer", "Black and White Printer", "3-D Printer"]))

file_counts = {"jpg": 10, "txt": 14, "csv":2, "py":23}
"txt" in file_counts
file_counts["zebras"] = 2
del file_counts["zebras"]
print(file_counts)

file_counts = {"jpg": 10, "txt": 14, "csv":2, "py":23}
for ext, amount in file_counts.items():

    print("There are {} files with the .{} extension".format(amount,ext))
    file_counts.keys()

def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result

print(count_letters("aaaaa"))
print(count_letters("tenant"))

def sum_server_use_time(Server):
    total_use_time = 0.0
    for key, value in Server.items():
        total_use_time += Server[key]

    return round(total_use_time, 2)

FileServer = {"EndUser1": 2.254, "EndUser2": 4.52, "EndUser3": 13, "EndUser4": 3.75, "EndUser5": 0.6, "EndUser6": 8}
print(sum_server_use_time(FileServer))

def setup_guests(guest_list):
    # loop over the guest list and add each guest to the dictionary with
    # an initial value of 0
    result = guest_list.copy() # Initialize a new dictionary 
    for guest, people in result.items():  # Iterate over the elements in the list 
        result[people] = 0 # Add each list element to the dictionary as a key with 
            # the starting value of 0
    return result


print(help("str"))


import os

def create_python_script(filename):
  comments = "# Start of a new Python program"
  with open("program.py", "a") as file:
    file.write(comments)
  filesize = os.path.getsize("program.py")
  return(filesize)

print(create_python_script("program.py"))

import os

def new_directory(directory, filename):
  # Before creating a new directory, check to see if it already exists
  if os.path.isdir(directory) == False:
    os.mkdir(directory)

  # Create the new file inside of the new directory
  os.chdir(filename)
  with open (filename, "w") as file:
    pass

  # Return the list of files in the new directory
  return os.listdir()

print(new_directory("PythonPrograms", "script.py"))


import os
import datetime

def file_date(filename):
  # Create the file in the current directory
  with open(filename, "a") as file:
    timestamp = os.path.getmtime(filename)
    date = datetime.datetime.fromtimestamp(timestamp) 
  # Convert the timestamp into a readable format, then into a string
    date_string = str(date)
  # Return just the date portion 
  # Hint: how many characters are in “yyyy-mm-dd”? 
  return ("{}".format(date_string[0:10]))

print(file_date("newfile.txt")) 
# Should be today's date in the format of yyyy-mm-dd

import os

def parent_directory():
  # Create a relative path to the parent of the current working directory 
  relative_parent = os.path.join(os.getcwd(), os.pardir)

  # Return the absolute path of the parent directory
  return os.path.abspath(relative_parent)

print(parent_directory())

import csv

users = [{"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"},
    {"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"},
    {"name": "Charlie Grey", "username": "greyc", "department": "Development"}]
keys = ["name", "username", "department"]

with open('by_department.csv','w') as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)

import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  with open(filename, 'r') as file:
    # Read the rows of the file into a dictionary
    reader = csv.DictReader(file)
    # Process each item of the dictionary
    for row in reader:
      return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
  return return_string


#Call the function
print(contents_of_file("flowers.csv"))


import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  with open(filename, 'r') as file:
    # Read the rows of the file
    rows = csv.reader(file)
    # Process each row
    for row in rows:
      name, color, types = row
      # Format the return string for data rows only

      return_string += "a {} {} is {}\n".format(name, color, types)
  return return_string

#Call the function
print(contents_of_file("flowers.csv"))


import re
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
# index = log.index("[")
# print(log[index+1:index+6])

regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])

GREP in TERMINAL
grep thon /usr/share/dict/words
(-i match regardless of case) grep -i python /usr/share/dict/words
(. means any character) grep l.rts /usr/share/dict/words
(^ means starts with) grep ^fruit /usr/share/dict/words
($ means ends with) grep cat$ /usr/share/dict/words 

!/usr/bin/env python3

Import libraries
import csv
import re  

def contains_domain(address, domain):
  domain_pattern = r'[\w\.-]+@'+domain+'$'
  if re.match(domain_pattern, address):
    return True 
  return False

def replace_domain(address, old_domain, new_domain):
  old_domain_pattern = r'' + old_domain + '$'
  address = re.sub(old_domain_pattern, new_domain, address)
  return address

def main():
  """Processes the list of emails, replacing any instances of the
    old domain with the new domain."""

main(old_domain, new_domain = 'abc.edu', 'xyz.edu')

!/usr/bin/env python3
import re
import sys

logfile = sys.argv[1]
with open(logfile) as f:
    for line in f:
        if "loginwindow" not in line:
            continue
        pattern = r"USER \((\w+)\)$"
        result = re.search(pattern, line)

        print(result[1])

import re
def show_time_of_pid(line):
  pattern = r"^[(\w+:)][\d*]$"
  result = re.search(pattern, line)
  return result

