#!/usr/bin/env python

# This is the CLUI of the dtinstaller for Exigo Linux.

# Copyright (c) 2005 David Kimpe <DNAku at Exigo.DistroTalk.net>
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

def mainCLUI():
        from time import sleep
        import curses
	import os
        stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        stdscr.keypad(1)

        # str
        #stdscr.addstr( "The staff of DistroTalk.net presents:"; curses.color_pair(1) )
        #stdscr.refresh()

        def addText(text):
                stdscr.addstr(text)

        sleep(1)
        addText("\n")
        addText(" _____ _   _ __  _____   ___  \n")
        addText("|__ __| | | |\ \/ / _ \ / __| \n")
        addText("  | | | | | | \  /|| | |  \_  \n")
        addText("  | | | |_| | /  \||_| |\__ | \n")
        addText("  |_| |_____|/_/\_\___//____/ \n")
        addText("\n")
        stdscr.refresh()
        sleep(2)
        addText("cli installer\n")
        addText("\n")
        stdscr.refresh()
        sleep(5)

        curses.endwin()

        #sleep(1)

        print "What partition do you want to install TuxOS on?\n"
	part = raw_input("Choose the partition you want to use.\n>")
	print "the partition %s will be used as the partition to install the base system" %part
	partverify = raw_input("Are you sure you want to install TuxOS on %s? (y/n)\n>" %part)
	if partverify == "y":
		print "TuxOS base-system will be installed on %s" %part
		os.popen("cp /media/cdrom /mnt/%s" %part)
		sleep(2)
		resp = raw_input("What keyboard lay-out do you want to use?\n>")
        	print
        	print "You are using the keyboard layout: %s\n" %resp
        	lay = raw_input("Is this ok? (y/n)\n>")
        	if lay == "y":
			print "\nThank you for testing the pre-alpha of dtinstaller.\n"
			import sys
			sys.exit()
        	elif lay == "n":
			print "This option is not available yet,\n"
			print "Thank you for testing the pre-alpha of dtinstaller! :)\n"
			import sys
			sys.exit()
		else:	
			print "This is not a valid option" 
			import sys
			sys.exit()
	else:
		print "This is not a valid option" 
