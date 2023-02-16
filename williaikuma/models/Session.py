#!usr/bin/env python
# -*- coding: utf8 -*-
#
# -----------------------------------------------------------------------------
#   File: Session.py (as part of project Williaikuma)
#   Created: 30/10/2022 21:24
#   Last Modified: 30/10/2022 21:24
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

import abc

from williaikuma.models.SessionRecording import SessionRecording
from williaikuma.models.SessionRespeaking import SessionRespeaking
from williaikuma.models.Tasks import TASKS
from williaikuma.models.utils import json_read


class Session(abc.ABC):
    def __init__(self):
        raise PermissionError('Class `{}` is not instanciable and may only be used as a factory '
                              'using .load() and .init() methods.'.format(type(self).__name__))

    @staticmethod
    def load(version, session_json):
        metadata = json_read(session_json)

        task = TASKS.from_string(metadata['task'])
        if task == TASKS.TEXT_ELICITATION:
            session = SessionRecording
        elif task == TASKS.RESPEAKING:
            session = SessionRespeaking
        else:
            raise ValueError('Unknown type of task `{}`.'.format(task))

        return session.load(session_json=session_json,  version=version)

    @staticmethod
    def init(task, version, **kwargs):
        if task == TASKS.TEXT_ELICITATION:
            session = SessionRecording
        elif task == TASKS.RESPEAKING:
            session = SessionRespeaking
        else:
            raise ValueError('Unknown type of task `{}`.'.format(task))

        return session(task=task, version=version, **kwargs)