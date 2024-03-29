#!usr/bin/env python
# -*- coding: utf8 -*-
#
# -----------------------------------------------------------------------------
#   File: utils.py (as part of project Williaikuma)
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
import csv
import json
import os
import wave
from datetime import datetime

from pympi import Praat

from williaikuma.consts import DATE_FORMAT

now = lambda: datetime.now().strftime(DATE_FORMAT)
now_raw = lambda: now().replace(' ', '-').replace('/', '').replace(':', '')

def resolve_relative_path(prefix_path, target_path):
    if os.path.isabs(target_path):
        return target_path
    else:
        return os.path.abspath(os.path.join(prefix_path, target_path))


def assert_recording_exists(path):
    return os.path.exists(path)


def assert_recording_readable(path):
    return os.path.exists(path)


def text_read(txt_path):
    with open(txt_path, 'r', encoding='utf-8') as in_file:
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

def create_praat_tg(rec_length, sentence, textgrid_path, raw_filename):
    tg = Praat.TextGrid(xmin=0, xmax=rec_length)
    tier = tg.add_tier('transcription')
    tier.add_interval(begin=0, end=rec_length, value=sentence)
    tg.to_file(filepath=os.path.join(textgrid_path, '{}.TextGrid'.format(raw_filename)),
               codec='utf-8')


def read_csv(path_csv):
    with open(path_csv, encoding="utf-8") as csv_file:
        dialect = csv.Sniffer().sniff(csv_file.read(1024));
        csv_file.seek(0)
        data = csv.DictReader(csv_file, dialect=dialect)
        return list(data)
