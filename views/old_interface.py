#!usr/bin/env python
# -*- coding: utf8 -*-
#
# -----------------------------------------------------------------------------
#   File: old_interface.py (as part of project noname.py)
#   Created: 16/10/2022 16:25
#   Last Modified: 16/10/2022 16:25
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
import tkinter as tk
import tkinter.font as tkFont
import tkinter.simpledialog
from tkinter import PhotoImage, messagebox
from PIL import Image
from PIL.ImageTk import PhotoImage
from datetime import datetime

from ThreadedAudio import ThreadedRecorder, ThreadedPlayer
from views.utils import TkinterButtons as TkButtons
from models.utils import text_read, assert_recording_exists
from consts import SAMPLING_RATE, NUM_CHANNELS

class App:
    def __init__(self, root, data_source, speaker):
        self.root = root
        self.data_source = data_source
        self.speaker = speaker

        root.title("Williaikuma")

        # Setting window size
        width=560
        height=440

        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.tk.call('encoding', 'system', 'utf-8')

        # Images
        self.image_record_on = self._load_image(TkButtons.BUTTON_RECORD_ON.value)
        self.image_record_off = self._load_image(TkButtons.BUTTON_RECORD_OFF.value)
        self.image_play_on = self._load_image(TkButtons.BUTTON_PLAY_ON.value)
        self.image_play_off = self._load_image(TkButtons.BUTTON_PLAY_OFF.value)
        self.image_left = self._load_image(TkButtons.BUTTON_LEFT.value)
        self.image_right = self._load_image(TkButtons.BUTTON_RIGHT.value)
        self.image_delete = self._load_image(TkButtons.BUTTON_DELETE.value)


        Button_Previous=tk.Button(root, state = tk.DISABLED, image=self.image_left)
        Button_Previous["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        Button_Previous["font"] = ft
        Button_Previous["fg"] = "#000000"
        Button_Previous["justify"] = "center"
        Button_Previous["text"] = "<-"
        Button_Previous.place(x=0,y=60,width=120,height=120)
        Button_Previous["command"] = self.Button_Previous_command
        self.Button_Previous = Button_Previous

        Button_Record=tk.Button(root, state = tk.DISABLED, image=self.image_record_on)
        Button_Record["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        Button_Record["font"] = ft
        Button_Record["fg"] = "#000000"
        Button_Record["justify"] = "center"
        Button_Previous["text"] = "Grabar"
        Button_Record.place(x=120,y=60,width=320,height=60)
        Button_Record["command"] = self.Button_Record_command
        self.Button_Record = Button_Record

        Button_Next=tk.Button(root, state = tk.DISABLED, image=self.image_right)
        Button_Next["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        Button_Next["font"] = ft
        Button_Next["fg"] = "#000000"
        Button_Next["justify"] = "center"
        Button_Next["text"] = "->"
        Button_Next.place(x=440,y=60,width=120,height=120)
        Button_Next["command"] = self.Button_Next_command
        self.Button_Next = Button_Next

        Button_Rechazar=tk.Button(root, state = tk.DISABLED, image=self.image_delete)
        Button_Rechazar["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        Button_Rechazar["font"] = ft
        Button_Rechazar["fg"] = "#000000"
        Button_Rechazar["justify"] = "center"
        Button_Rechazar["text"] = "Rechazar"
        Button_Rechazar.place(x=120,y=120,width=320,height=60)
        Button_Rechazar["command"] = self.Button_Rechazar_command
        self.Button_Rechazar = Button_Rechazar

        Button_Escuchar=tk.Button(root, state = tk.DISABLED, image=self.image_play_on)
        Button_Escuchar["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        Button_Escuchar["font"] = ft
        Button_Escuchar["fg"] = "#000000"
        Button_Escuchar["justify"] = "center"
        Button_Escuchar["text"] = "Escuchar"
        Button_Escuchar.place(x=0,y=0,width=560,height=60)
        Button_Escuchar["command"] = self.Button_Escuchar_command
        self.Button_Escuchar = Button_Escuchar

        Label_ID=tk.Label(root)
        ft = tkFont.Font(family='Times',size=15)
        Label_ID["font"] = ft
        Label_ID["fg"] = "#333333"
        Label_ID["justify"] = "center"
        Label_ID["text"] = "ID"
        Label_ID.place(x=0,y=180,width=280,height=25)
        self.Label_ID = Label_ID

        Label_Progress = tk.Label(root)
        ft = tkFont.Font(family='Times', size=15)
        Label_Progress["font"] = ft
        Label_Progress["fg"] = "#333333"
        Label_Progress["justify"] = "center"
        Label_Progress["text"] = "[##/##]"
        Label_Progress.place(x=280, y=180, width=280, height=25)
        self.Label_Progress = Label_Progress

        Label_Frase=tk.Label(root, wraplength=560)
        ft = tkFont.Font(family='latin modern roman',size=25)
        Label_Frase["font"] = ft
        Label_Frase["fg"] = "#333333"
        Label_Frase["justify"] = "center"
        Label_Frase["text"] = "Frase"
        Label_Frase.place(x=0,y=205,width=560,height=245)
        self.Label_Frase = Label_Frase

        self.data = self._load_file(self.data_source)
        self.sentence_index = 0
        self.sentence_id = None
        self.is_recording = False
        self.recorder = None
        self._recordings_done = 0

        self._start()


    def _load_image(self, path):
        image = Image.open(path)
        image = image.resize((50, 50), Image.ANTIALIAS)
        image = PhotoImage(image)
        return image


    def Button_Previous_command(self):
        self._previous()


    def Button_Record_command(self):
        self._record()


    def Button_Next_command(self):
        self._next()


    def Button_Rechazar_command(self):
        self._rechazar()


    def Button_Escuchar_command(self):
        self._listen()


    def _rechazar(self):
        if assert_recording_exists(self._get_recording_path()):
            os.remove(self._get_recording_path())
        self._change_sentence_button_update()
        self.recordings_done = self.recordings_done-1


    def _listen(self):
        self._disable(self.Button_Escuchar)
        self._change_image(self.Button_Escuchar, self.image_play_off)
        try:
            player = ThreadedPlayer(self._get_recording_path())
            player.start()
            player.join()
        except Exception as e:
            messagebox('Error!', 'Hube un problema con esta grabación!')

        self._change_image(self.Button_Escuchar, self.image_play_on)
        self._change_sentence_button_update()

    def _change_sentence_button_update(self):
        if os.path.exists(self._get_recording_path()):
            self._disable(self.Button_Record)
            self._enable(self.Button_Escuchar)
            self._enable(self.Button_Rechazar)
        else:
            self._enable(self.Button_Record)
            self._disable(self.Button_Rechazar)
            self._disable(self.Button_Escuchar)


    def _next(self):
        next_index = self.sentence_index + 1 if self.sentence_index < len(self.data) - 1 else 0
        self._set_sentence(next_index)
        self._change_sentence_button_update()


    def _previous(self):
        previous_index = self.sentence_index - 1 if self.sentence_index > 0 else len(self.data) - 1
        self._set_sentence(previous_index)
        self._change_sentence_button_update()


    def _record(self):
        if self.is_recording:
            self._change_image(self.Button_Record, self.image_record_on)
            self.recorder.stop()
            self.is_recording = False
            if not self.recorder.success:
                messagebox('Error!', 'Hube un problema con esta grabación!')
            else:
                self.recordings_done = self.recordings_done +1
        else:
            self._change_image(self.Button_Record, self.image_record_off)
            self.is_recording = True

            self.recorder = ThreadedRecorder(self._get_recording_path(),
                                             sampling_rate=SAMPLING_RATE, num_channels=NUM_CHANNELS)
            self.recorder.start()
        self._change_sentence_button_update()


    def _start(self):
        self._initiate_new_session()
        self._enable(self.Button_Next)
        self._enable(self.Button_Previous)
        self._set_sentence(self.sentence_index)
        self._change_sentence_button_update()
        self.recordings_done = 0


    def _initiate_new_session(self):
        datetime_value = datetime.now().strftime("%d%m%Y_%H%M%S")
        data_source_filename = os.path.basename(os.path.splitext(self.data_source)[0]).replace(' ', '_')
        session_path = 'session_{}_{}_{}'.format(self.speaker, data_source_filename, datetime_value)
        session_path = os.path.join('sessions', session_path)

        # Restore session ?
        already_existing_session = [item for item in os.listdir(os.path.join('sessions'))
                                    if item.startswith('session_{}_{}'.format(self.speaker, data_source_filename))]

        if already_existing_session and len(already_existing_session) == 1:
            continue_seesion = tkinter.messagebox.askyesno('Continuar?', 'Continuar ultima sesión?')
            if continue_seesion:
                self.session_path = already_existing_session[0]
                print(self.session_path)
                return

        # New session
        os.makedirs(session_path, exist_ok=True)
        self.session_path = session_path


    def _get_recording_path(self):
        return os.path.join('sessions', self.session_path,
                            'sentence_recording_{}_id-{}_line-{}.wav'.format(self.speaker,
                                                                             self.sentence_id,
                                                                             self.sentence_index+1))

    @property
    def recordings_done(self):
        return self._recording_done


    @recordings_done.setter
    def recordings_done(self, value):
        self._recording_done = max(0, value)
        self.Label_Progress['text'] ='{}/{}'.format(self.recordings_done, len(self.data))


    def _set_sentence(self, index):
        sent_text, sent_id = self.data[index].split('##')
        self.Label_Frase['text'] = sent_text.strip()
        self.Label_ID['text'] = sent_id.strip()
        self.sentence_index = index
        self.sentence_id = sent_id.rstrip('.')


    def _change_image(self, button, image):
        button.configure(image=image)
        self.root.update()


    def _enable(self, item):
        item['state'] = tk.NORMAL


    def _disable(self, item):
        item['state'] = tk.DISABLED


    def _load_file(self, file):
        data = list(text_read(file))
        return data
