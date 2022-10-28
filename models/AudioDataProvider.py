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
import os

from natsort import natsorted
from models.utils import json_read


class AudioDataProvider(object):
    def __init__(self, path):
        self.path = path
        self._index = -1


    def load(self):
        self.set_wav_path()

        self.data = []
        wavs = natsorted([os.path.join(self.wav_path, item) for item in os.listdir(self.wav_path)
                if item.endswith('.wav')])
        self.data = wavs


    def set_wav_path(self):
        json_data = json_read(self.path)
        source_root_path = json_data['path']

        self.wav_path = os.path.join(source_root_path, 'wavs')


    @property
    def item(self):
        return self[self.index]


    @property
    def index(self):
        return self._index


    @index.setter
    def index(self, value):
        assert type(value) == int, ValueError("Index can only be an integer!")
        assert value >= 0, ValueError("Index can't be negative!")
        self._index = value
        

    def previous(self):
        self.index = self.index - 1 if self.index > 0 else len(self.data) - 1


    def next(self):
        self.index = self.index + 1 if self.index < len(self.data) - 1 else 0


    def __getitem__(self, index):
        sentence_recording = self.data[index]
        sentence_recording_name = os.path.basename(os.path.splitext(sentence_recording)[0])
        return sentence_recording, sentence_recording_name


    def __len__(self):
        return len(self.data)