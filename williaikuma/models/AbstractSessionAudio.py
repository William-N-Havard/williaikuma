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

from williaikuma.models.defaults import SAMPLING_RATE, NUM_CHANNELS
from williaikuma.models.AbstractSession import AbstractSession

class AbstractSessionAudio(AbstractSession, abc.ABC):
    def __init__(self, sampling_rate=SAMPLING_RATE, num_channels=NUM_CHANNELS, **kwargs):
        super(AbstractSessionAudio, self).__init__(**kwargs)

        # Recording metadata
        self.sampling_rate = sampling_rate
        self.num_channels = num_channels
        self.recordings_list = {}

        # Path metadata
        self.recordings_path = os.path.join(self.path, 'wavs')
        self.textgrid_path = os.path.join(self.path, 'textgrids')


    def start(self):
        super().start()

        if not os.path.exists(self.recordings_path):
            os.makedirs(self.recordings_path)

        found_recordings = self.list_recordings()

        self.recordings_list = {self.item_index_from_rec_name(rec): rec for rec in found_recordings}
        self.data.index = max(self.recordings_list.keys()) if found_recordings else -1

    def list_recordings(self):
        return [os.path.join(self.recordings_path, item) for item in os.listdir(self.recordings_path)
                if item.endswith('.wav')]

    def save(self):
        audio_metadata = {
            'sampling_rate': self.sampling_rate,
            'num_channels': self.num_channels,
        }

        super().save(audio_metadata)


    @property
    def recordings_done(self):
        return len(self.recordings_list)

    def register_done_recording(self, recording_path):
        item_idx = self.item_index_from_rec_name(recording_path)
        self.recordings_list[item_idx] = recording_path

    def register_removed_recording(self, recording_path):
        item_idx = self.item_index_from_rec_name(recording_path)
        del self.recordings_list[item_idx]

    @property
    def index(self):
        return self.data.index

    @abc.abstractmethod
    def update_current_data_item(self):
        pass

    @abc.abstractmethod
    def item_save_path(self):
        pass

    @abc.abstractmethod
    def item_index_from_rec_name(self):
        pass

    @abc.abstractmethod
    def get_missing_items(self):
        pass

    @abc.abstractmethod
    def generate_textgrids(self):
        pass
