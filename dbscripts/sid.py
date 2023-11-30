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
            schemachange_command = (
                f"schemachange -f {os.path.join(directory, file_name)} -a {os.environ['SF_ACCOUNT']} "
                f"-u {os.environ['SF_USERNAME']} -r {os.path.abspath(directory)} "
                f"-w {os.environ['SF_WAREHOUSE']} -d {os.environ['SF_DATABASE']} "
                f"-c {os.environ['SF_DATABASE']}.SCHEMACHANGE.CHANGE_HISTORY --create-change-history-table"
            )
            subprocess.run(schemachange_command, shell=True, check=True)
            
        else:
            print(f"File '{file_name}' does not match the pattern. Skipping schemachange.")
            continue
