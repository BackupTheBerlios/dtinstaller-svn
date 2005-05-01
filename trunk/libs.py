#!/usr/bin/env python

import sys
import os
import time
import pygtk
import gtk
import gtk.glade
import gobject

rootdir = os.getcwd()

def fullPath():
	paths = ["/src", "/src/art", "/modules"]
	
	for path in paths:
		sys.path.append(rootdir + path)

fullPath()

import libs
import widgets
import variables
import colours

def ChangeColorSide():
	e = gtk.Entry()
	map = e.get_colormap()
	colour = map.alloc_color("#FF9999") # light red
	xml = gtk.glade.XML(rootdir + '/src/gui/gui.glade')
	colorbox = xml.get_widget('colorbox')
	widgets = xml.get_widget_prefix('')
	gtk.EventBox.modify_bg(colorbox, "GTK_STATE_NORMAL", colour)

def quitProg(q, w):
	print "ERROR: Unexpected Quit Signal!"
	gtk.main_quit()

def quitProgWarning(message):
	print "TODO: Quit Warning!"
	gtk.main_quit()
