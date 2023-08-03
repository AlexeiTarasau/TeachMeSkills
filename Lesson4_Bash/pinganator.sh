#!/bin/bash

#argument checking
if [ $# -ne 2 ]; then
    echo "Invalid number of arguments!"
    exit 1
fi

#Assignment of arguments
uri=$1
retries=$2

#File for writing the result
output_file="ping_results.txt"

#Ping host
for ((i=1; i<=$retries; i++))
do
    ping -c $retries $uri > $output_file
done

echo "Ping complited!!!"
