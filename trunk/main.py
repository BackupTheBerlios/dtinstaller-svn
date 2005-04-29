#!/usr/bin/env python

import sys
import os
import time
import pygtk
import gtk
import gtk.glade
import gobject

rootdir = os.getcwd()
sys.path.append(rootdir + '/src')
sys.path.append(rootdir + '/src/art')

import libs
import widgets
import variables
import colours
import tabs

## variables

debug = 1

## end variables
## definitions
def checkXorg(versionX="nover"):
	if versionX != "nover":
		print "TODO: Check for Xorg version if not \"nover\""
		return 0
	else:
		print "DEBUG: You have specified to not check for a specific Xorg version."
		return 1

## end of definitions
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
