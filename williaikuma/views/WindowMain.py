#!usr/bin/env python
# -*- coding: utf8 -*-
#
# -----------------------------------------------------------------------------
#   File: WindowMain.py (as part of project Williaikuma)
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

from williaikuma.views.PanelRecord import PanelRecord


class WindowMain(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__ (self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition, size=wx.Size(500,250), style=wx.DEFAULT_FRAME_STYLE|wx.MAXIMIZE|wx.MAXIMIZE_BOX|wx.TAB_TRAVERSAL)

        # Set up UI
        self.SetSizeHints(wx.Size(500,250), wx.DefaultSize)

        self.menubar = wx.MenuBar(0)
        self.menu_file = wx.Menu()
        self.menu_submenu_file_new = wx.Menu()
        self.menu_submenu_file_item_new_text_elicit = wx.MenuItem(self.menu_submenu_file_new, wx.ID_ANY, u"New Text Elicitation", wx.EmptyString, wx.ITEM_NORMAL)
        self.menu_submenu_file_new.Append(self.menu_submenu_file_item_new_text_elicit)

        self.menu_submenu_file_item_new_respeaking = wx.MenuItem(self.menu_submenu_file_new, wx.ID_ANY, u"Respeaking", wx.EmptyString, wx.ITEM_NORMAL)
        self.menu_submenu_file_new.Append(self.menu_submenu_file_item_new_respeaking)

        self.menu_file.AppendSubMenu(self.menu_submenu_file_new, u"New")

        self.menu_item_file_open = wx.MenuItem(self.menu_file, wx.ID_ANY, u"Open", wx.EmptyString, wx.ITEM_NORMAL)
        self.menu_file.Append(self.menu_item_file_open)

        self.menu_file.AppendSeparator()

        self.menu_submenu_item_file_recent = wx.Menu()
        self.menu_submenu_item_file_recent_none = wx.MenuItem(self.menu_submenu_item_file_recent, wx.ID_ANY, u"None", wx.EmptyString, wx.ITEM_NORMAL)
        self.menu_submenu_item_file_recent.Append(self.menu_submenu_item_file_recent_none)
        self.menu_submenu_item_file_recent_none.Enable(False)

        self.menu_file.AppendSubMenu(self.menu_submenu_item_file_recent, u"Recent")

        self.menu_file.AppendSeparator()

        self.menu_item_file_quit = wx.MenuItem(self.menu_file, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL)
        self.menu_file.Append(self.menu_item_file_quit)

        self.menubar.Append(self.menu_file, u"File")

        self.menu_data = wx.Menu()
        self.menu_item_data_missing_items = wx.MenuItem(self.menu_data, wx.ID_ANY, u"View missing items", wx.EmptyString, wx.ITEM_NORMAL)
        self.menu_data.Append(self.menu_item_data_missing_items)

        self.menu_data.AppendSeparator()

        self.menu_item_generate_textgrid = wx.MenuItem(self.menu_data, wx.ID_ANY, u"Generate TextGrids", wx.EmptyString, wx.ITEM_NORMAL)
        self.menu_data.Append(self.menu_item_generate_textgrid)

        self.menubar.Append(self.menu_data, u"Data")

        self.menu_preferences = wx.Menu()
        self.menu_item_preferences_session = wx.MenuItem(self.menu_preferences, wx.ID_ANY, u"Default session directory", wx.EmptyString, wx.ITEM_NORMAL)
        self.menu_preferences.Append(self.menu_item_preferences_session)

        self.menu_submenu_languages = wx.Menu()
        self.menu_submenu_item_preferences_language_default = wx.MenuItem(self.menu_submenu_languages, wx.ID_ANY, u"Default", wx.EmptyString, wx.ITEM_NORMAL)
        self.menu_submenu_languages.Append(self.menu_submenu_item_preferences_language_default)

        self.menu_preferences.AppendSubMenu(self.menu_submenu_languages, u"Languages")

        self.menubar.Append(self.menu_preferences, u"Preferences")

        self.menu_about = wx.Menu()
        self.menu_item_about_version = wx.MenuItem(self.menu_about, wx.ID_ANY, u"Version", wx.EmptyString, wx.ITEM_NORMAL)
        self.menu_about.Append(self.menu_item_about_version)

        self.menubar.Append(self.menu_about, u"?")

        self.SetMenuBar(self.menubar)

        sizer_main = wx.BoxSizer(wx.VERTICAL)

        self.main_dummy_panel = PanelRecord(self)
        sizer_main.Add(self.main_dummy_panel, 1, wx.EXPAND |wx.ALL, 5)


        self.SetSizer(sizer_main)
        self.Layout()
        self.statusbar = self.CreateStatusBar(3, wx.STB_SIZEGRIP, wx.ID_ANY)

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_MENU, self.Menu_File_New_Text_commmand, id = self.menu_submenu_file_item_new_text_elicit.GetId())
        self.Bind(wx.EVT_MENU, self.Menu_File_New_Respeak_command, id = self.menu_submenu_file_item_new_respeaking.GetId())
        self.Bind(wx.EVT_MENU, self.Menu_File_Open_commmand, id = self.menu_item_file_open.GetId())
        self.Bind(wx.EVT_MENU, self.Menu_Data_ViewMissing_Command, id = self.menu_item_data_missing_items.GetId())
        self.Bind(wx.EVT_MENU, self.Menu_Data_Generate_TextGrid_Command, id = self.menu_item_generate_textgrid.GetId())
        self.Bind(wx.EVT_MENU, self.Menu_Preference_Session_command, id = self.menu_item_preferences_session.GetId())
        self.Bind(wx.EVT_MENU, self.Menu_Question_Version, id = self.menu_item_about_version.GetId())

    def __del__(self):
        pass


    # Virtual event handlers, override them in your derived class
    def Menu_File_New_Text_commmand(self, event):
        event.Skip()

    def Menu_File_New_Respeak_command(self, event):
        event.Skip()

    def Menu_File_Open_commmand(self, event):
        event.Skip()

    def Menu_Data_ViewMissing_Command(self, event):
        event.Skip()

    def Menu_Data_Generate_TextGrid_Command(self, event):
        event.Skip()

    def Menu_Preference_Session_command(self, event):
        event.Skip()

    def Menu_Question_Version(self, event):
        event.Skip()

    def set_controller(self, controller):
        self.ctrl = controller


if __name__ == '__main__':
    app = wx.App()
    frame = WindowMain(None)
    frame.Show()
    app.MainLoop()
