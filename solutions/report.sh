#! /usr/bin/env bash

for filename in *; do


    if [[ "$filename" != "report.sh" ]] ; then

        extension="${filename##*.}"
        name="${filename%.*}"

        if [[ "$extension" == "py" ]] ; then

            echo "Problem: $name"
            python3 $filename
            echo

        fi
    fi

done
