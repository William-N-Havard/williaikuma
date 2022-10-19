#!usr/bin/env python
# -*- coding: utf8 -*-
#
# -----------------------------------------------------------------------------
#   File: TextDataProvider.py (as part of project noname.py)
#   Created: 16/10/2022 16:37
#   Last Modified: 16/10/2022 16:37
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


from .utils import text_read


class TextDataProvider(object):
    def __init__(self, path):
        self.path = path
        self.index = -1


    def load(self):
        self.data = []
        for i_line, line in enumerate(text_read(self.path), 1):
            assert ' ## ' in line, ValueError("' ## ' not found on line {}.".format(i_line))
            self.data.append(line)


    @property
    def item(self):
        return self[self.index]


    def previous(self):
        self.index = self.index - 1 if self.index > 0 else len(self.data) - 1


    def next(self):
        self.index = self.index + 1 if self.index < len(self.data) - 1 else 0


    def __getitem__(self, index):
        sentence, sentence_id = self.data[index].split(' ## ')
        sentence = sentence.strip()
        sentence_id = sentence_id.strip()

        return sentence, sentence_id


    def __len__(self):
        return len(self.data)