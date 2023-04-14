#!usr/bin/env python
# -*- coding: utf8 -*-
#
# -----------------------------------------------------------------------------
#   File: App.py (as part of project Williaikuma)
#   Created: 18/10/2022 04:20
#   Last Modified: 18/10/2022 04:20
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
import sys
import tkinter as tk
import gettext

from williaikuma import __version__
from williaikuma.controllers.Controller import Controller
from williaikuma.views.MainView import MainView
from williaikuma.models.Application import Application

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        application = Application(version=__version__)
        view = MainView(self)
        controller = Controller(application, view)
        view.set_controller(controller)
        self.title(application.name)


if __name__ == "__main__":
    # Set locale translations
    from locale import getlocale
    from babel import Locale

    try:
        wd = sys._MEIPASS
    except AttributeError:
        wd = os.getcwd()

    local_dir = os.path.join(wd, 'williaikuma','assets','locales')
    local_lang = Locale.parse(getlocale()[0]).language

    local_gettext = gettext.translation('base', localedir=local_dir, languages=[local_lang], fallback=True)
    local_gettext.install(names=['gettext'])

    # Start app
    app = App()
    app.mainloop()
