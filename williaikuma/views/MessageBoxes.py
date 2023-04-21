#!usr/bin/env python
# -*- coding: utf8 -*-
#
# -----------------------------------------------------------------------------
#   File: MainView.py (as part of project Williaikuma)
#   Created: 15/10/2022 18:11
#   Last Modified: 15/10/2022 18:11
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
import os.path
import tkinter as tk
import tkinter.simpledialog
import tkinter.filedialog
from tkinter import messagebox

from williaikuma.models.Messages import MSG


def action_open_file(initial_dir=os.path.expanduser('~'), file_type=['txt']):
    filetypes = tuple([(MSG.TEXT_FILES, "*.{}".format(ext)) for ext in file_type])
    return tk.filedialog.askopenfilename(initialdir=initial_dir,
                                         title=MSG.TITLE_CHOOSE_FILE,
                                         filetypes=filetypes)


def action_prompt(title, message):
    return tk.simpledialog.askstring(title, message)


def action_error(title, message):
    return tk.messagebox.showerror(title, message)


def action_notify(title, message):
    return tk.messagebox.showinfo(title, message)


def action_choose_dir(initial_dir=os.path.expanduser('~')):
    return tk.filedialog.askdirectory(initialdir=initial_dir)


def action_yes_no(title, message):
    return tk.messagebox.askyesno(title, message, default="no")


def action_yes_no_cancel(title, message):
    return tk.messagebox.askyesnocancel(title, message, default="cancel")