#!/bin/bash

if [ -f pip_installs.txt ]; then
    pip install -r pip_installs.txt
else
    echo "pip_installs.txt file not found."
fi
