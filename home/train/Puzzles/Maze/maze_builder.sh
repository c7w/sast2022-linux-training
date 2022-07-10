#!/bin/bash

function build_maze() {
        # echo $1
        if [ $1 -gt 6 ] # Make it 6 layers deep
        then
                return
        fi
        for loop in 1 2 3
        do
                filename=$(tr -dc A-Za-z0-9 </dev/urandom | head -c 6)
                # echo $filename
                mkdir $filename
                cd $filename
                build_maze `expr $1 + 1`
                cd ..
        done
}

build_maze 0

# Now I'm gonna put the flag in one of the leaf dir.
