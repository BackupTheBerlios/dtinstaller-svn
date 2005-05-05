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
failsafe = 0
clui = 0
failsafeChecked = 0
cluiChecked = 1

## definitions and classes

class checkArgs:

	"""Argument handling. This should be replaced by a more sane system soon!

	@authors: trygvebw <trygvebw@gmail.com>
	@license: BSDL"""

	if len(sys.argv) > 1:
		if sys.argv[1]=="--help":
			print "usage: dtinstaller [--help] [--debug|--failsafe|--clui]"

	@classmethod
	def checkDebug(self): 
			if len(sys.argv) > 1:
				if sys.argv[1]=="--debug":
					debug = 1
					debugChecked = 1
					print "debug mode was called!"
					self.checkFailsafe()
					if failsafeChecked == 1 and cluiChecked == 0:
						self.checkClui()
					elif failsafeChecked == 0:
						self.checkFailsafe()
						if cluiChecked == 0:
							self.checkClui()

	@classmethod
	def checkFailsafe(self):
			if len(sys.argv) > 1:
				if sys.argv[1]=="--failsafe":
					failsafe = 1
					failsafeChecked = 1
					print "failsafe mode was called!"
					if debugChecked == 1 and cluiChecked == 0:
						self.checkClui()
					elif debugChecked == 0:
						self.checkDebug()
						if cluiChecked == 0:
							self.checkClui()

	@classmethod
	def checkClui(self):
			if len(sys.argv) > 1:
				if sys.argv[1]=="--clui":
					clui = 1
					cluiChecked = 1
					print "clui mode was called!"
					if debugChecked == 1 and failsafeChecked == 0:
						self.checkFailsafe()
					elif debugChecked == 0:
						self.checkDebug()
						if failsafeChecked == 0:
							self.checkFailsafe()
	@classmethod
	def checkArgsStart(self):
			self.checkDebug()

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

def callGUI():
	from CallModules import CallEm
	CallEm.nextModule("fdfd")
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
