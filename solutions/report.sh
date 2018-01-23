#! /usr/bin/env bash

for filename in $(ls . | sort -n); do


    if [[ "$filename" != "report.sh" ]] &&
       [[ "$filename" != "common.py" ]] ; then

        extension="${filename##*.}"
        name="${filename%.*}"

        echo "Problem: $name"
        if [[ "$extension" == "py" ]] ; then
            python3 $filename
        elif [[ "$extension" == "scm" ]] ; then
            racket -f "$filename" -e "(problem)"
        fi
        echo
    fi

done
