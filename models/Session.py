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

from pympi import Praat
from .TextDataProvider import TextDataProvider
from .utils import json_read, json_dump, get_recording_length


class Session(object):
    def __init__(self, name, path, data_path, speaker, task,
                 sampling_rate=44100, num_channels=1):

        # Default Session Metadata
        self.name = name
        self.path = path
        self.data_path = data_path
        self.speaker = speaker
        self.task = task

        # Recording metadata
        self.sampling_rate = sampling_rate
        self.num_channels = num_channels

        # Path metadata
        self.recordings_path = os.path.join(self.path, 'wavs')
        self.textgrid_path = os.path.join(self.path, 'textgrids')

        self.data = TextDataProvider(self.data_path)
        self.index = -1

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

        if not os.path.exists(self.recordings_path):
            os.makedirs(self.recordings_path)

        found_recordings = self.list_recordings()
        max_line = max([self.get_recording_line_number(rec) for rec in found_recordings])-1 if found_recordings else -1
        self.index = max_line
        self.recordings_done = len(found_recordings)


    def previous(self):
        index = self.index - 1 if self.index > 0 else len(self.data) - 1
        self._update_current_item(index)


    def next(self):
        index = self.index + 1 if self.index < len(self.data) - 1 else 0
        self._update_current_item(index)


    def _update_current_item(self, index):
        self.index = index
        sentence_text, sentence_id = self.data[index]
        self.current_sentence_text = sentence_text
        self.current_sentence_id = sentence_id

        return self.current_sentence_text


    def list_recordings(self):
        return [item for item in os.listdir(self.recordings_path) if item.endswith('.wav')]


    def generate_textgrids(self):
        if not os.path.exists(self.textgrid_path): os.makedirs(self.textgrid_path)

        # Go through each recording
        done = 0
        errors = []
        try:
            for wav_file in self.list_recordings():
                raw_filename = os.path.basename(os.path.splitext(wav_file)[0])
                rec_length = get_recording_length(os.path.join(self.recordings_path, wav_file))
                line_number = self.get_recording_line_number(wav_file)
                sentence, _ = self.data[line_number-1]

                tg = Praat.TextGrid(xmin=0, xmax=rec_length)
                tier = tg.add_tier('transcription')
                tier.add_interval(begin=0, end=rec_length, value=sentence)
                tg.to_file(filepath=os.path.join(self.textgrid_path, '{}.TextGrid'.format(raw_filename)),
                           codec='utf-8')
                done += 1
        except:
            errors.append(wav_file)
        return done, errors


    def get_current_sentence_recording_path(self):
        return os.path.join(self.recordings_path, 'line-{}_sentid-{}_speaker-{}.wav'.format(
            self.index+1, self.current_sentence_id, self.speaker))


    def get_recording_line_number(self, recording_name):
        return int(recording_name.split('_')[0].split('-')[-1])


    def save(self):
        if os.path.exists(self.session_metadata_path):
            existing_metadata = json_read(self.session_metadata_path)
        else:
            existing_metadata = False

        metadata = {
            'name': self.name,
            'path': self.path,
            'data_path': self.data_path,
            'speaker': self.speaker,
            'sampling_rate': self.sampling_rate,
            'num_channels': self.num_channels,
            'task': self.task,
        }

        if existing_metadata:
            for k, v in metadata.items():
                assert existing_metadata[k] == v, \
                    ValueError('Value between existing metadata file and new metdata differ ({} v. {}'.format(
                        existing_metadata[k], v
                    ))
                if k not in metadata.keys():
                    metadata[k] = v

        json_dump(self.session_metadata_path, metadata)


    def open(self, metadata_file):
        return json_read(metadata_file)


    @classmethod
    def load(cls, session_json):
        session_path, _ = os.path.split(session_json)
        session_metadata = json_read(session_json)

        return cls(**session_metadata)
