#!/bin/bash
set -x

find . -type f -name '*.sql' -exec bash -c '
echo "Checking $file"
    for file do
        if ! [[ "$file" =~ ^[vV]\d+\.\d+\.\d+__[a-zA-Z0-9_]+\.sql$ ]]; then
            echo "Error: Invalid naming convention in $file"
            exit 1
        fi

        # Add additional checks as needed
    done
' bash {} +
echo "Validation successful"



