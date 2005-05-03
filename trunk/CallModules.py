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

	@authors: trygvebw <trygvebw@gmail.com>
	@license: BSDL"""

	@classmethod
	def callModule(module="none", x="x"):
		
		"""This function calls a module. moduleToCall is the module to call. module can
		be Welcome, ExpLang, Part, Package, BootLoader, Summary or Final."""
		moduleToCall = module
		if moduleToCall == "Welcome" or module == 1:
			from Welcome import WelcomeScreen
			WelcomeScreen.welcomeTab(WelcomeScreen)
			module = 1

	@classmethod
	def nextModule(x, y):
		"""This function cycles to the next module without checking anything. It shouldn't
		normally be used. Please use callModule(). In the first alpha/beta versions it
		can be used, since we haven't got callModule() working correctly yet."""

		from widgets import WidgetActions
		notebook = WidgetActions.xml.get_widget('notebook')
		notebook.next_page()
