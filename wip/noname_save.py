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
## Class Wilaikuma_Frame
###########################################################################

class Wilaikuma_Frame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1000,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.MAXIMIZE|wx.MAXIMIZE_BOX|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        self.m_menubar1 = wx.MenuBar( 0 )
        self.menubar_main = wx.Menu()
        self.menuitem_file_quit = wx.MenuItem( self.menubar_main, wx.ID_ANY, _(u"Quit"), wx.EmptyString, wx.ITEM_NORMAL )
        self.menubar_main.Append( self.menuitem_file_quit )

        self.m_menubar1.Append( self.menubar_main, _(u"File") )

        self.SetMenuBar( self.m_menubar1 )

        sizer_main = wx.BoxSizer( wx.VERTICAL )

        self.m_panel3 = MyPanel(self)
        sizer_main.Add( self.m_panel3, 1, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( sizer_main )
        self.Layout()

        self.Centre( wx.BOTH )
        self.Show()

    def __del__( self ):
        pass


###########################################################################
## Class MyPanel3
###########################################################################

def scale_bitmap(bitmap, width, height):
    image = wx.ImageFromBitmap(bitmap)
    image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
    result = wx.BitmapFromImage(image)
    return result

class MyPanel ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        bSizer10 = wx.BoxSizer( wx.VERTICAL )

        self.panel_recording = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer6 = wx.BoxSizer( wx.VERTICAL )

        bSizer91 = wx.BoxSizer( wx.HORIZONTAL )

        self.button_listen_start = wx.Button( self.panel_recording, wx.ID_ANY, _(u"Listen"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer91.Add( self.button_listen_start, 1, wx.ALL|wx.EXPAND, 5 )

        self.button_listen_stop = wx.Button( self.panel_recording, wx.ID_ANY, _(u"Pause"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer91.Add( self.button_listen_stop, 1, wx.ALL|wx.EXPAND, 5 )


        bSizer6.Add( bSizer91, 1, wx.EXPAND, 5 )

        bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

        self.button_previous = wx.Button( self.panel_recording, wx.ID_ANY, _(u"Previous"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer7.Add( self.button_previous, 1, wx.ALL|wx.EXPAND, 5 )

        bSizer8 = wx.BoxSizer( wx.VERTICAL )

        self.button_record = wx.Button( self.panel_recording, wx.ID_ANY,  wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        record_image = wx.Bitmap(u"assets/record.png", wx.BITMAP_TYPE_ANY)
        record_image = scale_bitmap(record_image, 50, 50)
        self.button_record.SetBitmap(record_image)
        bSizer8.Add( self.button_record, 1, wx.ALL|wx.EXPAND, 5 )

        self.button_delete = wx.Button( self.panel_recording, wx.ID_ANY, _(u"Delete"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer8.Add( self.button_delete, 1, wx.ALL|wx.EXPAND, 5 )


        bSizer7.Add( bSizer8, 1, 0, 5 )

        self.button_next = wx.Button( self.panel_recording, wx.ID_ANY, _(u"Next"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer7.Add( self.button_next, 1, wx.ALL|wx.EXPAND, 5 )


        bSizer6.Add( bSizer7, 1, wx.EXPAND, 5 )

        bSizer92 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText2 = wx.StaticText( self.panel_recording, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.m_staticText2.Wrap( -1 )

        bSizer92.Add( self.m_staticText2, 1, wx.ALL|wx.EXPAND, 5 )

        self.m_staticText3 = wx.StaticText( self.panel_recording, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.m_staticText3.Wrap( -1 )

        bSizer92.Add( self.m_staticText3, 1, wx.ALL|wx.EXPAND, 5 )


        bSizer6.Add( bSizer92, 1, wx.EXPAND, 5 )


        bSizer5.Add( bSizer6, 0, wx.ALIGN_CENTER, 5 )

        bSizer9 = wx.BoxSizer( wx.VERTICAL )


        bSizer9.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText4 = wx.StaticText( self.panel_recording, wx.ID_ANY, _(u"MyLabel"), wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.m_staticText4.Wrap( -1 )

        bSizer9.Add( self.m_staticText4, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


        bSizer9.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer5.Add( bSizer9, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


        self.panel_recording.SetSizer( bSizer5 )
        self.panel_recording.Layout()
        bSizer5.Fit( self.panel_recording )
        bSizer10.Add( self.panel_recording, 1, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( bSizer10 )
        self.Layout()

    def __del__( self ):
        pass


if __name__ == '__main__':
    app = wx.App()
    frame = Wilaikuma_Frame(None)
    app.MainLoop()

