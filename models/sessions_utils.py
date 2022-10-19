#!usr/bin/env python
# -*- coding: utf8 -*-
#
# -----------------------------------------------------------------------------
#   File: sessions_utils.py (as part of project Williaikuma)
#   Created: 19/10/2022 17:25
#   Last Modified: 19/10/2022 17:25
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

from models.consts import TASKS
from models.RecordingSession import RecordingSession
from models.RespeakingSession import RespeakingSession
from models.utils import json_read


def session_loader(session_json):
    metadata = json_read(session_json)

    task = TASKS.from_string(metadata['task'])
    if task == TASKS.TEXT_ELICITATION:
        return RecordingSession.load(session_json)
    elif task == TASKS.RESPEAKING:
        return RespeakingSession.load(session_json)
    else:
        raise ValueError('Unknown type of task `{}`.'.format(task))


def session_initiator(task, **kwargs):
    if task == TASKS.TEXT_ELICITATION:
        return RecordingSession(task=task, **kwargs)
    elif task == TASKS.RESPEAKING:
        return RespeakingSession(task=task, **kwargs)
    else:
        raise ValueError('Unknown type of task `{}`.'.format(task))
