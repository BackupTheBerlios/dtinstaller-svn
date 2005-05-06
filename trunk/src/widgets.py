# Copyright (c) 2000 Trygve B. Wiig <trygvebw@gmail.com>
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:

# 1. Redistributions of source code must retain the above copyright notice, this list of 
# conditions # and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice, this list of 
# conditions and the following disclaimer in the documentation and/or other materials provided 
# with the distribution.
# 3. The name of the author may not be used to endorse or promote products derived from this 
# software without specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, 
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. 
# IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, 
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF 
# USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) 
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, 
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
# OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

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
	quitmenubt = xml.get_widget('quit1')
	notebook = xml.get_widget('notebook')
	quitbt = xml.get_widget('quitbt')
	widgets = xml.get_widget_prefix('')

	@classmethod
	def createWindow(self, window="dtinstaller"):

		"""This function creates all the windows and widgets and configures them."""
	
		self.notebook.set_show_tabs(0)
#		e = gtk.Entry()
#		map = e.get_colormap()
#		colourRightBar = map.alloc_color(colours.rightbar) # blue
#		gtk.EventBox.modify_bg(self.colourbox, "GTK_STATE_NORMAL", colourRightBar)
		
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
			
			print "fake"
			f = gtk.Entry()
			map2 = f.get_colormap()
			xml2 = gtk.glade.XML(libs.rootdir + '/src/gui/gui.glade', "msgwindow")
			msgwcolour = map2.alloc_color("#F0F0F0") # grey
			msgwindowcolour = xml2.get_widget('msgwindow')
			gtk.EventBox.modify_bg(msgwindowcolour, "GTK_STATE_NORMAL", msgwcolour)
