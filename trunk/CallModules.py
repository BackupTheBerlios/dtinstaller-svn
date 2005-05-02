#!/usr/bin/env python

import sys
import os
import time
import pygtk
import gtk
import gtk.glade
import libs

libs.fullPath()

class CallEm:

	"""All installer modules are loaded through these functions.

	@authors: Exigo Linux Team 4 <trygvebw@gmail.com>
	@license: BSDL"""

	def callModule(self, module):
		
		"""This function calls a module. moduleToCall is the module to call. module can
		be Welcome, ExpLang, Part, Package, BootLoader, Summary or Final."""
		moduleToCall = module
		if moduleToCall == "Welcome":
			from Welcome import WelcomeScreen
			WelcomeScreen.welcomeTab(WelcomeScreen)
