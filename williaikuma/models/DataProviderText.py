#!usr/bin/env python
# -*- coding: utf8 -*-
#
# -----------------------------------------------------------------------------
#   File: DataProviderText.py (as part of project Williaikuma)
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
import csv

from williaikuma.models.AbstractDataProvider import AbstractDataProvider
from williaikuma.models.Messages import MSG
from williaikuma.models.utils import read_csv, text_read


class DataProviderText(AbstractDataProvider):
    def __init__(self, path):
        super(DataProviderText, self).__init__(path=path)

    def load(self):
        # Different loading scheme depending on the file type
        if self.path.endswith('.txt'):
            data = []
            for i_line, line in enumerate(text_read(self.path), 1):
                assert ' ## ' in line, ValueError(MSG.EXCEPT_MISSING_LINE_SEP.format(i_line))
                data.append(line.split(' ## '))
        elif self.path.endswith('.csv'):
            try:
                data = read_csv(self.path)
            except:
                raise ValueError(MSG.EXCEPT_CSV_FILE)
            try:
                data = [(line['sentence'], line['sentence_id']) for line in data]
            except:
                raise ValueError(MSG.EXCEPT_CSV_COLUMN)
        else:
            raise MSG.EXCEPT_FILE_TYPES.format("txt, csv")

        self.data = data


    def __getitem__(self, index):
        sentence, sentence_id = self.data[index]
        sentence = sentence.strip()
        sentence_id = sentence_id.strip()

        return sentence, sentence_id
