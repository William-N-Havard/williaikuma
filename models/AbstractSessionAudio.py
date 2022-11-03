#!usr/bin/env python
# -*- coding: utf8 -*-
#
# -----------------------------------------------------------------------------
#   File: AbstractSessionAudio.py (as part of project Williaikuma)
#   Created: 19/10/2022 04:53
#   Last Modified: 19/10/2022 04:53
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
import abc
from pympi import Praat

from models.defaults import SAMPLING_RATE, NUM_CHANNELS
from models.AbstractSession import AbstractSession
from models.utils import get_recording_length


class AbstractSessionAudio(AbstractSession, abc.ABC):
    def __init__(self, sampling_rate=SAMPLING_RATE, num_channels=NUM_CHANNELS, **kwargs):
        super(AbstractSessionAudio, self).__init__(**kwargs)

        # Recording metadata
        self.sampling_rate = sampling_rate
        self.num_channels = num_channels
        self.recordings_done = 0

        # Path metadata
        self.recordings_path = os.path.join(self.path, 'wavs')
        self.textgrid_path = os.path.join(self.path, 'textgrids')


    @abc.abstractmethod
    def update_current_data_item(self):
        pass


    def start(self):
        super().start()

        if not os.path.exists(self.recordings_path):
            os.makedirs(self.recordings_path)

        found_recordings = self.list_recordings()
        max_line = max([self.item_index(rec) for rec in found_recordings])-1 if found_recordings else -1
        self.data.index = max_line
        self.recordings_done = len(found_recordings)


    def list_recordings(self):
        return [item for item in os.listdir(self.recordings_path) if item.endswith('.wav')]


    def save(self):
        audio_metadata = {
            'sampling_rate': self.sampling_rate,
            'num_channels': self.num_channels,
        }

        super().save(audio_metadata)

    @property
    def index(self):
        return self.data.index
