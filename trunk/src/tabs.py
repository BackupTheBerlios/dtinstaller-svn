#!/usr/bin/env python

import sys
import os
import time
import pygtk
import gtk
import gtk.glade
import gobject

rootdir = os.getcwd()
sys.path.append(rootdir + '/..')
sys.path.append(rootdir + '/art')

import libs
import variables
import colours
import widgets

## variables

failsafe = 1

## end variables
## definitions

def tabZero():
	ExpLabel.set_use_markup(gtk.TRUE)
	ExpLabel.set_markup('normal text, <b>bold text</b>, <i>italic text</i>')

## end of definitions
