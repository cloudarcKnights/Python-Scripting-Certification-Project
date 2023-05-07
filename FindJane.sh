
!/bin/bash

# create an empty oldFiles.txt file
> oldFiles.txt

# search for all files containing "jane" in list.txt
files=$(grep "jane" ../data/list.txt | cut -d ' ' -f 3)

# loop over each file and check if it exists
for file in $files; do
  if test -e $HOME$file; then
    # if the file exists, append it to oldFiles.txt
    echo $HOME$file >> oldFiles.txt
  fi
done
