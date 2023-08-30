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

import wx

from williaikuma.utilities.FrozenEnum import FrozenEnum
from williaikuma.consts import IMAGE_PATH


@unique
class ImagesButtons(Enum, metaclass=FrozenEnum):
    BUTTON_RECORD_ON = os.path.join(IMAGE_PATH, 'record.png')
    BUTTON_RECORD_OFF = os.path.join(IMAGE_PATH, 'stop.png')
    BUTTON_PLAY_ON = os.path.join(IMAGE_PATH, 'play.png')
    BUTTON_PLAY_OFF = os.path.join(IMAGE_PATH, 'pause.png')
    BUTTON_DELETE = os.path.join(IMAGE_PATH, 'cross-mark.png')
    BUTTON_LEFT = os.path.join(IMAGE_PATH, 'left-arrow.png')
    BUTTON_RIGHT = os.path.join(IMAGE_PATH, 'right-arrow.png')
    BUTTON_RESPEAK = os.path.join(IMAGE_PATH, 'music-note.png')

    def _accessed(self):
        return self.value
