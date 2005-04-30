#!/usr/bin/env python

class CallEm:

	"""All installer modules are loaded through these functions.

	@authors: Exigo Linux Team 4 <trygvebw@gmail.com>
	@license: BSDL"""

	def callModule(self, moduleName, function):
		
		"""This function calls a module. moduleToLoad is the module to import,
		and functionToCall is the function to call from moduleToLoad."""
		
		moduleToLoad = moduleName
		functionToCall = function
		
		
