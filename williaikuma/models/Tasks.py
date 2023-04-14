#!usr/bin/env python
# -*- coding: utf8 -*-
#
# -----------------------------------------------------------------------------
#   File: Tasks.py (as part of project Williaikuma)
#   Created: 15/10/2022 04:52
#   Last Modified: 15/10/2022 04:52
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

from enum import Enum, unique


@unique
class TASKS(Enum):
    TEXT_ELICITATION = 'text-elicitation'
    RESPEAKING = 'respeaking'

    @staticmethod
    def from_string(label):
        for tasks_const in list(TASKS):
            if tasks_const.value == label:
                return tasks_const
        raise ValueError(gettext("Unknown type of task `{}`.").format(label))