#!usr/bin/env python
# -*- coding: utf8 -*-
#
# -----------------------------------------------------------------------------
#   File: interface.py (as part of project noname.py)
#   Created: 16/10/2022 18:11
#   Last Modified: 16/10/2022 18:11
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

import tkinter as tk
import tkinter.font as tkFont
import tkinter.simpledialog
import tkinter.filedialog
from tkinter import PhotoImage, messagebox
from PIL import Image
from PIL.ImageTk import PhotoImage


from views.utils import TkinterButtons as TkButtons

class App:
    def __init__(self, root):
        self.root = root
        self.ctrl = None

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
        self.image_record_on = self.load_resized_image(TkButtons.BUTTON_RECORD_ON.value)
        self.image_record_off = self.load_resized_image(TkButtons.BUTTON_RECORD_OFF.value)
        self.image_play_on = self.load_resized_image(TkButtons.BUTTON_PLAY_ON.value)
        self.image_play_off = self.load_resized_image(TkButtons.BUTTON_PLAY_OFF.value)
        self.image_left = self.load_resized_image(TkButtons.BUTTON_LEFT.value)
        self.image_right = self.load_resized_image(TkButtons.BUTTON_RIGHT.value)
        self.image_delete = self.load_resized_image(TkButtons.BUTTON_DELETE.value)

        # Menus
        menu = tk.Menu(root)
        root.config(menu=menu)
        fileMenu = tk.Menu(menu, tearoff=False)
        fileMenu.add_command(label="New", command=self.Menu_File_New_commmand)
        fileMenu.add_command(label="Open", command=self.Menu_File_Open_commmand)
        fileMenu.add_separator()
        self.recent_menu = tk.Menu(fileMenu, tearoff=0)
        self.recent_menu.add_command(label='None', state=tk.DISABLED)
        fileMenu.add_cascade(
            label="Recent",
            menu=self.recent_menu
        )
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=exit)
        menu.add_cascade(label="File", menu=fileMenu)


        Button_Record=tk.Button(root, state = tk.DISABLED, image=self.image_record_on)
        Button_Record["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        Button_Record["font"] = ft
        Button_Record["fg"] = "#000000"
        Button_Record["justify"] = "center"
        Button_Record["text"] = "Grabar"
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

        Button_Delete=tk.Button(root, state = tk.DISABLED, image=self.image_delete)
        Button_Delete["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        Button_Delete["font"] = ft
        Button_Delete["fg"] = "#000000"
        Button_Delete["justify"] = "center"
        Button_Delete["text"] = "Rechazar"
        Button_Delete.place(x=120,y=120,width=320,height=60)
        Button_Delete["command"] = self.Button_Delete_Command
        self.Button_Delete = Button_Delete

        Button_Listen=tk.Button(root, state = tk.DISABLED, image=self.image_play_on)
        Button_Listen["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        Button_Listen["font"] = ft
        Button_Listen["fg"] = "#000000"
        Button_Listen["justify"] = "center"
        Button_Listen["text"] = "Escuchar"
        Button_Listen.place(x=0,y=0,width=560,height=60)
        Button_Listen["command"] = self.Button_Listen_Command
        self.Button_Listen = Button_Listen

        Label_ID=tk.Label(root)
        ft = tkFont.Font(family='Times',size=15)
        Label_ID["font"] = ft
        Label_ID["fg"] = "#333333"
        Label_ID["justify"] = "center"
        Label_ID["text"] = ""
        Label_ID.place(x=0,y=180,width=280,height=25)
        self.Label_ID = Label_ID

        Label_Progress = tk.Label(root)
        ft = tkFont.Font(family='Times', size=15)
        Label_Progress["font"] = ft
        Label_Progress["fg"] = "#333333"
        Label_Progress["justify"] = "center"
        Label_Progress["text"] = ""
        Label_Progress.place(x=280, y=180, width=280, height=25)
        self.Label_Progress = Label_Progress

        Label_Sentence=tk.Label(root, wraplength=560)
        ft = tkFont.Font(family='latin modern roman',size=25)
        Label_Sentence["font"] = ft
        Label_Sentence["fg"] = "#333333"
        Label_Sentence["justify"] = "center"
        Label_Sentence["text"] = "Create a new project or open an existing one."
        Label_Sentence.place(x=0,y=205,width=560,height=245)
        self.Label_Sentence = Label_Sentence

        statusbar = tk.Label(root, text="Waiting...", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        statusbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.statusbar = statusbar

    @property
    def controller(self):
        return self.ctrl

    @controller.setter
    def controller(self, controller):
        self.ctrl = controller


    #
    #   Event method
    #
    def Menu_File_New_commmand(self):
        self.ctrl.new()


    def Menu_File_Open_commmand(self):
        self.ctrl.open()


    def Button_Previous_command(self):
        self.ctrl.previous()


    def Button_Record_command(self):
        self.ctrl.record()


    def Button_Next_command(self):
        self.ctrl.next()


    def Button_Delete_Command(self):
        self.ctrl.delete()


    def Button_Listen_Command(self):
        self.ctrl.listen()

    #
    # Update widgets (ugly but it works)
    #
    def set_label_sentence_text(self, sentence):
        self.Label_Sentence['text'] = sentence

    def set_label_sentence_id(self, sentence):
        self.Label_ID['text'] = sentence

    def set_label_progress(self, done, total):
        self.Label_Progress['text'] = '{}/{}'.format(done, total)

    def set_status_bar(self, speaker, session):
        self.statusbar['text'] = 'Speaker: {} | Session: {}'.format(speaker, session)

    def enable_directional_buttons(self):
        self.enable_widget(self.Button_Previous)
        self.enable_widget(self.Button_Next)

    def enable_recording(self):
        self.enable_widget(self.Button_Record)

    def enable_play(self):
        self.enable_widget(self.Button_Listen)

    def enable_delete(self):
        self.enable_widget(self.Button_Delete)

    def disable_recording(self):
        self.disable_widget(self.Button_Record)

    def disable_play(self):
        self.disable_widget(self.Button_Listen)

    def disable_delete(self):
        self.disable_widget(self.Button_Delete)

    def update_recording_on(self):
        self.update_widget_image(self.Button_Record, self.image_record_on)

    def update_recording_off(self):
        self.update_widget_image(self.Button_Record, self.image_record_off)

    def update_play_on(self):
        self.update_widget_image(self.Button_Listen, self.image_play_on)

    def update_play_off(self):
        self.update_widget_image(self.Button_Listen, self.image_play_off)

    def populate_recent(self, recents):
        for recent_name, recent_path in recents:
            print(recent_name, recent_path)
            self.recent_menu.add_command(label=recent_name,
                                         command=lambda path=recent_path: self.ctrl.direct_open(path))
            print(recent_name, recent_path)

        self.recent_menu.delete(0)
    #
    # Message boxes
    #
    def dialog_open_file(self, initial_dir = "/home/", file_type='txt'):
        return tkinter.filedialog.askopenfilename(initialdir=initial_dir,
                                   title="Elegir un archivo",
                                   filetypes=(("Files", "*.{}*".format(file_type)),))

    def dialog_prompt(self):
        return tk.simpledialog.askstring("Hablador?", "Quién está hablando?")


    def dialog_error(self, title, message):
        tk.messagebox.showerror(title, message)

    #
    #   Utility methods
    #
    def update_widget_image(self, widget, image):
        widget.configure(image=image)
        self.root.update()


    def enable_widget(self, widget):
        widget['state'] = tk.NORMAL


    def disable_widget(self, widget):
        widget['state'] = tk.DISABLED


    def load_resized_image(self, path):
        image = Image.open(path)
        image = image.resize((50, 50), Image.ANTIALIAS)
        image = PhotoImage(image)
        return image
