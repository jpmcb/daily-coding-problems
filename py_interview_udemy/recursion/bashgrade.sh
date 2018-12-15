#!/bin/bash

# for each file ...
for x in *.py
do
    string_arr=(${x//_/ })

    # make ONID directory
    mkdir $string_arr
    mv $x $string_arr
    cd $string_arr

    cat "--- Running python program --- \n" >> "result.txt"

    python $x >> "result.txt" || python3 $x >> "result.txt"

    cat "--- Checking file contents --- \n" >> "result.txt"

    for y in .
    do
        cat y >> "result.txt"
        wc -c y >> "result.txt"
    done

    # Go back to all ONID directories
    cd ../
done