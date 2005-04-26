#!/usr/bin/env python

import sys
import os
import time
import pygtk
import gtk
import gtk.glade
import gobject

sys.path.append('./src')
sys.path.append('./src/art')
rootdir = os.getcwd()

import imports

## This file is a roadsign to all the different files that normal .py files should import.
## All .py files should import this file and run one of the imports() functions.

def imports():
	import libs
	import widgets
	import variables
	import colours

def importsBasic():
	import libs
	import variables
	import widgets
