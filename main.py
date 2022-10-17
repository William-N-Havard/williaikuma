#!usr/bin/env python
# -*- coding: utf8 -*-


import tkinter as tk

from controllers.Controller import Controller
from views.interface import App


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root=root)
    app.controller = Controller(app)
    root.mainloop()
