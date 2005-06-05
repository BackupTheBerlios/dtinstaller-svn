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

#!/usr/bin/env python

import sys
import os
import time
import pygtk
import gtk
import gtk.glade
import libs

libs.fullPath()

#import importModules

#importModules.importModules()

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
	def nextModuleBorked(x):
		"""Only for use in main.py."""
		from widgets import WidgetActions
		notebook = WidgetActions.xml.get_widget('notebook')
		#notebook.next_page()
		print "nextModuleBorked() has been called!"

	@classmethod
	def nextModule(x, y):
		"""This function cycles to the next module without checking anything. It shouldn't
		normally be used. Please use callModule(). In the first alpha/beta versions it
		can be used, since we haven't got callModule() working correctly yet."""

		from widgets import WidgetActions
		try: # prøve om explevel er definert

			if explevel == "Beginner": # hvis explevel er begynner
				import stages # vi importer stages.py
				notebook.set_page(begstage[stage]) # vi setter den aktive siden 
				# til det "stage" er. "stage" er det steget vi er på.
				stageFunction = begstage[stage] # vi lager en funksjon
				stageFunction() # vi kaller startfunksjonen til den.
				stage = stage + 1 # vi gjør stage en høyere

			if explevel == "Advanced": # hvis explevel er begynner
				import stages # vi importer stages.py
				notebook.set_page(begstage[stage]) # vi setter den aktive siden 
				# til det "stage" er. "stage" er det steget vi er på.
				stageFunction = begstage[stage] # vi lager en funksjon
				stageFunction() # vi kaller startfunksjonen til den.
				stage = stage + 1 # vi gjør stage en høyere

			if explevel == "Expert": # hvis explevel er begynner
				import stages # vi importer stages.py
				notebook.set_page(begstage[stage]) # vi setter den aktive siden 
				# til det "stage" er. "stage" er det steget vi er på.
				stageFunction = begstage[stage] # vi lager en funksjon
				stageFunction() # vi kaller startfunksjonen til den.
				stage = stage + 1 # vi gjør stage en høyere

		except: # hvis explevel ikke er definert
			notebook = WidgetActions.xml.get_widget('notebook') # importer
			notebook.next_page() # vi går til neste side

#		def goTo():
#			if stage: ## This if-sequense is broken, too many indents.
#				notebook.set_page(stage)
#				if stage == 0:
#					if explevel:
#						if explevel == "Beginner":
#							notebook.set_page(begstage[stage])
#			else: 
#				stage = 0

#		notebook = WidgetActions.xml.get_widget('notebook')
#		notebook.next_page()
