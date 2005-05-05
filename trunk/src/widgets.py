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
from CallModules import CallEm
from colours import colours

#def importObjects():
#	widgets = xml.get_widget('colorbox')

## class: we do different things with widgets.

class WidgetActions:

	"""Class for general widget/window actions.

	@authors: trygvebw <trygvebw@gmail.com>
	@license: BSDL"""

	xml = gtk.glade.XML(libs.rootdir + '/src/gui/gui.glade', "dtinstaller")
	colourbox = xml.get_widget('colorbox')
	quitmenubt = xml.get_widget('quit1')
	notebook = xml.get_widget('notebook')
	colourtopbox = xml.get_widget('coloreventbox')
	quitbt = xml.get_widget('quitbt')
	widgets = xml.get_widget_prefix('')

	@classmethod
	def createWindow(self, window="dtinstaller"):

		"""This function creates all the windows and widgets and configures them."""
	
		self.notebook.set_show_tabs(0)
		e = gtk.Entry()
		map = e.get_colormap()
		colourRightBar = map.alloc_color(colours.rightbar) # blue
		colourTopBar = map.alloc_color(colours.topbar) # dark blue
		gtk.EventBox.modify_bg(self.colourbox, "GTK_STATE_NORMAL", colourRightBar)
		gtk.EventBox.modify_bg(self.colourtopbox, "GTK_STATE_NORMAL", colourTopBar)
		
		## gtk event/signal checking/connecting/handling	
	
		signal_handlers = {
			'on_' + window + '_delete_event': libs.quitProg,
			'on_quitbt_clicked': libs.quitProgWarning,
			'on_nextbt_clicked': CallEm.nextModule,
			'on_quit1_activate': self.WindowTypes.createMessageWindow
			}
	
		self.xml.signal_autoconnect(signal_handlers)

	## subclass: templates of different window types

	class WindowTypes:

		"""Templates of different window types."""

		@classmethod
		def createMessageWindow(message="", title="", backbtaction="", proceedbtaction=""):
			
			"""This function creates a message window."""
			
			f = gtk.Entry()
			map2 = f.get_colormap()
			xml2 = gtk.glade.XML(libs.rootdir + '/src/gui/gui.glade', "msgwindow")
			msgwcolour = map2.alloc_color("#F0F0F0") # grey
			msgwindowcolour = xml2.get_widget('msgwindow')
			gtk.EventBox.modify_bg(msgwindowcolour, "GTK_STATE_NORMAL", msgwcolour)
