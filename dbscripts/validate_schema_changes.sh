#!/bin/bash

for file in $(find . -type f -name '*.sql' ! -path './dbscripts/*'); do
    echo "Checking $file"
    if ! [[ $(basename "$file") =~ ^[vV]\d+\.\d+\.\d+__[a-zA-Z0-9_]+\.sql$ ]]; then
        echo "Error: Invalid naming convention in $file"
        exit 1
    fi

    # Add additional checks as needed
done



