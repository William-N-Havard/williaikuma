#!usr/bin/env python
# -*- coding: utf8 -*-
#
# -----------------------------------------------------------------------------
#   File: AbstractDataProvider.py (as part of project Williaikuma)
#   Created: 30/10/2022 15:39
#   Last Modified: 30/10/2022 15:39
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

from williaikuma.models.Messages import MSG


class AbstractDataProvider(abc.ABC):
    def __init__(self, path):
        self.path = path
        self._data = None
        self._index = -1

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    @property
    def item(self):
        return self[self.index]

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, value):
        assert type(value) == int, ValueError(MSG.EXCEPT_INDEX_NOT_INTEGER)
        assert value >= -1, ValueError(MSG.EXCEPT_INDEX_NEGATIVE.format(value))
        self._index = value

    @abc.abstractmethod
    def __getitem__(self, item):
        pass

    @abc.abstractmethod
    def load(self):
        pass

    def previous(self):
        self.index = self.index - 1 if self.index > 0 else len(self.data) - 1

    def next(self):
        self.index = self.index + 1 if self.index < len(self.data) - 1 else 0

    def __len__(self):
        return len(self.data)
