#!usr/bin/env python
# -*- coding: utf8 -*-
#
# -----------------------------------------------------------------------------
#   File: utils.py (as part of project Williaikuma)
#   Created: 15/10/2022 03:38
#   Last Modified: 15/10/2022 03:38
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
import sys
from enum import Enum, unique

try:
   wd = sys._MEIPASS
except AttributeError:
   wd = os.getcwd()

BASE_PATH = os.path.join(wd, 'williaikuma', 'assets', 'images')

@unique
class TkinterButtons(Enum):
    BUTTON_RECORD_ON = os.path.join(BASE_PATH, 'record.png')
    BUTTON_RECORD_OFF = os.path.join(BASE_PATH, 'stop.png')
    BUTTON_PLAY_ON = os.path.join(BASE_PATH, 'play.png')
    BUTTON_PLAY_OFF = os.path.join(BASE_PATH, 'pause.png')
    BUTTON_DELETE = os.path.join(BASE_PATH, 'cross-mark.png')
    BUTTON_LEFT = os.path.join(BASE_PATH, 'left-arrow.png')
    BUTTON_RIGHT = os.path.join(BASE_PATH, 'right-arrow.png')
    BUTTON_RESPEAK = os.path.join(BASE_PATH, 'music-note.png')