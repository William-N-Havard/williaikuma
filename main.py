#!usr/bin/env python
# -*- coding: utf8 -*-

import sys
import faulthandler

from App import App

if __name__ == "__main__":
    faulthandler.enable(file=sys.stderr, all_threads=True)

    app = App()
    app.mainloop()
