# Copyright (c) 2005 Trygve B. Wiig <trygvebw@gmail.com>
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

import colours

class WelcomeScreen:

	"""Last screen before installation - summary of what you've chosen
	in the install.

	@authors: trygvebw <trygvebw@gmail.com>
	@license: BSDL"""

	## Variables	

	def welcomeTab(self):
		notebook1 = gtk.Notebook
		notebook1.set_page(1)
		
		## widgets

		oneleft = xml.get_widget('1left')
		oneright = xml.get_widget('1right')
		onebottom = xml.get_widget('1bottom')
		onetop = xml.get_widget('1top')

		self.notebook.set_show_tabs(0)
		e = gtk.Entry()
		map = e.get_colormap()
		black = map.alloc_color(colours.black) # black
		gtk.EventBox.modify_bg(oneleft, "GTK_STATE_NORMAL", colourBottomBox)
		gtk.EventBox.modify_bg(oneright, "GTK_STATE_NORMAL", colourBottomBox)
		gtk.EventBox.modify_bg(onebottom, "GTK_STATE_NORMAL", colourBottomBox)
		gtk.EventBox.modify_bg(onetop, "GTK_STATE_NORMAL", colourBottomBox)
