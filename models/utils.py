#!usr/bin/env python
# -*- coding: utf8 -*-
#
# -----------------------------------------------------------------------------
#   File: utils.py (as part of project noname.py)
#   Created: 15/10/2022 00:51
#   Last Modified: 15/10/2022 00:51
# -----------------------------------------------------------------------------
#   Author: William N. Havard
#           Postdoctoral Researcher
#
#   Mail  : william.havard@ens.fr / william.havard@gmail.com
#  
#   Institution: ENS / Laboratoire de Sciences Cognitives et Psycholinguistique
#
# ------------------------------------------------------------------------------
#   Description: 
#       • 
# -----------------------------------------------------------------------------

import json
import os
import wave
from datetime import datetime


def assert_recording_exists(path):
    return os.path.exists(path)


def assert_recording_readable(path):
    return os.path.exists(path)


def text_read(txt_path):
    with open(txt_path, 'r') as in_file:
        lines = map(str.strip, in_file.readlines())
    return lines


def json_read(json_path):
    with open(json_path) as in_json:
        return json.load(in_json)


def json_dump(json_path, data):
    with open(json_path, 'w') as out_json:
        json.dump(data, out_json)


def get_recording_length(path):
    with wave.open(path, 'r') as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)

    return duration

now = lambda: datetime.now().strftime("%d/%m/%Y %H:%M:%S")