#!/usr/bin/env python

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

import sys
import os
import time
import libs

libs.fullPath()

from widgets import WidgetActions
import variables
import colours

## definitions and classes

def initGUI():
        if os.getenv("DISPLAY") == None:
                print "We must start X here"
                xorg = 0
        else:
                print "X is running, so lets continue"
                xorg = 1

        ## import GTK

        if xorg == 1:
                import pygtk
                import gtk
                import gtk.glade
                import gobject
        else:
                print "Unable to load GTK"

        ## end

        ## end of definitions
        ## checks and pre-variables

        ## end checks and pre-variables
        ## main body - this'll check if Xorg exists.

        WidgetActions.createWindow("dtinstaller")

        ## "In the beginning the Universe was created. This has made a lot of people very angry and been widely regarded as a bad move." -Douglas Adams

        print "Executing the GUI... Please stand by"
        from CallModules import CallEm
        gtk.main()
