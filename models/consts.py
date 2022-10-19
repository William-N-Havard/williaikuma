#!usr/bin/env python
# -*- coding: utf8 -*-
#
# -----------------------------------------------------------------------------
#   File: consts.py (as part of project noname.py)
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

SAMPLING_RATE = 44_100
NUM_CHANNELS = 1

@unique
class TASKS(Enum):
    TEXT_ELICITATION = 'text-elicitation'
    RESPEAKING = 'respeaking'

    @staticmethod
    def from_string(label):
        for tasks_const in list(TASKS):
            if tasks_const.value == label:
                return tasks_const
        raise ValueError('Unknown task {}!'.format(label))