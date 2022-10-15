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

import os


def assert_recording_exists(path):
    return os.path.exists(path)


def assert_recording_readable(path):
    return os.path.exists(path)


def text_read(txt_path):
    with open(txt_path, 'r') as in_file:
        lines = map(str.strip, in_file.readlines())
    return lines
