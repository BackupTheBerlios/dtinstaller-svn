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

## basic definitions. most of these are deprecated, if you find another way of getting working
## code without pre-defining them, please fix.

debug = 0
failsafe = 0
clui = 0
failsafeChecked = 0
cluiChecked = 1

## definitions and classes

class checkArgs:

	"""Argument handling. This should be replaced by a more sane system soon!

	@authors: trygvebw <trygvebw@gmail.com>
	@license: BSDL"""

	@classmethod
	def checkHelp(self):
		if len(sys.argv) > 1:
			if sys.argv[1]=="--help":
				print "usage: dtinstaller [--help] [--debug|--failsafe|--clui]"
		self.checkDebug()

	@classmethod
	def checkDebug(self): 
			if len(sys.argv) > 1:
				if sys.argv[1]=="--debug":
					debug = 1
					debugChecked = 1
					print "debug mode was called!"
				self.checkFailsafe()

	@classmethod
	def checkFailsafe(self):
			if len(sys.argv) > 1:
				if sys.argv[1]=="--failsafe":
					failsafe = 1
					failsafeChecked = 1
					print "failsafe mode was called!"
				self.checkClui()

	@classmethod
	def checkClui(self):
			if len(sys.argv) > 1:
				if sys.argv[1]=="--clui":
					clui = 1
					cluiChecked = 1
					print "clui mode was called!"
	@classmethod
	def checkArgsStart(self):
			self.checkHelp()

## w00t0h! the checkXorg function *finally* does something! :D

if os.getenv("DISPLAY") == None:
	print "xorg = 0 has been defined"
	xorg = 0
else:
	print "xorg = 1 has been defined"
	xorg = 1

## import GTK

if xorg == 1:
	import pygtk
	import gtk
	import gtk.glade
	import gobject
else:
	print "DEBUG: no GTK loaded"

## end

def callGUI():
	from CallModules import CallEm
	CallEm.nextModuleBorked()
#	Call()
	gtk.main()

def callCLUI():
	print "TODO: command line environment!"

#def Call():
#	import CallModules
#	CallModules.CallEm.callModule("Welcome")
	
## end of definitions
## checks and pre-variables

## end checks and pre-variables
## main body - this'll check if Xorg exists.

def xorgCheck():
	if xorg == 1:
		if debug == 1:
			print "xorg is running."
			try:
				if clui == 0:
					clui = 0
				elif clui == 1:
					clui = 1
				else:
					print "nil"
			except:
				clui == 0
		else:
			try:
				if clui == 0:
					clui = 0
				elif clui == 1:
					clui = 1
				else:
					print "nil"
			except:
				print "nil"
	elif xorg == 0:
		print "xorg is not running."
		clui = 0

xorgCheck()

WidgetActions.createWindow("dtinstaller")

## "In the beginning the Universe was created. This has made a lot of people very angry and been widely regarded as a bad move." -Douglas Adams

if len(sys.argv) > 1:
	checkArgs.checkArgsStart()
	if debug == 1:
		callGUI()
	if failsafe == 1:
		callGUI()
	if clui == 1:
		callCLUI()
else:
	print "standard gui mode was called!"
	callGUI()
