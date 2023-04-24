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
from williaikuma.models.DataProviderText import DataProviderText
from williaikuma.models.utils import create_praat_tg, get_recording_length, now_raw


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


    def item_recording_path(self):
        tentative_path = os.path.join(self.recordings_path,
                                      'line-{}_sentid-{}_speaker-{}_at-{}_v-{}.wav'.format(
                                          self.index+1,
                                          self.current_sentence_id,
                                          self.speaker,
                                          now_raw(),
                                          self.recording_retakes.get(self.index, 0) + 1,
                                        )
                                      )
        return self.recordings_list.get(self.index, tentative_path)


    def item_index_from_rec_name(self, recording_name):
        filepath, filename = os.path.split(recording_name)
        # '_' can be trusted here as ID will always be first
        return int(filename.split('_')[0].split('-')[-1])-1


    def item_retake_from_rec_name(self, recording_name):
        filepath, filename = os.path.split(recording_name)
        bare_filename, _ = os.path.splitext(filename)
        split_filename = bare_filename.split('_')

        # '_' CAN NOT be trusted here as sentid might contain "_"
        # find index of items that start with "v-" in split_filename and keep the last
        v_pos = [idx for idx, v in enumerate(split_filename) if v.startswith('v-')]
        max_v_pos = max(v_pos) if v_pos else -1
        if max_v_pos != -1:
            retake_num = int(split_filename[max_v_pos].split('-')[-1])
        else:
            retake_num = 1 # if this function is called, it means a recording was deleted
        return retake_num

    def get_missing_items(self):
        existing_recordings = [self.item_index_from_rec_name(item) for item in self.list_recordings()]
        missing_indices = sorted([i for i in range(0,len(self.data)) if i not in existing_recordings], reverse=True)
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
                sentence, _ = self.data[line_number]

                create_praat_tg(rec_length, sentence, self.textgrid_path, raw_filename)
                done += 1
        except:
            errors.append(wav_file)
        return done, errors