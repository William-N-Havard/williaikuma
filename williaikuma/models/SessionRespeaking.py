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

from williaikuma.models.AbstractSessionAudio import AbstractSessionAudio
from williaikuma.models.DataProviderAudio import DataProviderAudio
from williaikuma.models.utils import create_praat_tg, get_recording_length, now_raw


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

        return os.path.join(self.recordings_path, '{}_respeak-speaker-{}_at-{}.wav'.format(
            raw_sentence_recording, self.speaker, now_raw()))

    def item_index_from_rec_name(self, recording_name):
        return int(recording_name.split('_')[0].split('-')[-1])-1


    def get_missing_items(self):
        existing_recordings = [self.item_index_from_rec_name(item) for item in self.list_recordings()]
        target_recortings = [self.item_index_from_rec_name(item) for item in os.listdir(self.data.wav_path)
                             if item .endswith('.wav')]
        missing_indices = sorted(list(set(target_recortings)-set(existing_recordings)), reverse=True)
        return missing_indices


    def generate_textgrids(self):
        if not os.path.exists(self.textgrid_path): os.makedirs(self.textgrid_path)

        # Go through each recording
        done = 0
        errors = []
        try:
            for wav_file in self.list_recordings():
                raw_filename = os.path.basename(os.path.splitext(wav_file)[0])
                rec_length = get_recording_length(os.path.join(self.recordings_path, wav_file))
                line_number = self.item_index_from_rec_name(wav_file)
                sentence, _ = self.data.source_sentences[line_number - 1]

                create_praat_tg(rec_length, sentence, self.textgrid_path, raw_filename)
                done += 1
        except Exception as e:
            errors.append(wav_file)
        return done, errors