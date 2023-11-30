import os
import re
import subprocess
directory = "dbscripts/"
pattern = r"^[vV]\d+\.\d+\.\d+__[a-zA-Z0-9_]+\.sql$"
for entry in os.scandir(directory):
    if entry.is_file():
        file_name = entry.name
        print(file_name)
        if re.match(pattern, file_name):
            print(f"File '{file_name}' matches the pattern. Proceeding with schemachange.")
            print("Running schemachange")
schemachange_command = [
    'schemachange',
    '-f', f'{github_workspace}/dbscripts',
    '-a', sf_account,
    '-u', sf_username,
    '-r', sf_role,
    '-w', sf_warehouse,
    '-d', sf_database,
    '-c', f'{sf_database}.SCHEMACHANGE.CHANGE_HISTORY',
    '--create-change-history-table'
]
    subprocess.run(schemachange_command, check=True, shell=True)
            
        else:
            print(f"File '{file_name}' does not match the pattern. Skipping schemachange.")
            continue
