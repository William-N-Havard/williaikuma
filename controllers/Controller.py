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
import logging
import os
from datetime import datetime

from models.consts import TASKS
from models.sessions_utils import session_loader, session_initiator
from models.utils import assert_recording_exists, json_read, json_dump, now
from views.interface import MainView
from audio.ThreadedAudio import ThreadedRecorder, ThreadedPlayer


class Controller(object):

    def __init__(self, gui):
        # View
        self.gui: MainView = gui

        # Model
        self.session = None

        # Audio
        self.recorder = None
        self.player = None

        self._recording_status = False
        self._playing_status = False
        self._respeak_playing_status = False

        # Other
        self.app_config_file = '.williaikuma.json'
        self.app_config = self._read_config()
        self.session_path = self.app_config.get('session_path', os.path.realpath('sessions'))

        self.gui.populate_recent([(name, path) for name, path, *_ in self.app_config['recent']])


    def start(self):
        self._update_app_config(recent=self.session)

        try:
            self.session.start()
        except Exception as e:
            self.gui.action_error('Error!', str(e))
            return

        self.command_next()
        self.gui.enable_directional_buttons()
        self.gui.set_status_bar(self.session.index+1, self.session.speaker, self.session.name)

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
            self.gui.enable_plays()
            self.gui.update_play_on()
        else:
            self.gui.disable_plays()
            self.gui.update_play_off()


    @property
    def respeak_playing_status(self):
        return self._respeak_playing_status


    @playing_status.setter
    def respeak_playing_status(self, value):
        self._respeak_playing_status = value
        if self._respeak_playing_status == False:
            self.gui.enable_plays()
            self.gui.update_play_respeak_on()
        else:
            self.gui.disable_plays()
            self.gui.update_play_respeak_off()

    #
    #   Menu Commands
    #
    def command_new(self, task):
        ext = 'txt' if task == TASKS.TEXT_ELICITATION else 'json'
        data_path = self.gui.action_open_file(file_type=ext)
        if not data_path: return

        speaker = self.gui.action_prompt("Speaker?", "Enter speaker's name")
        if not speaker: return

        # Generate session directory
        datetime_now = now().replace(' ', '_').replace('/', '').replace(':', '')
        data_source_filename = os.path.basename(os.path.splitext(data_path)[0])

        session_name = '{}_session_{}_{}_{}'.format(
                        task.value, speaker, data_source_filename, datetime_now)
        session_path = os.path.join(self.session_path, session_name)
        os.makedirs(session_path)

        self.session = session_initiator(name=session_name, path=session_path, data_path=data_path,
                                         speaker=speaker, task=task)
        self.start()


    def command_open(self):
        session = self.gui.action_open_file(initial_dir=self.session_path,
                                            file_type='json')
        if not session: return

        try:
            self.session = session_loader(session)
            self.start()
        except Exception as e:
            logging.exception(e)
            self.gui.action_error('Error!', "Couldn't open this session!")


    def command_recent_open(self, session):
        try:
            self.session = session_loader(session)
            self.start()
        except Exception as e:
            logging.exception(e)
            self.gui.action_error('Error!', "Couldn't open this session!")


    def command_generate_textgrid(self):
        try:
            generated, failures = self.session.generate_textgrids()
            self.gui.action_notify('Information', 'Done! ({} generated, {} failures)\n'.format(
                generated, len(failures), '\n'.join(failures)
            ))
        except:
            self.gui.action_error('Error', 'There was a problem when generating the TextGrid files.')

    #
    #   Recording Panel Commands
    #
    def command_next(self):
        self.session.next()
        self.gui_update()


    def command_previous(self):
        self.session.previous()
        self.gui_update()


    def command_record(self):
        try:
            if self.recording_status:
                self.recorder.stop()
                self.recorder.join()
                del self.recorder

                self.recording_status = False
                self.session.recordings_done += 1
            else:
                self.recording_status = True
                self.recorder = ThreadedRecorder(self.session.item_save_path(),
                                                 sampling_rate=self.session.sampling_rate,
                                                 num_channels=self.session.num_channels)
                self.recorder.start()
        except Exception as e:
            self.gui.action_error("Error", "Unknown error!")

        self.gui_update()


    def command_listen(self):
        self._listen(self.session.item_save_path())


    def command_listen_respeak(self):
        self._listen(self.session.current_sentence_recording, which='respeak')


    def command_delete(self):
        yes_no = self.gui.action_yes_no("Delete", "Delete this recording?")
        if not yes_no: return

        if assert_recording_exists(self.session.item_save_path()):
            os.remove(self.session.item_save_path())
            self.session.recordings_done -= 1
        self.gui_update()


    def command_select_session_directory(self):
        new_dir = self.gui.action_choose_dir(os.path.realpath(self.session_path))
        if not new_dir: return

        self.session_path = new_dir
        self._update_app_config(session_path=new_dir)

    #
    #   Private methods
    #
    def _listen(self, item, which=''):
        try:
            setattr(self, '{}playing_status'.format('{}_'.format(which) if which else ''), True)
            self.gui.disable_play()
            self.player = ThreadedPlayer(item)
            self.player.start()
            self.player.join()
            del self.player
        except Exception as e:
            self.gui.action_error('Error!', 'There is a problem with this recording!')

        setattr(self, '{}playing_status'.format('{}_'.format(which) if which else ''), False)
        self.gui_update()

    #
    #   GUI refreshers
    #
    def gui_update(self):
        if self.session.task == TASKS.TEXT_ELICITATION:
            self.gui_text_elicitation_update()
        elif self.session.task == TASKS.RESPEAKING:
            self.gui_respeaking_update()
        else:
            ValueError('Unknown task type ``!'.format(self.session.task))


    def gui_respeaking_update(self):
        # Hide/Show widgets
        self.gui.hide_widget(self.gui.Label_Sentence)
        self.gui.show_widget(self.gui.Button_Listen_Respeak)

        # Update labels
        self.gui.set_label_sentence_id(self.session.current_sentence_recording_name)
        self.gui.set_label_progress(self.session.recordings_done, len(self.session.data))
        self.gui.set_status_bar(self.session.index+1, self.session.speaker, self.session.name)
        self.gui.enable_play_respeak()

        self.gui_audio_session_player_switch()


    def gui_text_elicitation_update(self):
        # Hide/Show widgets
        self.gui.hide_widget(self.gui.Button_Listen_Respeak)
        self.gui.show_widget(self.gui.Label_Sentence)

        # Update labels
        self.gui.set_label_sentence_text(self.session.current_sentence_text)
        self.gui.set_label_sentence_id(self.session.current_sentence_id)
        self.gui.set_label_progress(self.session.recordings_done, len(self.session.data))
        self.gui.set_status_bar(self.session.index+1, self.session.speaker, self.session.name)

        if self.session.recordings_done > 0:
            self.gui.enable_menu_data_generate_textgrid()
        self.gui_audio_session_player_switch()


    def gui_audio_session_player_switch(self):
        if not assert_recording_exists(self.session.item_save_path()):
            self.gui.enable_recording()
            self.gui.disable_play()
            self.gui.disable_delete()
        else:
            self.gui.disable_recording()
            self.gui.enable_play()
            self.gui.enable_delete()

    #
    #   Application configuration
    #
    def _read_config(self):
        if not os.path.exists(self.app_config_file):
            json_dump(self.app_config_file, {
                    "recent": []
                })

        config = json_read(self.app_config_file)
        config['recent'] = [[name, path, date] for name, path, date in config['recent'] if os.path.exists(path)]
        config['recent'] = list(sorted(config['recent'],
                                  key=lambda tup: datetime.strptime(tup[-1], "%d/%m/%Y %H:%M:%S"), reverse=True))
        json_dump(self.app_config_file, config)
        
        return config


    def _update_app_config(self, **kwargs):
        config = self.app_config
        for k, v in kwargs.items():
            if k == "recent":
                cur_sess = v
                config.setdefault(k, [])
                recent = [cur_sess.name, cur_sess.session_metadata_path, cur_sess.last_access]

                recent_names = [name for name, _, _ in config[k]]
                if cur_sess.name not in recent_names:
                    config[k].insert(0, recent)
                else:
                    idx = recent_names.index(cur_sess.name)
                    config[k][idx][-1] = cur_sess.last_access

                config[k] = sorted(config[k][:5],
                                   key=lambda tup: datetime.strptime(tup[-1], "%d/%m/%Y %H:%M:%S"), reverse=True)
            else:
                config[k] = v
        json_dump(self.app_config_file, config)
