#!/bin/bash

for file in $(find . -type f -name '*.sql'); do
    if ! [[ ("$file") =~ ^V\d+\.\d+\.\d+__[a-zA-Z0-9_]+\.sql$ ]]; then
        echo "Error: Invalid naming convention in $file"
        exit 1
    fi

    # Add additional checks as needed

done

echo "Validation successful"
