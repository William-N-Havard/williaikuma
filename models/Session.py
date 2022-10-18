#!usr/bin/env python
# -*- coding: utf8 -*-
#
# -----------------------------------------------------------------------------
#   File: Session.py (as part of project noname.py)
#   Created: 16/10/2022 16:34
#   Last Modified: 16/10/2022 16:34
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

from .DataProvider import DataProvider
from .utils import json_read, json_dump


class Session(object):
    def __init__(self, name, path, data_path, speaker,
                 sampling_rate=44100, num_channels=1):

        self.name = name
        self.path = path
        self.data_path = data_path
        self.speaker = speaker
        self.sampling_rate = sampling_rate
        self.num_channels = num_channels

        self.index = -1
        self.data = DataProvider(self.data_path)

        self.current_sentence_text = None
        self.current_sentence_id = None
        self.recordings_done = 0

        self.session_metadata_path = os.path.join(self.path, 'metadata_{}.json'.format(self.name))

        self.save()

    def start(self):
        try:
            self.data.load()
        except Exception as e:
            raise Exception(e)

        found_recordings = [item for item in os.listdir(self.path) if item.endswith('.wav')]
        max_line = max([int(rec.split('_')[0].split('-')[-1]) for rec in found_recordings])-1 if found_recordings else -1
        self.index = max_line
        self.recordings_done = len(found_recordings)


    def previous(self):
        index = self.index - 1 if self.index > 0 else len(self.data) - 1
        self._update_current_sentence(index)


    def next(self):
        index = self.index + 1 if self.index < len(self.data) - 1 else 0
        self._update_current_sentence(index)


    def _update_current_sentence(self, index):
        self.index = index
        sentence_text, sentence_id = self.data[index]
        self.current_sentence_text = sentence_text
        self.current_sentence_id = sentence_id

        return self.current_sentence_text


    def get_current_sentence_recording_path(self):
        return os.path.join(self.path, 'line-{}_sentid-{}_speaker-{}.wav'.format(
            self.index+1, self.current_sentence_id, self.speaker))


    def save(self):
        if os.path.exists(self.session_metadata_path):
            existing_metadata = json_read(self.session_metadata_path)

        metadata = {
            'name': self.name,
            'path': self.path,
            'data_path': self.data_path,
            'speaker': self.speaker,
            'sampling_rate': self.sampling_rate,
            'num_channels': self.num_channels,
        }

        for k, v in metadata.items():
            assert existing_metadata[k] == v, \
                ValueError('Value between existing metadata file and new metdata differ ({} v. {}'.format(
                    existing_metadata[k], v
                ))

        json_dump(self.session_metadata_path, metadata)


    @classmethod
    def load(cls, session_json):
        session_path, _ = os.path.split(session_json)
        session_metadata = json_read(session_json)

        return cls(**session_metadata)
