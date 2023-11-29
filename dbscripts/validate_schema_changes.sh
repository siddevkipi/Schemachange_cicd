#!/bin/bash

directory="dbscripts/"
pattern="^[vV]\d+\.\d+\.\d+__[a-zA-Z0-9_]+\.sql$"

# Use find to get a list of files in the directory
find "$directory" -type f | while read -r file; do
    # Extract the file name from the full path
    file_name=$(basename "$file")
	echo "$file_name"

    # Check if the file name matches the pattern
    if [[ $file_name =~ $pattern ]]; then
        echo "File '$file_name' matches the pattern."
    else
        echo "File '$file_name' does not match the pattern."
    fi
done



