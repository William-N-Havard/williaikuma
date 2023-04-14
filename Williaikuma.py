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
    from babel import default_locale, Locale

    local_lang = Locale.parse(default_locale('LC_MESSAGES')).language
    local_dir = os.path.join('williaikuma','assets','locales')
    try:
        local_gettext = gettext.translation('base', localedir=local_dir, languages=[local_lang])
    except:
        local_gettext = gettext.translation('base', localedir=local_dir, languages=['en'])

    local_gettext.install(names=['gettext'])

    app = App()
    app.mainloop()
