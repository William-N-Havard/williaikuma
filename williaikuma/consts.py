#!usr/bin/env python
# -*- coding: utf8 -*-
#
# -----------------------------------------------------------------------------
#   File: utils.py (as part of project Williaikuma)
#   Created: 14/04/2023 14:58
#   Last Modified: 14/04/2023 14:58
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

# Do not change: design required by PyInstaller on Windows
# Does not prevent the app from running on Linux fortunately!
try:
    WORK_DIR = sys._MEIPASS
except AttributeError:
    WORK_DIR = os.getcwd()

IMAGE_PATH = os.path.join(WORK_DIR, 'williaikuma', 'assets', 'images')
LOCAL_PATH = os.path.join(WORK_DIR, 'williaikuma', 'assets', 'locales')