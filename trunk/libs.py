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
