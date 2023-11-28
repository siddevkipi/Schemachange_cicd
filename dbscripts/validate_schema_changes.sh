#!/bin/bash

for file in $(find dbscripts/ -type f -name '*.sql'); do
    echo "Checking $file"
    if ! [[ $(basename "$file") =~ ^[vV]\d+\.\d+\.\d+__[a-zA-Z0-9_]+\.sql$ ]]; then
        echo "Error: Invalid naming convention in $file"
        exit 1
    fi

    # Add additional checks as needed
done


