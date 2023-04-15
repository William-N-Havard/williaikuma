#!usr/bin/env python
# -*- coding: utf8 -*-
#
# -----------------------------------------------------------------------------
#   File: MainView.py (as part of project Williaikuma)
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

import tkinter as tk
import tkinter.font as tkFont
import tkinter.simpledialog
import tkinter.filedialog
from tkinter import PhotoImage, messagebox

import babel
from PIL import Image
from PIL.ImageTk import PhotoImage

from williaikuma.models.Messages import MSG
from williaikuma.models.Tasks import TASKS
from williaikuma.views.MissingView import MissingView
from williaikuma.views.utils import TkinterButtons as TkButtons

class MainView(tk.Frame):
    def __init__(self, root):
        super().__init__(root)

        self.root = root
        self.ctrl = None

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
        self.image_respeak_on = self.load_resized_image(TkButtons.BUTTON_RESPEAK.value)
        self.image_respeak_off = self.load_resized_image(TkButtons.BUTTON_PLAY_OFF.value)

        # Menus
        menu = tk.Menu(root)
        root.config(menu=menu)

        # File Menu
        fileMenu = tk.Menu(menu, tearoff=False)
        self.newMenu = tk.Menu(fileMenu, tearoff=0)
        self.newMenu.add_command(label=MSG.MENU_NEW_TEXT_ELICITATION, command=self.Menu_File_New_Text_commmand)
        self.newMenu.add_command(label=MSG.MENU_NEW_RESPEAKING, command=self.Menu_File_New_Respeak_command)
        fileMenu.add_cascade(label=MSG.MENU_NEW, menu=self.newMenu)
        fileMenu.add_command(label=MSG.MENU_OPEN, command=self.Menu_File_Open_commmand)
        fileMenu.add_separator()
        self.recent_menu = tk.Menu(fileMenu, tearoff=0)
        fileMenu.add_cascade(label=MSG.MENU_RECENT, menu=self.recent_menu)
        fileMenu.add_separator()
        fileMenu.add_command(label=MSG.MENU_EXIT, command=self.root.destroy)
        menu.add_cascade(label=MSG.MENU_FILE, menu=fileMenu)

        # Preference Menu
        dataMenu = tk.Menu(menu, tearoff=False)
        dataMenu.add_command(label=MSG.MENU_MISSING_ITEMS, state=tk.DISABLED,
                             command=self.Menu_Data_ViewMissing_Command)
        dataMenu.add_separator()
        dataMenu.add_command(label=MSG.MENU_GENERATE_TEXTGRID, state=tk.DISABLED,
                             command=self.Menu_Data_Generate_TextGrid_Command)
        self.dataMenu = dataMenu
        menu.add_cascade(label=MSG.MENU_DATA, menu=dataMenu)


        # Preference Menu
        preferenceMenu = tk.Menu(menu, tearoff=False)
        preferenceMenu.add_command(label=MSG.MENU_DEFAULT_SESSION_DIR, command=self.Menu_Preference_Session_command)
        menu.add_cascade(label=MSG.MENU_PREFERENCES, menu=preferenceMenu)

        # Language selection
        self.locale_menu = tk.Menu(preferenceMenu, tearoff=0)
        preferenceMenu.add_cascade(label=MSG.MENU_LANGUAGE, menu=self.locale_menu)

        Button_Record=tk.Button(root, state = tk.DISABLED, image=self.image_record_on)
        Button_Record["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        Button_Record["font"] = ft
        Button_Record["fg"] = "#000000"
        Button_Record["justify"] = "center"
        Button_Record["text"] = MSG.BUTTON_RECORD
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
        Button_Delete["text"] = MSG.BUTTON_DETELE
        Button_Delete.place(x=120,y=120,width=320,height=60)
        Button_Delete["command"] = self.Button_Delete_Command
        self.Button_Delete = Button_Delete

        Button_Listen=tk.Button(root, state = tk.DISABLED, image=self.image_play_on)
        Button_Listen["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        Button_Listen["font"] = ft
        Button_Listen["fg"] = "#000000"
        Button_Listen["justify"] = "center"
        Button_Listen["text"] = MSG.BUTTON_PLAY
        Button_Listen.place(x=0,y=0,width=560,height=60)
        Button_Listen["command"] = self.Button_Listen_Command
        self.Button_Listen = Button_Listen

        Button_Listen_Respeak = tk.Button(root, state=tk.DISABLED, image=self.image_respeak_on)
        Button_Listen_Respeak["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        Button_Listen_Respeak["font"] = ft
        Button_Listen_Respeak["fg"] = "#000000"
        Button_Listen_Respeak["justify"] = "center"
        Button_Listen_Respeak["text"] = MSG.BUTTON_RESPEAK
        Button_Listen_Respeak.place(x=0,y=220,width=560,height=230)
        Button_Listen_Respeak["command"] = self.Button_Listen_Respeak_Command
        self.Button_Listen_Respeak = Button_Listen_Respeak
        self.hide_widget(Button_Listen_Respeak)


        Label_ID=tk.Label(root, wraplength=380)
        ft = tkFont.Font(family='Times',size=15)
        Label_ID["font"] = ft
        Label_ID["fg"] = "#333333"
        Label_ID["justify"] = "center"
        Label_ID["text"] = ""
        Label_ID.place(x=0,y=180,width=380,height=30)
        self.Label_ID = Label_ID

        Label_Progress = tk.Label(root)
        ft = tkFont.Font(family='Times', size=15)
        Label_Progress["font"] = ft
        Label_Progress["fg"] = "#333333"
        Label_Progress["justify"] = "center"
        Label_Progress["text"] = ""
        Label_Progress.place(x=380, y=180, width=180, height=30)
        self.Label_Progress = Label_Progress

        Label_Sentence=tk.Label(root, wraplength=560)
        ft = tkFont.Font(family='latin modern roman',size=25)
        Label_Sentence["font"] = ft
        Label_Sentence["fg"] = "#333333"
        Label_Sentence["justify"] = "center"
        Label_Sentence["text"] = MSG.TEXT_EXPLANATION
        Label_Sentence.place(x=0,y=205,width=560,height=230)
        self.Label_Sentence = Label_Sentence

        statusbar = tk.Label(root, text=MSG.STATUS_WAITING, bd=1, relief=tk.SUNKEN, anchor=tk.W)
        statusbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.statusbar = statusbar

        self.reset_recent_menu()

    @property
    def controller(self):
        return self.ctrl

    @controller.setter
    def controller(self, controller):
        self.ctrl = controller


    #
    #   Event method
    #
    def Menu_File_New_Text_commmand(self):
        self.ctrl.command_new(task=TASKS.TEXT_ELICITATION)


    def Menu_File_New_Respeak_command(self):
        self.ctrl.command_new(task=TASKS.RESPEAKING)


    def Menu_File_Open_commmand(self):
        self.ctrl.command_open()


    def Menu_Data_Generate_TextGrid_Command(self):
        self.ctrl.command_generate_textgrid()


    def Menu_Preference_Session_command(self):
        self.ctrl.command_select_session_directory()


    def Menu_Recent_Reset_command(self):
        self.ctrl.command_reset_recent()


    def Menu_Data_ViewMissing_Command(self):
        self.ctrl.command_view_missing()

    def Button_Previous_command(self):
        self.ctrl.command_previous()


    def Button_Record_command(self):
        self.ctrl.command_record()


    def Button_Next_command(self):
        self.ctrl.command_next()


    def Button_Delete_Command(self):
        self.ctrl.command_delete()


    def Button_Listen_Command(self):
        self.ctrl.command_listen()


    def Button_Listen_Respeak_Command(self):
        self.ctrl.command_listen_respeak()

    #
    # Update widgets (ugly but it works)
    #
    def set_label_sentence_text(self, sentence):
        self.Label_Sentence['text'] = sentence


    def set_label_sentence_id(self, sentence):
        self.Label_ID['text'] = sentence


    def set_label_progress(self, done, total):
        self.Label_Progress['text'] = '{}/{}'.format(done, total)


    def set_status_bar(self, index, speaker, session):
        self.statusbar['text'] = MSG.STATUS_SESSION.format(index, speaker, session)


    def enable_directional_buttons(self):
        self.enable_widget(self.Button_Previous)
        self.enable_widget(self.Button_Next)


    def enable_recording(self):
        self.enable_widget(self.Button_Record)


    def enable_play(self):
        self.enable_widget(self.Button_Listen)


    def enable_delete(self):
        self.enable_widget(self.Button_Delete)


    def enable_play_respeak(self):
        self.enable_widget(self.Button_Listen_Respeak)


    def enable_menu_data_generate_textgrid(self):
        self.dataMenu.entryconfig(2, state=tk.NORMAL)


    def disable_menu_data_generate_textgrid(self):
        self.dataMenu.entryconfig(2, state=tk.DISABLED)


    def enable_menu_data_missing(self):
        self.dataMenu.entryconfig(0, state=tk.NORMAL)


    def disable_menu_data_missing(self):
        self.dataMenu.entryconfig(0, state=tk.DISABLED)


    def disable_recording(self):
        self.disable_widget(self.Button_Record)


    def disable_play(self):
        self.disable_widget(self.Button_Listen)


    def disable_play_respeak(self):
        self.disable_widget(self.Button_Listen_Respeak)


    def disable_delete(self):
        self.disable_widget(self.Button_Delete)


    def disable_plays(self):
        self.disable_widget(self.Button_Listen)
        self.disable_widget(self.Button_Listen_Respeak)


    def enable_plays(self):
        self.enable_widget(self.Button_Listen)
        self.enable_widget(self.Button_Listen_Respeak)

    #
    #   Button image update
    #
    def update_recording_on(self):
        self.update_widget_image(self.Button_Record, self.image_record_on)


    def update_recording_off(self):
        self.update_widget_image(self.Button_Record, self.image_record_off)


    def update_play_on(self):
        self.update_widget_image(self.Button_Listen, self.image_play_on)


    def update_play_off(self):
        self.update_widget_image(self.Button_Listen, self.image_play_off)


    def update_play_respeak_on(self):
        self.update_widget_image(self.Button_Listen_Respeak, self.image_respeak_on)


    def update_play_respeak_off(self):
        self.update_widget_image(self.Button_Listen_Respeak, self.image_respeak_off)


    def populate_recent(self, recents):
        if recents:
            for idx, (recent_name, recent_path) in enumerate(recents, 1):
                self.recent_menu.insert_command(
                        index=idx,
                        label=recent_name,
                        command=lambda path=recent_path: self.ctrl.command_recent_open(path))

            if (idx_to_del:=self.recent_menu.index(MSG.MENU_NONE)) != None:\
                self.recent_menu.delete(idx_to_del)

            self.recent_menu.entryconfigure(self.recent_menu.index(MSG.MENU_RESET),
                                            state=tk.NORMAL)
        else:
            self.reset_recent_menu()

    def reset_recent_menu(self):
        while (last_index := self.recent_menu.index(tk.END)) != None:
            self.recent_menu.delete(last_index)

        self.recent_menu.add_command(label=MSG.MENU_NONE, state=tk.DISABLED)
        self.recent_menu.add_separator()
        self.recent_menu.add_command(label=MSG.MENU_RESET, state=tk.DISABLED, command=self.Menu_Recent_Reset_command)


    def populate_locale(self, locales):
        if locales:
            for idx, lang_code in enumerate(locales, 1):
                try:
                    lang_name = babel.Locale.parse(lang_code).get_language_name()
                except:
                    lang_name = lang_code

                self.locale_menu.insert_command(
                        index=idx,
                        label=lang_name,
                        command=lambda lc=lang_code: self.ctrl.set_locale(str(lc)))
                if idx == 1:
                    self.locale_menu.add_separator()

    #
    # Message boxes
    #
    def action_open_file(self, initial_dir ="/home/", file_type='txt'):
        return tkinter.filedialog.askopenfilename(initialdir=initial_dir,
                                                  title=MSG.TITLE_CHOOSE_FILE,
                                                  filetypes=((MSG.TEXT_FILES, "*.{}*".format(file_type)),))


    def action_prompt(self, title, message):
        return tk.simpledialog.askstring(title, message)


    def action_error(self, title, message):
        return tk.messagebox.showerror(title, message)


    def action_notify(self, title, message):
        return tk.messagebox.showinfo(title, message)


    def action_choose_dir(self, initial_dir ='/home/'):
        return tkinter.filedialog.askdirectory(initialdir=initial_dir)


    def action_yes_no(self, title, message):
        return tkinter.messagebox.askyesno(title, message, default="no")


    def show_missing(self, missing_items):
        selected_item = MissingView(self, missing_items=missing_items).show()
        return selected_item

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


    def hide_widget(self, widget):
        if not hasattr(widget, 'original_place'):
            setattr(widget, 'original_place', widget.place_info())

        if not hasattr(widget, 'visibility_status'):
            setattr(widget, 'visibility_status', 'visible')

        if getattr(widget, 'visibility_status') == 'visible':
            widget.place_forget()
            setattr(widget, 'visibility_status', 'hidden')
        # Otherwise the widget was already hidden

    def show_widget(self, widget):
        if not hasattr(widget, 'original_place'):
            setattr(widget, 'original_place', widget.place_info())

        if not hasattr(widget, 'visibility_status'):
            setattr(widget, 'visibility_status', 'hidden')

        if getattr(widget, 'visibility_status') == 'hidden':
            widget.place(**widget.original_place)
            setattr(widget, 'visibility_status', 'visible')


    def load_resized_image(self, path):
        image = Image.open(path)
        image = image.resize((50, 50), Image.ANTIALIAS)
        image = PhotoImage(image)
        return image


    def set_controller(self, controller):
        self.ctrl = controller
