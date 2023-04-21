#!usr/bin/env python
# -*- coding: utf8 -*-
#
# -----------------------------------------------------------------------------
#   File: Controller.py (as part of project Williaikuma)
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
import shutil

import williaikuma
from williaikuma.models.Messages import MSG
from williaikuma.models.Tasks import TASKS
from williaikuma.models.utils import assert_recording_exists
from williaikuma.models.Application import Application
from williaikuma.audio.ThreadedAudio import ThreadedRecorder, ThreadedPlayer
from williaikuma.views.MainView import MainView
from williaikuma.views import MessageBoxes
from williaikuma.consts import project_dirs
from williaikuma.controllers.utils import generate_session_path, get_parent_dir, select_writable_dir

class Controller(object):

    def __init__(self, model: Application, view: MainView):
        # Model
        self.model: Application = model

        # View
        self.view: MainView = view

        # Audio
        self.recorder = None
        self.player = None

        self._recording_status = False
        self._playing_status = False
        self._respeak_playing_status = False

        self.__init_view__()

    def __init_view__(self):
        self.view.root.title(self.model.name)
        self.view.populate_recent(self.model.recent_sessions)
        self.view.populate_locale(self.model.get_locales())

    def start(self):
        try:
            self.model.session_start()
        except Exception as e:
            logging.exception(e)
            msg = MSG.ERROR_UNABLE_SESSION_START.format(str(e) if str(e) in MSG.values() else '')

            MessageBoxes.action_error(MSG.TITLE_ERROR, msg)
            return

        self.command_next()
        self.view.enable_directional_buttons()

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
            self.view.disable_recording()
            self.view.update_recording_on()
            self.view.enable_directional_buttons()
        else:
            self.view.enable_recording()
            self.view.update_recording_off()
            self.view.disable_directional_buttons()


    @property
    def playing_status(self):
        return self._playing_status


    @playing_status.setter
    def playing_status(self, value):
        self._playing_status = value
        if self.playing_status == False:
            self.view.enable_plays()
            self.view.update_play_on()
        else:
            self.view.disable_plays()
            self.view.update_play_off()


    @property
    def respeak_playing_status(self):
        return self._respeak_playing_status


    @playing_status.setter
    def respeak_playing_status(self, value):
        self._respeak_playing_status = value
        if self._respeak_playing_status == False:
            self.view.enable_plays()
            self.view.update_play_respeak_on()
        else:
            self.view.disable_plays()
            self.view.update_play_respeak_off()

    #
    #   Menu Commands
    #
    def command_version(self):
        MessageBoxes.action_notify(MSG.TITLE_INFORMATION, MSG.TEXT_VERSION.format(williaikuma.__version__,
                                                                                  williaikuma.__author__,
                                                                                  williaikuma.__email__))


    def command_new(self, task):
        #
        # Prompt for data
        #
        data_path = MessageBoxes.action_open_file(initial_dir=self.model.recent_path_data,
                                                  file_type=task.extensions)
        if not data_path: return
        # Update recent path
        self.model.recent_path_data = os.path.split(data_path)[0]

        #
        # Prompt for session dir
        #
        yes_no = MessageBoxes.action_yes_no(MSG.TITLE_INFORMATION,
                                            MSG.TEXT_SESSION_PATH.format(self.model.session_path))

        # User wants to change directory
        if yes_no:
            session_root_dir = select_writable_dir(initial_dir=get_parent_dir(self.model.session_path))
        else:
            session_root_dir = self.model.session_path

        #
        # Prompt for speaker
        #
        speaker = MessageBoxes.action_prompt(MSG.TITLE_INFORMATION, MSG.TEXT_PROMPT_SPEAKER)
        if not speaker: return

        # Generate session directory
        data_source_filename = os.path.basename(data_path)
        session_path, session_name = generate_session_path(data_path, task, speaker, session_root_dir)

        # Create directory
        session_dirs = project_dirs(session_path)
        for p in session_dirs:
            os.makedirs(p)

        # From now on, session sentences will be stored inside the session directory
            # First copy file
        shutil.copyfile(data_path, os.path.join(session_path, 'data', data_source_filename))
            # Then, make its path relative to the session's path
        data_path = os.path.join('.', 'data', data_source_filename)

        try:
            self.model.session_init(name=session_name, path=session_path, data_path=data_path,
                                    speaker=speaker, task=task)
            self.start()
        except Exception as e:
            logging.exception(e)
            msg = MSG.ERROR_UNABLE_CREATE_SESSION.format(str(e) if str(e) in MSG.values() else '')

            MessageBoxes.action_error(MSG.TITLE_ERROR, msg)


    def command_open(self):
        session = MessageBoxes.action_open_file(initial_dir=self.model.session_path,
                                                file_type=['json'])
        if not session: return

        try:
            self.model.session_load(session)
            self.start()
        except Exception as e:
            logging.exception(e)
            msg = MSG.ERROR_UNABLE_OPEN_SESSION.format(str(e) if str(e) in MSG.values() else '')

            MessageBoxes.action_error(MSG.TITLE_ERROR, msg)


    def command_recent_open(self, session):
        try:
            self.model.session_load(session)
            self.start()
        except Exception as e:
            logging.exception(e)
            msg = MSG.ERROR_UNABLE_OPEN_SESSION.format(str(e) if str(e) in MSG.values() else '')

            MessageBoxes.action_error(MSG.TITLE_ERROR, msg)


    def command_generate_textgrid(self):
        try:
            generated, failures = self.model.session.generate_textgrids()
            MessageBoxes.action_notify(MSG.TITLE_INFORMATION, MSG.TEXT_INFORMATION_GENERATE_TEXTGRID.format(
                generated, len(failures), '\n'.join(failures)
            ))
        except Exception as e:
            logging.exception(e)
            MessageBoxes.action_error(MSG.TITLE_ERROR, MSG.ERROR_UNABLE_GENERATE_TEXTGRID)

    #
    #   Recording Panel Commands
    #
    def command_next(self):
        self.model.session.next()
        self.view_update()


    def command_previous(self):
        self.model.session.previous()
        self.view_update()


    def command_record(self):
        try:
            if self.recording_status:
                self.recorder.stop()
                self.recorder.join()
                del self.recorder

                self.recording_status = False
                self.model.session.recordings_done += 1
            else:
                self.recording_status = True
                self.recorder = ThreadedRecorder(self.model.session.item_save_path(),
                                                 sampling_rate=self.model.session.sampling_rate,
                                                 num_channels=self.model.session.num_channels)
                self.recorder.start()
        except Exception as e:
            try:
                self.recorder.join()
                del self.recorder
            except:
                del self.recorder

            self.recording_status = False

            logging.exception(e)
            MessageBoxes.action_error(MSG.TITLE_ERROR, MSG.ERROR_UNKNOWN)
            self.view.enable_directional_buttons()

        self.view_update()


    def command_listen(self):
        self._listen(self.model.session.item_save_path())


    def command_listen_respeak(self):
        self._listen(self.model.session.current_sentence_recording, which='respeak')


    def command_delete(self):
        yes_no = MessageBoxes.action_yes_no(MSG.TITLE_DELETE, MSG.TEXT_PROMPT_DELETE_RECORDING)
        if not yes_no: return

        if assert_recording_exists(self.model.session.item_save_path()):
            os.remove(self.model.session.item_save_path())
            self.model.session.recordings_done -= 1
        self.view_update()


    def command_select_session_directory(self):
        new_dir = MessageBoxes.action_choose_dir(self.model.session_path)
        if not new_dir: return

        self.model.session_path = new_dir

    def command_reset_recent(self):
        yes_no = MessageBoxes.action_yes_no(MSG.TITLE_DELETE, MSG.TEXT_PROMPT_DELETE_RECORDING)
        if not yes_no: return

        self.view_refresh_recent()

    def set_locale(self, lang_code):
        original_lang = self.model.get_lang()
        self.model.set_locale(lang_code)

        yes_no_cancel = MessageBoxes.action_yes_no_cancel(MSG.TITLE_INFORMATION, MSG.TEXT_PROMPT_CHANGE_LOCALE)

        # If cancel, restore old language
        if yes_no_cancel == None:
            self.model.set_locale(original_lang)
            return

        # Restart?
        if yes_no_cancel: self.view.root.restart()

    def command_view_missing(self):
        missing_items = self.model.session.get_missing_items()
        selected_missing_item = self.view.show_missing(missing_items=missing_items)
        if selected_missing_item:
            self.model.session.override_index(selected_missing_item)
        self.view_update()

    #
    #   Private methods
    #
    def _listen(self, item, which=''):
        self.view.disable_play()
        self.view.disable_delete()
        try:
            setattr(self, '{}playing_status'.format('{}_'.format(which) if which else ''), True)
            self.player = ThreadedPlayer(item)
            self.player.start()
            self.player.join()
            del self.player
        except Exception as e:
            logging.exception(e)
            MessageBoxes.action_error(MSG.TITLE_ERROR, MSG.ERROR_UNABLE_READ_RECORDING)

        setattr(self, '{}playing_status'.format('{}_'.format(which) if which else ''), False)
        self.view_update()

    #
    #   GUI refreshers
    #
    def view_update(self):
        self.view.enable_menu_data_missing()
        if self.model.session.task == TASKS.TEXT_ELICITATION:
            self.view_text_elicitation_update()
        elif self.model.session.task == TASKS.RESPEAKING:
            self.view_respeaking_update()
        else:
            ValueError(MSG.EXCEPT_UNKNOWN_TASK.format(self.model.session.task))


    def view_respeaking_update(self):
        # Hide/Show widgets
        self.view.hide_widget(self.view.Label_Sentence)
        self.view.show_widget(self.view.Button_Listen_Respeak)

        # Update labels
        self.view.set_label_sentence_id(self.model.session.current_sentence_recording_name)
        self.view.set_label_progress(self.model.session.recordings_done, len(self.model.session.data))
        self.view.set_status_bar(self.model.session.index + 1, self.model.session.speaker, self.model.session.name)
        self.view.enable_play_respeak()

        if self.model.session.recordings_done > 0:
            self.view.enable_menu_data_generate_textgrid()
        self.view_audio_session_player_switch()


    def view_text_elicitation_update(self):
        # Hide/Show widgets
        self.view.hide_widget(self.view.Button_Listen_Respeak)
        self.view.show_widget(self.view.Label_Sentence)

        # Update labels
        self.view.set_label_sentence_text(self.model.session.current_sentence_text)
        self.view.set_label_sentence_id(self.model.session.current_sentence_id)
        self.view.set_label_progress(self.model.session.recordings_done, len(self.model.session.data))
        self.view.set_status_bar(self.model.session.index + 1, self.model.session.speaker, self.model.session.name)

        if self.model.session.recordings_done > 0:
            self.view.enable_menu_data_generate_textgrid()
        self.view_audio_session_player_switch()


    def view_audio_session_player_switch(self):
        if not assert_recording_exists(self.model.session.item_save_path()):
            self.view.enable_recording()
            self.view.disable_play()
            self.view.disable_delete()
        else:
            self.view.disable_recording()
            self.view.enable_play()
            self.view.enable_delete()

    def view_refresh_recent(self):
        self.view.reset_recent_menu()
        self.view.populate_recent(self.model.recent_sessions)
