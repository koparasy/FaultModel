#!/bin/bash

cmd=$1
if [ "$cmd" == "clean" ]; then
    cd lib 
    make clean
    cd ..
    cd applications/ 
    make clean
    cd ..
elif [ "$cmd" == "build" ]; then
    cd lib 
    make
    cd ..
    cd applications/
    make
    cd ..
else
    echo "Give a valid command"
fi    

