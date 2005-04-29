#!/usr/bin/env python

import sys
import os
import time
import pygtk
import gtk
import gtk.glade
import gobject

import libs
import widgets
import variables
import colours
import tabs

## definitions and classes
def checkXorg(versionX="nover"):
	if versionX != "nover":
		print "TODO: Check for Xorg version if not \"nover\""
		return 0
	else:
		print "DEBUG: You have specified to not check for a specific Xorg version."
		return 1

class checkArgs:
	if sys.argv[1]=="--help":
		print "usage: dtinstaller [--help] [--debug|--failsafe|--clui]"

	def checkDebug(self): 
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

## end of definitions
## checks and pre-variables

checkArgs()

## end checks and pre-variables
## main body

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

#imports.variables.variablee()
widgets.createWindow("dtinstaller")
#libs.ChangeColorSide()

#def quit(x, y):
#	window1.destroy()
#	gtk.main_quit()

gtk.main()
