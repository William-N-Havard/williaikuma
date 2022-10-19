#!usr/bin/env python
# -*- coding: utf8 -*-
#
# -----------------------------------------------------------------------------
#   File: utils.py (as part of project noname.py)
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
from enum import Enum, unique

@unique
class TkinterButtons(Enum):
    BUTTON_RECORD_ON = os.path.join('assets', 'images', 'record.png')
    BUTTON_RECORD_OFF = os.path.join('assets', 'images', 'stop.png')
    BUTTON_PLAY_ON = os.path.join('assets', 'images', 'play.png')
    BUTTON_PLAY_OFF = os.path.join('assets', 'images', 'pause.png')
    BUTTON_DELETE = os.path.join('assets', 'images', 'cross-mark.png')
    BUTTON_LEFT = os.path.join('assets', 'images', 'left-arrow.png')
    BUTTON_RIGHT = os.path.join('assets', 'images', 'right-arrow.png')
    BUTTON_RESPEAK = os.path.join('assets', 'images', 'music-note.png')