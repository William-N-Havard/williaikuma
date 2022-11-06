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

import tkinter as tk

from __init__ import __version__
from controllers.Controller import Controller
from views.MainView import MainView
from models.Application import Application


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        application = Application(version=__version__)
        view = MainView(self)
        controller = Controller(application, view)
        view.set_controller(controller)
        self.title(application.name)
