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

from williaikuma import __version__
from williaikuma.controllers.Controller import Controller
from williaikuma.views.MainView import MainView
from williaikuma.models.Application import Application

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Get main model and set locale
        model = Application(version=__version__)
        model.set_locale()
        # Get View
        view = MainView(self)
        # Get controller
        controller = Controller(model, view)
        # Attach controler to view
        view.set_controller(controller)
        # Set title
        self.title(model.name)


if __name__ == "__main__":
    # Start app
    app = App()
    app.mainloop()
