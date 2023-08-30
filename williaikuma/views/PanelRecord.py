#!usr/bin/env python
# -*- coding: utf8 -*-
#
# -----------------------------------------------------------------------------
#   File: PanelRecord.py (as part of project Williaikuma)
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

from williaikuma.views.utils import ImagesButtons


class PanelRecord (wx.Panel):

    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(-1,-1), style=wx.TAB_TRAVERSAL, name=wx.EmptyString):
        wx.Panel.__init__ (self, parent, id = id, pos = pos, size = size, style = style, name = name)

        record_panel_sizer = wx.BoxSizer(wx.VERTICAL)

        self.record_panel_inner = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        record_panel_inner_sizer = wx.BoxSizer(wx.VERTICAL)


        # Font changing buttons
        record_panel_inner_sizer_font_button = wx.BoxSizer(wx.HORIZONTAL)
        self.button_font_bigger = wx.Button(self.record_panel_inner, wx.ID_ANY, u"+", wx.DefaultPosition, wx.Size(30,30), 0)
        record_panel_inner_sizer_font_button.Add(self.button_font_bigger, 0, wx.ALIGN_TOP|wx.ALL, 5)

        self.button_font_lower = wx.Button(self.record_panel_inner, wx.ID_ANY, u"-", wx.DefaultPosition, wx.Size(30,30), 0)
        record_panel_inner_sizer_font_button.Add(self.button_font_lower, 0, wx.ALIGN_TOP|wx.ALL, 5)

        record_panel_inner_sizer.Add(record_panel_inner_sizer_font_button, 1, wx.ALIGN_RIGHT|wx.ALL|wx.TOP, 5)

        # Sentence
        record_panel_inner_sizer_sentence = wx.BoxSizer(wx.VERTICAL)
        record_panel_inner_sizer_sentence.Add((0, 0), 1, wx.EXPAND, 5)

        self.label_sentence = wx.StaticText(self.record_panel_inner, wx.ID_ANY, u"sentence", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL)
        self.label_sentence.Wrap(-1)

        record_panel_inner_sizer_sentence.Add(self.label_sentence, 1, wx.ALL|wx.EXPAND, 5)
        record_panel_inner_sizer_sentence.Add((0, 0), 1, wx.EXPAND, 5)
        record_panel_inner_sizer.Add(record_panel_inner_sizer_sentence, 1, wx.EXPAND, 5)

        # Statistics labels (num. done, sentence id)
        record_panel_inner_sizer_stats = wx.BoxSizer(wx.HORIZONTAL)

            # Num. Done
        self.label_progress = wx.StaticText(self.record_panel_inner, wx.ID_ANY, u"0/0", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL)
        self.label_progress.Wrap(-1)
        record_panel_inner_sizer_stats.Add(self.label_progress, 1, wx.ALIGN_BOTTOM|wx.ALL, 5)

            # Sentence ID
        self.label_sentence_id = wx.StaticText(self.record_panel_inner, wx.ID_ANY, u"sentence_id", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL)
        self.label_sentence_id.Wrap(-1)
        record_panel_inner_sizer_stats.Add(self.label_sentence_id, 1, wx.ALIGN_BOTTOM|wx.ALL, 5)
        
        record_panel_inner_sizer.Add(record_panel_inner_sizer_stats, 1, wx.EXPAND, 5)

        # Control buttons
        record_panel_inner_sizer_control = wx.BoxSizer(wx.VERTICAL)

            # Play buttons
        self.button_play = wx.BitmapToggleButton(self.record_panel_inner, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0)
        self.button_play.SetBitmap(ImagesButtons.BUTTON_PLAY_ON)
        self.button_play.SetBitmapPressed(ImagesButtons.BUTTON_PLAY_OFF)
        self.button_play.SetMinSize(wx.Size(500,-1))
        record_panel_inner_sizer_control.Add(self.button_play, 0, wx.ALL|wx.EXPAND, 5)

            # Previous/Record/Delete/Next
        control_middle_record_sizer = wx.BoxSizer(wx.HORIZONTAL)

                # Previous
        self.button_previous = wx.BitmapButton( self.record_panel_inner, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
        self.button_previous.SetBitmap(ImagesButtons.BUTTON_LEFT)
        control_middle_record_sizer.Add( self.button_previous, 0, wx.ALL|wx.EXPAND, 5 )

                # Record/Delete
        control_bottom_stats = wx.BoxSizer(wx.VERTICAL)

                    # Record
        self.button_record = wx.BitmapToggleButton(self.record_panel_inner, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0)
        self.button_record.SetBitmap(ImagesButtons.BUTTON_RECORD_ON)
        self.button_record.SetBitmapPressed(ImagesButtons.BUTTON_RECORD_OFF)
        control_bottom_stats.Add(self.button_record, 0, wx.ALL|wx.EXPAND, 5)

                    # Delete
        self.button_delete = wx.BitmapButton( self.record_panel_inner, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
        self.button_delete.SetBitmap(ImagesButtons.BUTTON_DELETE)
        control_bottom_stats.Add( self.button_delete, 0, wx.ALL|wx.EXPAND, 5 )

        control_middle_record_sizer.Add(control_bottom_stats, 1, 0, 5)

                # Next
        self.button_next = wx.BitmapButton( self.record_panel_inner, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
        self.button_next.SetBitmap(ImagesButtons.BUTTON_RIGHT)
        control_middle_record_sizer.Add( self.button_next, 0, wx.ALL|wx.EXPAND, 5 )

        record_panel_inner_sizer_control.Add(control_middle_record_sizer, 1, wx.EXPAND, 5)
        record_panel_inner_sizer.Add(record_panel_inner_sizer_control, 0, wx.ALIGN_CENTER, 5)

        # Add sizes
        self.record_panel_inner.SetSizer(record_panel_inner_sizer)
        self.record_panel_inner.Layout()
        record_panel_inner_sizer.Fit(self.record_panel_inner)
        record_panel_sizer.Add(self.record_panel_inner, 1, wx.EXPAND |wx.ALL, 5)


        self.SetSizer(record_panel_sizer)
        self.Layout()
        record_panel_sizer.Fit(self)

        # Connect Events
        self.button_font_bigger.Bind(wx.EVT_BUTTON, self.Button_Font_Bigger)
        self.button_font_lower.Bind(wx.EVT_BUTTON, self.Button_Font_Lower)
        self.button_play.Bind(wx.EVT_TOGGLEBUTTON, self.Button_Listen_Command)
        self.button_previous.Bind(wx.EVT_TOGGLEBUTTON, self.Button_Previous_command)
        self.button_record.Bind(wx.EVT_TOGGLEBUTTON, self.Button_Record_command)
        self.button_delete.Bind(wx.EVT_TOGGLEBUTTON, self.Button_Delete_Command)
        self.button_next.Bind(wx.EVT_TOGGLEBUTTON, self.Button_Next_command)

    def __del__(self):
        pass


    # Virtual event handlers, override them in your derived class
    def Button_Font_Bigger(self, event):
        event.Skip()

    def Button_Font_Lower(self, event):
        event.Skip()

    def Button_Listen_Command(self, event):
        event.Skip()

    def Button_Previous_command(self, event):
        event.Skip()

    def Button_Record_command(self, event):
        event.Skip()

    def Button_Delete_Command(self, event):
        event.Skip()

    def Button_Next_command(self, event):
        event.Skip()


