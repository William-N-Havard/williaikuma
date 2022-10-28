#!usr/bin/env python
# -*- coding: utf8 -*-
#
# -----------------------------------------------------------------------------
#   File: MissingView.py (as part of project Williaikuma)
#   Created: 28/10/2022 02:43
#   Last Modified: 28/10/2022 02:43
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

class MissingView(tk.Toplevel):
    def __init__(self, parent, missing_items = []):
        super().__init__(parent)

        self.parent = parent
        self.missing_items = missing_items

        #setting title
        self.title("Missing Items")

        #setting window size
        width=250
        height=280

        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        Go_Button=tk.Button(self)
        Go_Button["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        Go_Button["font"] = ft
        Go_Button["fg"] = "#000000"
        Go_Button["justify"] = "center"
        Go_Button["text"] = "Go"
        Go_Button.place(x=0,y=250,width=125,height=30)
        Go_Button["command"] = self.Go_Button_command

        Cancel_Button=tk.Button(self)
        Cancel_Button["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        Cancel_Button["font"] = ft
        Cancel_Button["fg"] = "#000000"
        Cancel_Button["justify"] = "center"
        Cancel_Button["text"] = "Cancel"
        Cancel_Button.place(x=125,y=250,width=125,height=30)
        Cancel_Button["command"] = self.Cancel_Button_command

        Label_Missing_Items=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        Label_Missing_Items["font"] = ft
        Label_Missing_Items["fg"] = "#333333"
        Label_Missing_Items["justify"] = "center"
        Label_Missing_Items["text"] = "Missing items"
        Label_Missing_Items.place(x=0,y=0,width=250,height=25)

        Listbox_Missing_Items=tk.Listbox(self)
        Listbox_Missing_Items["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        Listbox_Missing_Items["font"] = ft
        Listbox_Missing_Items["fg"] = "#333333"
        Listbox_Missing_Items["justify"] = "center"
        Listbox_Missing_Items.place(x=0,y=25,width=250,height=225)
        Listbox_Missing_Items["selectmode"] = "single"
        self.Listbox_Missing_Items = Listbox_Missing_Items

        self.selected = []
        self.populate_listbox()


    def show(self):
        self.transient(self.parent)
        self.wait_visibility(self)
        self.grab_set()
        self.wait_window()
        return self.selected

    def Go_Button_command(self):
        selected = self.Listbox_Missing_Items.curselection()
        if selected:
            self.selected = self.Listbox_Missing_Items.get(selected)
        self.destroy()


    def Cancel_Button_command(self):
        self.destroy()


    def populate_listbox(self):
        for item in self.missing_items:
            self.Listbox_Missing_Items.insert(0, item)
