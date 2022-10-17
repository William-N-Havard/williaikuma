#!usr/bin/env python
# -*- coding: utf8 -*-
#
# -----------------------------------------------------------------------------
#   File: Controller.py (as part of project noname.py)
#   Created: 16/10/2022 17:06
#   Last Modified: 16/10/2022 17:06
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
from datetime import datetime

from models.Session import Session
from views.interface import App
from audio.ThreadedAudio import ThreadedRecorder, ThreadedPlayer
from models.utils import assert_recording_exists, json_read, json_dump


class Controller(object):

    def __init__(self, gui):
        # View
        self.gui: App = gui

        # Model
        self.session = None

        # Audio
        self.recorder = None
        self.player = None

        self._recording_status = False
        self._playing_status = False

        # Other
        self._config_file = '../.williaikuma.json'
        self.config = self._read_config()
        self.session_path = self.config.get('sentence_path', os.path.realpath('sessions'))

        self.gui.populate_recent(self.config['recent'])

    def start(self):
        self._update_app_config(recent=self.session)

        try:
            self.session.start()
        except Exception as e:
            self.gui.dialog_error('Error!', str(e))
            return

        self.next()
        self.gui.enable_directional_buttons()
        self.gui.set_status_bar(self.session.speaker, self.session.name)


    def next(self):
        self.session.next()
        self._update_sentence()


    def previous(self):
        self.session.previous()
        self._update_sentence()


    def record(self):
        if self.recording_status:
            self.recorder.stop()
            self.recording_status = False
            self.session.recordings_done += 1
        else:
            self.recording_status = True
            self.recorder = ThreadedRecorder(self.session.get_current_sentence_recording_path(),
                                             sampling_rate=self.session.sampling_rate,
                                             num_channels=self.session.num_channels)
            self.recorder.start()
        self._update_sentence()


    def listen(self):
        try:
            self.playing_status = True
            self.gui.disable_play()
            self.player = ThreadedPlayer(self.session.get_current_sentence_recording_path())
            self.player.start()
            self.player.join()
        except Exception as e:
            self.gui.dialog_error('Error!', 'Hube un problema con esta grabación!')

        self.playing_status = False
        self._update_sentence()


    def delete(self):
        if assert_recording_exists(self.session.get_current_sentence_recording_path()):
            os.remove(self.session.get_current_sentence_recording_path())
            self.session.recordings_done -= 1
        self._update_sentence()

    def select_default_session_directory(self):
        new_dir = self.gui.dialog_chose_dir(os.path.realpath(self.session_path))
        if not new_dir: return

        self.session_path = new_dir
        self._update_app_config(sentence_path=new_dir)

    # Refresh GUI
    def _update_sentence(self):
        self.gui.set_label_sentence_text(self.session.current_sentence_text)
        self.gui.set_label_sentence_id(self.session.current_sentence_id)
        self.gui.set_label_progress(self.session.recordings_done, len(self.session.data))

        if not assert_recording_exists(self.session.get_current_sentence_recording_path()):
            self.gui.enable_recording()
            self.gui.disable_play()
            self.gui.disable_delete()
        else:
            self.gui.disable_recording()
            self.gui.enable_play()
            self.gui.enable_delete()


    def _read_config(self):
        if not os.path.exists(self._config_file):
            json_dump(self._config_file, {
                    "recent": []
                })

        config = json_read(self._config_file)
        config['recent'] = [(a,b) for a,b in config['recent'] if os.path.exists(b)]
        json_dump(self._config_file, config)
        
        return config

    def _update_app_config(self, **kwargs):
        config = self.config
        for k, v in kwargs.items():
            if k == "recent":
                config.setdefault(k, [])
                recent = [v.name, v.session_metadata_path]
                if recent not in config[k]:
                    config[k].insert(0, recent)
                config[k] = config[k][:5]
            else:
                config[k] = v
        json_dump(self._config_file, config)

    #
    #   Properties
    #
    @property
    def recording_status(self):
        return self._recording_status

    @recording_status.setter
    def recording_status(self, value):
        self._recording_status = value
        if self.recording_status == False:
            self.gui.disable_recording()
            self.gui.update_recording_on()
        else:
            self.gui.enable_recording()
            self.gui.update_recording_off()

    @property
    def playing_status(self):
        return self._playing_status

    @playing_status.setter
    def playing_status(self, value):
        self._playing_status = value
        if self.playing_status == False:
            self.gui.enable_play()
            self.gui.update_play_on()
        else:
            self.gui.disable_play()
            self.gui.update_play_off()

    #
    #   Handle Sessions
    #
    def new(self):
        data_path = self.gui.dialog_open_file(file_type='txt')
        if not data_path: return

        speaker = self.gui.dialog_prompt()
        if not speaker: return

        # Generate session directory
        datetime_now = datetime.now().strftime("%d%m%Y_%H%M%S")
        data_source_filename = os.path.basename(os.path.splitext(data_path)[0])

        session_name = 'session_{}_{}_{}'.format(speaker, data_source_filename, datetime_now)
        session_path = os.path.join(self.session_path, session_name)
        os.makedirs(session_path)

        self.session = Session(name=session_name, path=session_path, data_path=data_path, speaker=speaker)
        self.start()


    def open(self):
        session_path = self.gui.dialog_open_file(initial_dir=self.session_path,
                                                 file_type='json')
        if not session_path: return

        try:
            self.session = Session.load(session_path)
            self.start()
        except:
            self.gui.dialog_error('Error!', "Couldn't open this session!")


    def direct_open(self, sess):
        try:
            self.session = Session.load(sess)
            self.start()
        except:
            self.gui.dialog_error('Error!', "Couldn't open this session!")