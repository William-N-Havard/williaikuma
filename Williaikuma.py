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

from williaikuma.controllers.Controller import Controller
from williaikuma.views.MainView import MainView
from williaikuma.models.Application import Application

class App(tk.Tk):
    def __init__(self, wrapper):
        super().__init__()

        self.wrapper = wrapper

        # Get main model and set locale
        self.model = Application()
        # Get View
        view = MainView(self)
        # Get controller
        controller = Controller(self.model, view)
        # Attach controler to view
        view.set_controller(controller)

    def restart(self):
        self.wrapper.restart = True
        self.destroy()


class AppWrapper:
    def __init__(self):
        self.app = App
        self.restart = True

    def run(self):
        while self.restart:
            if self.restart: self.restart = False

            # Run app
            app = self.app(self)
            app.mainloop()
            # Save state on exit
            try:
                app.model.save()
            except:
                pass


if __name__ == "__main__":
    # Start app
    app = AppWrapper()
    app.run()
