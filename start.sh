#!/bin/bash
PWD=`pwd`
activate () {
    source $PWD/venv/bin/activate
}

activate

#!/usr/bin/python3
python3 main.py
