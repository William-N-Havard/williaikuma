#!usr/bin/env python
# -*- coding: utf8 -*-
#
# -----------------------------------------------------------------------------
#   File: DataProvider.py (as part of project noname.py)
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


class DataProvider(object):
    def __init__(self, path):
        self.path = path
        self.load()


    def load(self):
        self.data = list(text_read(self.path))


    def __getitem__(self, index):
        sentence, sentence_id = self.data[index].split(' ## ')
        sentence = sentence.strip()
        sentence_id = sentence_id.strip()

        return sentence, sentence_id


    def __len__(self):
        return len(self.data)