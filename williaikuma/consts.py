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


DATE_FORMAT = "%d/%m/%Y %H:%M:%S"

# Do not change: design required by PyInstaller on Windows
# Does not prevent the app from running on Linux fortunately!
try:
    WORK_DIR = sys._MEIPASS
except AttributeError:
    debug_dir = '/home/whavard/CODE/OTHER/williaikuma'
    WORK_DIR = os.getcwd() if not os.path.exists(debug_dir) else debug_dir


IMAGE_PATH = os.path.join(WORK_DIR, 'williaikuma', 'assets', 'images')
LOCAL_PATH = os.path.join(WORK_DIR, 'williaikuma', 'assets', 'locales')


def project_dirs(project_path):
    # Root project path
    paths = [project_path]
    # Data path used to store session's source sentences
    paths.append(os.path.join(project_path, 'data'))

    return paths