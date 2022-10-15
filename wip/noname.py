# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-239-ge2e4764f)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import gettext
_ = gettext.gettext

###########################################################################
## Class Wilaikuma_Main
###########################################################################

class Wilaikuma_Main ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1000,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.MAXIMIZE|wx.MAXIMIZE_BOX|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        self.m_menubar1 = wx.MenuBar( 0 )
        self.menubar = wx.Menu()
        self.menuitem_file_quit = wx.MenuItem( self.menubar, wx.ID_ANY, _(u"Quit"), wx.EmptyString, wx.ITEM_NORMAL )
        self.menubar.Append( self.menuitem_file_quit )

        self.m_menubar1.Append( self.menubar, _(u"File") )

        self.SetMenuBar( self.m_menubar1 )

        sizer_main = wx.BoxSizer( wx.VERTICAL )

        self.main_dummy_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        sizer_main.Add( self.main_dummy_panel, 1, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( sizer_main )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


###########################################################################
## Class welcome_panel
###########################################################################

class welcome_panel ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        welcome_panel_sizer = wx.BoxSizer( wx.HORIZONTAL )

        initiate_session_sizer = wx.BoxSizer( wx.VERTICAL )

        self.button_select_sentence_file = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, _(u"Select a file"), _(u"*.txt"), wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
        initiate_session_sizer.Add( self.button_select_sentence_file, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.button_start_session = wx.Button( self, wx.ID_ANY, _(u"Start Session"), wx.DefaultPosition, wx.DefaultSize, 0 )
        initiate_session_sizer.Add( self.button_start_session, 0, wx.ALL, 5 )


        welcome_panel_sizer.Add( initiate_session_sizer, 1, wx.EXPAND, 5 )


        self.SetSizer( welcome_panel_sizer )
        self.Layout()

    def __del__( self ):
        pass


###########################################################################
## Class record_panel
###########################################################################

class record_panel ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        record_panel_sizer = wx.BoxSizer( wx.VERTICAL )

        self.record_panel_inner = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        record_panel_inner_sizer = wx.BoxSizer( wx.HORIZONTAL )

        record_panel_inner_sizer_control = wx.BoxSizer( wx.VERTICAL )

        control_top_play_sizer = wx.BoxSizer( wx.HORIZONTAL )

        self.button_play = wx.Button( self.record_panel_inner, wx.ID_ANY, _(u"Play"), wx.DefaultPosition, wx.DefaultSize, 0 )
        control_top_play_sizer.Add( self.button_play, 1, wx.ALL|wx.EXPAND, 5 )


        record_panel_inner_sizer_control.Add( control_top_play_sizer, 1, wx.EXPAND, 5 )

        control_middle_record_sizer = wx.BoxSizer( wx.HORIZONTAL )

        self.button_previous = wx.Button( self.record_panel_inner, wx.ID_ANY, _(u"Previous"), wx.DefaultPosition, wx.DefaultSize, 0 )
        control_middle_record_sizer.Add( self.button_previous, 1, wx.ALL|wx.EXPAND, 5 )

        control_bottom_stats = wx.BoxSizer( wx.VERTICAL )

        self.button_record = wx.Button( self.record_panel_inner, wx.ID_ANY, _(u"Record"), wx.DefaultPosition, wx.DefaultSize, 0 )
        control_bottom_stats.Add( self.button_record, 1, wx.ALL|wx.EXPAND, 5 )

        self.button_delete = wx.Button( self.record_panel_inner, wx.ID_ANY, _(u"Delete"), wx.DefaultPosition, wx.DefaultSize, 0 )
        control_bottom_stats.Add( self.button_delete, 1, wx.ALL|wx.EXPAND, 5 )


        control_middle_record_sizer.Add( control_bottom_stats, 1, 0, 5 )

        self.button_next = wx.Button( self.record_panel_inner, wx.ID_ANY, _(u"Next"), wx.DefaultPosition, wx.DefaultSize, 0 )
        control_middle_record_sizer.Add( self.button_next, 1, wx.ALL|wx.EXPAND, 5 )


        record_panel_inner_sizer_control.Add( control_middle_record_sizer, 1, wx.EXPAND, 5 )

        control_bottom_stats = wx.BoxSizer( wx.HORIZONTAL )

        self.label_progress = wx.StaticText( self.record_panel_inner, wx.ID_ANY, _(u"[0/0]"), wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.label_progress.Wrap( -1 )

        control_bottom_stats.Add( self.label_progress, 1, wx.ALL|wx.EXPAND, 5 )

        self.label_sentence_id = wx.StaticText( self.record_panel_inner, wx.ID_ANY, _(u"sentence_id"), wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.label_sentence_id.Wrap( -1 )

        control_bottom_stats.Add( self.label_sentence_id, 1, wx.ALL|wx.EXPAND, 5 )


        record_panel_inner_sizer_control.Add( control_bottom_stats, 1, wx.EXPAND, 5 )

        self.button_stop_session = wx.Button( self.record_panel_inner, wx.ID_ANY, _(u"Stop Session"), wx.DefaultPosition, wx.DefaultSize, 0 )
        record_panel_inner_sizer_control.Add( self.button_stop_session, 1, wx.ALL|wx.EXPAND, 5 )


        record_panel_inner_sizer.Add( record_panel_inner_sizer_control, 0, wx.ALIGN_CENTER, 5 )

        record_panel_inner_sizer_sentence = wx.BoxSizer( wx.VERTICAL )


        record_panel_inner_sizer_sentence.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.label_sentence = wx.StaticText( self.record_panel_inner, wx.ID_ANY, _(u"sentence"), wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.label_sentence.Wrap( -1 )

        record_panel_inner_sizer_sentence.Add( self.label_sentence, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )


        record_panel_inner_sizer_sentence.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        record_panel_inner_sizer.Add( record_panel_inner_sizer_sentence, 1, wx.EXPAND, 5 )


        self.record_panel_inner.SetSizer( record_panel_inner_sizer )
        self.record_panel_inner.Layout()
        record_panel_inner_sizer.Fit( self.record_panel_inner )
        record_panel_sizer.Add( self.record_panel_inner, 1, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( record_panel_sizer )
        self.Layout()

        # Connect Events
        self.button_play.Bind( wx.EVT_BUTTON, self._event_play )
        self.button_previous.Bind( wx.EVT_BUTTON, self._event_previous )
        self.button_record.Bind( wx.EVT_BUTTON, self._event_record )
        self.button_delete.Bind( wx.EVT_BUTTON, self.event_delete )
        self.button_next.Bind( wx.EVT_BUTTON, self._event_next )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def _event_play( self, event ):
        event.Skip()

    def _event_previous( self, event ):
        event.Skip()

    def _event_record( self, event ):
        event.Skip()

    def event_delete( self, event ):
        event.Skip()

    def _event_next( self, event ):
        event.Skip()


