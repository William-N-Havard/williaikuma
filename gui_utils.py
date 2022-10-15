#!usr/bin/env python
# -*- coding: utf8 -*-
#
# -----------------------------------------------------------------------------
#   File: gui_utils.py (as part of project noname.py)
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
    BUTTON_RECORD_ON = os.path.join('.', 'assets', 'record.png')
    BUTTON_RECORD_OFF = os.path.join('.', 'assets', 'stop.png')
    BUTTON_PLAY_ON = os.path.join('.', 'assets', 'play.png')
    BUTTON_PLAY_OFF = os.path.join('.', 'assets', 'pause.png')
    BUTTON_DELETE = os.path.join('.', 'assets', 'cross-mark.png')
    BUTTON_LEFT = os.path.join('.', 'assets', 'left-arrow.png')
    BUTTON_RIGHT = os.path.join('.', 'assets', 'right-arrow.png')