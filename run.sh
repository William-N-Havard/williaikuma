#!/usr/bin/bash

eval "$(conda shell.bash hook)"
conda activate RECORDER
export LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu/alsa-lib/
export PYTHONFAULTHANDLER=1
python main.py
