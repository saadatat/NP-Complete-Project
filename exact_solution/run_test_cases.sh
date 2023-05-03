#!/bin/bash

# Loop through all test case files and run the script with each one
for file in test_cases/test_*.txt
do
    echo "Running test case: $file"
    python3 longest_path_exact_solution.py < "$file"
done