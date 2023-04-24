#!usr/bin/env python
# -*- coding: utf8 -*-
#
# -----------------------------------------------------------------------------
#   File: utils.py (as part of project Williaikuma)
#   Created: 21/04/2023 11:17
#   Last Modified: 21/04/2023 11:17
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

from williaikuma.models.Messages import MSG
from williaikuma.models.utils import now_raw
from williaikuma.views import MessageBoxes


def generate_session_path(data_path, task, speaker, session_dir):
    datetime_now = now_raw()
    data_source_filename = os.path.basename(data_path)
    data_source_filename_wo_ext = os.path.splitext(data_source_filename)[0]

    session_name = '{}_session_{}_{}_{}'.format(
        task.value, speaker, data_source_filename_wo_ext, datetime_now)
    session_path = os.path.join(session_dir, session_name)

    return session_path, session_name


def select_writable_dir(initial_dir=os.path.expanduser('~')):
    session_root_dir = None
    while not session_root_dir:
        session_root_dir = MessageBoxes.action_choose_dir(initial_dir=initial_dir)

        # Warn user if dir is not writable
        if session_root_dir and not os.access(session_root_dir, os.W_OK):
            session_root_dir = None
            MessageBoxes.action_notify(MSG.TITLE_ERROR, MSG.EXCEPT_PATH_NOT_WRITABLE)

    return session_root_dir

def get_parent_dir(path):
    return os.path.abspath(os.path.join(path, os.pardir))