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
import colours

#def importObjects():
#	widgets = xml.get_widget('colorbox')

def createWindow(window="dtinstaller"):
	xml = gtk.glade.XML(libs.rootdir + '/src/gui/gui.glade', window)
	colorbox = xml.get_widget('colorbox')
	widgets = xml.get_widget_prefix('')

	e = gtk.Entry()
	map = e.get_colormap()
	colour = map.alloc_color("#FF9999") # light red
	gtk.EventBox.modify_bg(colorbox, "GTK_STATE_NORMAL", colour)
	
	signal_handlers = {
		'on_' + window + '_delete_event': libs.quitProg
		}

	xml.signal_autoconnect(signal_handlers)
