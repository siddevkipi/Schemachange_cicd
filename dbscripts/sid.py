import os
import subprocess

directory = "dbscripts/"
pattern = r"^[vV]\d+\.\d+\.\d+__[a-zA-Z0-9_]+\.sql$"

for entry in os.scandir(directory):
    if entry.is_file() and entry.name.endswith(".sql"):
        file_name = entry.name
        print(f"Processing file: {file_name}")

        # Change the current working directory to the scripts directory
        os.chdir(directory)

        # Specify the file as the root folder in the command
        schemachange_command = (
            f"schemachange -f {file_name} -a {os.environ['SF_ACCOUNT']} "
            f"-u {os.environ['SF_USERNAME']} -r . "  # Use '.' to represent the current directory as root
            f"-w {os.environ['SF_WAREHOUSE']} -d {os.environ['SF_DATABASE']} "
            f"-c {os.environ['SF_DATABASE']}.SCHEMACHANGE.CHANGE_HISTORY --create-change-history-table"
        )

        try:
            subprocess.run(schemachange_command, shell=True, check=True)
            print(f"Schemachange completed for file: {file_name}")
        except subprocess.CalledProcessError as e:
            print(f"Error running schemachange for file '{file_name}'. Return code: {e.returncode}")
            print(e)

        # Change back to the original working directory
        os.chdir('..')
