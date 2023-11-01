#!/bin/bash

FILENAME="packages.txt"

python -m pip install --upgrade pip

if [ -f $FILENAME ]; then
    pip install -r $FILENAME
else
    echo "File '$FILENAME' not found."
fi
