#!usr/bin/env python
# -*- coding: utf8 -*-
#
# -----------------------------------------------------------------------------
#   File: DataProviderText.py (as part of project noname.py)
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

from models.AbstractDataProvider import AbstractDataProvider

class DataProviderText(AbstractDataProvider):
    def __init__(self, path):
        super(DataProviderText, self).__init__(path=path)

    def load(self):
        data = []
        for i_line, line in enumerate(text_read(self.path), 1):
            assert ' ## ' in line, ValueError("' ## ' not found on line {}.".format(i_line))
            data.append(line.split(' ## '))
        self.data = data


    def __getitem__(self, index):
        sentence, sentence_id = self.data[index]
        sentence = sentence.strip()
        sentence_id = sentence_id.strip()

        return sentence, sentence_id
