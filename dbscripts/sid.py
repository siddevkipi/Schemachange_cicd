import os
import re

directory = "dbscripts/"
pattern = r"^[vV]\d+\.\d+\.\d+__[a-zA-Z0-9_]+\.sql$"

# Use os.scandir to get a list of files in the directory
for entry in os.scandir(directory):
    if entry.is_file():
        # Extract the file name from the full path
        file_name = entry.name
        print(file_name)
        print(pattern)

        # Check if the file name matches the pattern
        if re.match(pattern, file_name):
            print(f"File '{file_name}' matches the pattern.")
        else:
            print(f"File '{file_name}' does not match the pattern.")
