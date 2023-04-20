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

from williaikuma.models.Messages import MSG


@unique
class TASKS(Enum):

    TEXT_ELICITATION = (('txt', 'csv'),)
    RESPEAKING = (('json',))


    def __new__(cls, *args):
        obj = object.__new__(cls)
        obj._value_ = None
        return obj

    def __init__(self, extensions):
        self._value_ = self._name_.lower().replace('_', '-')
        self.extensions = extensions

    @staticmethod
    def from_string(label):
        for tasks_const in list(TASKS):
            if tasks_const.value == label:
                return tasks_const
        raise ValueError(MSG.EXCEPT_UNKNOWN_TASK.format(label))
