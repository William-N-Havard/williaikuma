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

from models.AbstractDataProvider import AbstractDataProvider
from models.utils import json_read


class AudioDataProvider(AbstractDataProvider):
    def __init__(self, path):
        super().__init__(path=path)

    def load(self):
        self._set_wav_path()

        wavs = natsorted([os.path.join(self.wav_path, item) for item in os.listdir(self.wav_path)
                if item.endswith('.wav')])
        self.data = wavs


    def _set_wav_path(self):
        json_data = json_read(self.path)
        source_root_path = json_data['path']

        self.wav_path = os.path.join(source_root_path, 'wavs')


    def __getitem__(self, index):
        sentence_recording = self.data[index]
        sentence_recording_name = os.path.basename(os.path.splitext(sentence_recording)[0])
        return sentence_recording, sentence_recording_name
