#!/usr/bin/env python

class WelcomeScreen:

	"""Last screen before installation - summary of what you've chosen
	in the install.

	@authors: trygvebw <trygvebw@gmail.com>
	@license: BSDL"""

	## Variables	

	def welcomeTab(self):
		notebook1 = gtk.Notebook
		notebook1.set_page(1)
