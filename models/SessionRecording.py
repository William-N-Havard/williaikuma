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

from pympi import Praat

from models.AbstractSessionAudio import AbstractSessionAudio
from models.DataProviderText import DataProviderText
from models.utils import create_praat_tg, get_recording_length, json_read


class SessionRecording(AbstractSessionAudio):

    def __init__(self, **kwargs):
        super(SessionRecording, self).__init__(**kwargs)

        self.data = DataProviderText(self.data_path)

        self.current_sentence_text = None
        self.current_sentence_id = None

        self.save()


    def update_current_data_item(self):
        sentence_text, sentence_id = self.data.item
        self.current_sentence_text = sentence_text
        self.current_sentence_id = sentence_id

        return self.current_sentence_text


    def item_save_path(self):
        return os.path.join(self.recordings_path, 'line-{}_sentid-{}_speaker-{}.wav'.format(
            self.data.index+1, self.current_sentence_id, self.speaker))


    def item_index(self, recording_name):
        return int(recording_name.split('_')[0].split('-')[-1])


    def get_missing_items(self):
        existing_recordings = [self.item_index(item) for item in self.list_recordings()]
        missing_indices = sorted([i for i in range(1,len(self.data)+1) if i not in existing_recordings], reverse=True)
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
                line_number = self.item_index(wav_file)
                sentence, _ = self.data[line_number-1]

                create_praat_tg(rec_length, sentence, self.textgrid_path, raw_filename)
                done += 1
        except:
            errors.append(wav_file)
        return done, errors