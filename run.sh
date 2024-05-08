#!/bin/bash

python3 -m venv .venv
source .venv/bin/activate
pip3 install colored
pip install numpy
pip install matplotlib
python3 DietTracker.py