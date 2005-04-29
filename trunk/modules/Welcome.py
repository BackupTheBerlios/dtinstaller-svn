#!/usr/bin/env python

class WelcomeScreen:

	"""Last screen before installation - summary of what you've chosen
	in the install.

	@authors: Exigo Linux Team 4 <trygvebw@gmail.com
	@license: BSDL"""

	## Variables	

	def welcomeTab(self):
		notebook1 = gtk.Notebook
		notebook1.switch-page(1)
