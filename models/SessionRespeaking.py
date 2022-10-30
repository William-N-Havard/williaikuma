#!usr/bin/env python
# -*- coding: utf8 -*-
#
# -----------------------------------------------------------------------------
#   File: SessionRecording.py (as part of project Williaikuma)
#   Created: 19/10/2022 04:23
#   Last Modified: 19/10/2022 04:23
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

from models.AbstractSessionAudio import AbstractSessionAudio
from models.DataProviderAudio import DataProviderAudio
from models.utils import json_read



class SessionRespeaking(AbstractSessionAudio):
    def __init__(self, **kwargs):
        super(SessionRespeaking, self).__init__(**kwargs)

        self.data = DataProviderAudio(self.data_path)

        self.current_sentence_recording = None
        self.current_sentence_recording_name = None

        self.save()

    def update_current_data_item(self):
        sentence_recording, sentence_recording_name = self.data.item
        self.current_sentence_recording = sentence_recording
        self.current_sentence_recording_name = sentence_recording_name


    def item_save_path(self):
        raw_sentence_recording = os.path.basename(os.path.splitext(self.current_sentence_recording)[0])

        return os.path.join(self.recordings_path, '{}_respeak-speaker-{}.wav'.format(
            raw_sentence_recording, self.speaker))

    def item_index(self, recording_name):
        return int(recording_name.split('_')[0].split('-')[-1])


    def get_missing_items(self):
        existing_recordings = [self.item_index(item) for item in self.list_recordings()]
        target_recortings = [self.item_index(item) for item in os.listdir(self.data.wav_path)
                             if item .endswith('.wav')]
        missing_indices = sorted(list(set(target_recortings)-set(existing_recordings)))
        return missing_indices


    @classmethod
    def load(cls, session_json):
        session_path, _ = os.path.split(session_json)
        session_metadata = json_read(session_json)

        return cls(**session_metadata)