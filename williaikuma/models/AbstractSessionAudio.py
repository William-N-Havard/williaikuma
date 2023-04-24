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
    def __init__(self, sampling_rate=SAMPLING_RATE, num_channels=NUM_CHANNELS, recording_retakes=dict(), **kwargs):
        super(AbstractSessionAudio, self).__init__(**kwargs)

        # Recording metadata
        self.sampling_rate = sampling_rate
        self.num_channels = num_channels

        self.recordings_list = {}
        self.recording_retakes = {int(k):int(v) for k, v in recording_retakes.items()} # Restore int indices

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
            'recording_retakes': self.recording_retakes
        }

        super().save(audio_metadata, allowed_overwrite=['recording_retakes'])


    @property
    def recordings_done(self):
        return len(self.recordings_list)

    def register_done_recording(self, recording_path):
        item_idx = self.item_index_from_rec_name(recording_path)
        self.recordings_list[item_idx] = recording_path
        # Remove from retakes
        if item_idx in self.recording_retakes:
            del self.recording_retakes[item_idx]

    def register_removed_recording(self, recording_path):
        item_idx = self.item_index_from_rec_name(recording_path)
        # Add retakes
        self.recording_retakes[item_idx] = self.item_retake_from_rec_name(recording_path)
        # Delete from list of recordings
        del self.recordings_list[item_idx]

    @property
    def index(self):
        return self.data.index

    @abc.abstractmethod
    def update_current_data_item(self):
        pass

    @abc.abstractmethod
    def item_recording_path(self):
        pass

    @abc.abstractmethod
    def item_index_from_rec_name(self):
        pass

    @abc.abstractmethod
    def item_retake_from_rec_name(self):
        pass

    @abc.abstractmethod
    def get_missing_items(self):
        pass

    @abc.abstractmethod
    def generate_textgrids(self):
        pass
