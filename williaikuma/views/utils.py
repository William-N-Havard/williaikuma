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
from enum import Enum, unique

@unique
class TkinterButtons(Enum):
    BUTTON_RECORD_ON = os.path.join('williaikuma', 'assets', 'images', 'record.png')
    BUTTON_RECORD_OFF = os.path.join('williaikuma', 'assets', 'images', 'stop.png')
    BUTTON_PLAY_ON = os.path.join('williaikuma', 'assets', 'images', 'play.png')
    BUTTON_PLAY_OFF = os.path.join('williaikuma', 'assets', 'images', 'pause.png')
    BUTTON_DELETE = os.path.join('williaikuma', 'assets', 'images', 'cross-mark.png')
    BUTTON_LEFT = os.path.join('williaikuma', 'assets', 'images', 'left-arrow.png')
    BUTTON_RIGHT = os.path.join('williaikuma', 'assets', 'images', 'right-arrow.png')
    BUTTON_RESPEAK = os.path.join('williaikuma', 'assets', 'images', 'music-note.png')