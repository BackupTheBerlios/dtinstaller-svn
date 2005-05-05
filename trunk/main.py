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

from widgets import WidgetActions
import variables
import colours
import tabs

## basic definitions. most of these are deprecated, if you find another way of getting working
## code without pre-defining them, please fix.

debug = 0

## definitions and classes

## w00t0h! the checkXorg function *finally* does something! :D

def checkXorg(versionX="nover"):
	if versionX != "nover":
		def checkXorgBase():
			if os.getenv("DISPLAY") == None:
				return 0
			else:
				return 1
		x11exist = "nullthingies" ## checkthingies
	elif debug == 1 and versionX == "nover":
		print "DEBUG: You have specified to not check for a specific Xorg version."
		return 1

class checkArgs:
	if 1 in sys.argv:
		if sys.argv[1]=="--help":
			print "usage: dtinstaller [--help] [--debug|--failsafe|--clui]"

	def checkDebug(self): 
			if 1 in sys.argv:
				if sys.argv[1]=="--debug":
					debug = 1
					debugChecked = 1
					checkFailsafe()
					if failsafeChecked == 1 and cluiChecked == 0:
						checkClui()
					elif failsafeChecked == 0:
						checkFailsafe()
						if cluiChecked == 0:
							checkClui()

	def checkFailsafe(self):
			if 1 in sys.argv:
				if sys.argv[1]=="--failsafe":
					failsafe = 1
					failsafeChecked = 1
					if debugChecked == 1 and cluiChecked == 0:
						checkClui()
					elif debugChecked == 0:
						checkDebug()
						if cluiChecked == 0:
							checkClui()

	def checkClui(self):
			if 1 in sys.argv:
				if sys.argv[1]=="--clui":
					failsafe = 1
					failsafeChecked = 1
					if debugChecked == 1 and failsafeChecked == 0:
						checkFailsafe()
					elif debugChecked == 0:
						checkDebug()
						if failsafeChecked == 0:
							checkFailsafe()
	def checkArgsStart(self):
			self.checkDebug()

def callGUI():
	from CallModules import CallEm
	CallEm.nextModule("fdfd")
#	Call()
	gtk.main()

#def Call():
#	import CallModules
#	CallModules.CallEm.callModule("Welcome")
	
## end of definitions
## checks and pre-variables

## end checks and pre-variables
## main body - this'll check if Xorg exists. it's only printing some fake
## messages at the moment.

xorg = checkXorg("nover")

if xorg == 1:
	if debug == 1:
		print "xorg is running."
		xval = 1
	else:
		xval = 1
else:
	print "xorg is not running."
	xval = 0

WidgetActions.createWindow("dtinstaller")

## "In the beginning the Universe was created. This has made a lot of people very angry and been widely regarded as a bad move." -Douglas Adams

if 1 in sys.argv:
	checkArgs.checkArgsStart()
else:
	callGUI()
