#!/usr/bin/env python

import sys
import os
import time
import pygtk
import gtk
import gtk.glade
import gobject
import libs

libs.fullPath()

import variables
from colours import colours

#def importObjects():
#	widgets = xml.get_widget('colorbox')

def createWindow(window="dtinstaller"):
	xml = gtk.glade.XML(libs.rootdir + '/src/gui/gui.glade', window)
	colourbox = xml.get_widget('colorbox')
	notebook = xml.get_widget('notebook')
	colourtopbox = xml.get_widget('coloreventbox')
	quitbt = xml.get_widget('quitbt')
	widgets = xml.get_widget_prefix('')

	notebook.set_show_tabs(0)
	e = gtk.Entry()
	map = e.get_colormap()
	colourRightBar = map.alloc_color(colours.rightbar) # blue
	colourTopBar = map.alloc_color(colours.topbar) # dark blue
	gtk.EventBox.modify_bg(colourbox, "GTK_STATE_NORMAL", colourRightBar)
	gtk.EventBox.modify_bg(colourtopbox, "GTK_STATE_NORMAL", colourTopBar)
	
	
	signal_handlers = {
		'on_' + window + '_delete_event': libs.quitProg,
		'on_quitbt_clicked': libs.quitProgWarning
		}

	xml.signal_autoconnect(signal_handlers)
