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

import json
import os
import wave
from datetime import datetime
from enum import Enum, EnumMeta

from pympi import Praat

now = lambda: datetime.now().strftime("%d/%m/%Y %H:%M:%S")

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

def create_praat_tg(rec_length, sentence, textgrid_path, raw_filename):
    tg = Praat.TextGrid(xmin=0, xmax=rec_length)
    tier = tg.add_tier('transcription')
    tier.add_interval(begin=0, end=rec_length, value=sentence)
    tg.to_file(filepath=os.path.join(textgrid_path, '{}.TextGrid'.format(raw_filename)),
               codec='utf-8')

class FrozenEnum(EnumMeta):
    """
    This EnumMeta allows the subclass to call the _accessed() function
    everytime a member of the class is accessed.
    Most code from https://stackoverflow.com/questions/54274002/python-enum-prevent-invalid-attribute-assignment
    """
    def __new__(mcls, name, bases, classdict):
        classdict['__frozenenummeta_creating_class__'] = True
        enum = super().__new__(mcls, name, bases, classdict)
        del enum.__frozenenummeta_creating_class__
        return enum

    def __call__(cls, value, names=None, *, module=None, **kwargs):
        if names is None:  # simple value lookup
            return cls.__new__(cls, value)
        enum = Enum._create_(value, names, module=module, **kwargs)
        enum.__class__ = type(cls)
        return enum

    def __setattr__(cls, name, value):
        members = cls.__dict__.get('_member_map_', {})
        if hasattr(cls, '__frozenenummeta_creating_class__') or name in members:
            return super().__setattr__(name, value)
        if hasattr(cls, name):
            msg = "{!r} object attribute {!r} is read-only"
        else:
            msg = "{!r} object has no attribute {!r}"
        raise AttributeError(msg.format(cls.__name__, name))

    def __delattr__(cls, name):
        members = cls.__dict__.get('_member_map_', {})
        if hasattr(cls, '__frozenenummeta_creating_class__') or name in members:
            return super().__delattr__(name)
        if hasattr(cls, name):
            msg = "{!r} object attribute {!r} is read-only"
        else:
            msg = "{!r} object has no attribute {!r}"
        raise AttributeError(msg.format(cls.__name__, name))

    def __getattribute__(cls, name):
        obj = super().__getattribute__(name)
        if isinstance(obj, cls):
            obj = obj._accessed()
        return obj
