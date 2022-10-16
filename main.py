#!usr/bin/env python
# -*- coding: utf8 -*-

import sys
import tkinter as tk
import tkinter.filedialog

from Controller import Controller
from views.interface import App

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root=root)
    controller = Controller(app)
    app.controller = controller
    root.mainloop()
