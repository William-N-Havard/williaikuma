#!usr/bin/env python
# -*- coding: utf8 -*-
#
# -----------------------------------------------------------------------------
#   File: PanelStart.py (as part of project Williaikuma)
#   Created: 17/05/2023 14:28
#   Last Modified: 17/05/2023 14:28
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

import wx
import wx.xrc

from williaikuma.models.Messages import MSG


class PanelStart(wx.Panel):
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(500,300), style=wx.TAB_TRAVERSAL, name=wx.EmptyString):

        wx.Panel.__init__ (self, parent, id=id, pos=pos, size=size, style=style, name=name)

        start_panel_sizer = wx.BoxSizer(wx.VERTICAL)
        start_panel_sizer.Add((0, 0), 1, wx.EXPAND, 5)

        self.label_start_message = wx.StaticText(self, wx.ID_ANY, MSG.TEXT_EXPLANATION, wx.DefaultPosition, wx.DefaultSize, 0)
        self.label_start_message.Wrap(-1)

        start_panel_sizer.Add(self.label_start_message, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.LEFT|wx.RIGHT, 5)
        start_panel_sizer.Add((0, 0), 1, wx.EXPAND, 5)

        self.SetSizer(start_panel_sizer)
        self.Layout()

    def __del__(self):
        pass

