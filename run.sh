#!/usr/bin/bash

eval "$(conda shell.bash hook)"
conda activate RECORDER
export LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu/alsa-lib/
python main.py
