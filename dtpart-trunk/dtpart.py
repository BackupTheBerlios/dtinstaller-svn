#!/usr/bin/python
# Dtpart in python :-D
# Exigo partition autolayout handler redone in python v 0.0.2
# By letme0ut ( letme0ut@exigo.distrotalk.net ).
# This code and software is licensed under the BSD License.
# For more details, see the LICENSE file in the source directory,
# or http://www.opensource.org/licenses/bsd-license.php on the Internet.
# Syntax is ./dtpart.py -layout1 /dev/hdx filesystem-type
# Also if you really want to understand this program you will need to 
# read the man files on parted, sfdisk, and mkfs.

import os
import sys
import commands

argv = sys.argv
hd = argv[2]
fs = argv[3]
remove = 0
if argv[1] == "-layout3":
   remove = 1
if argv[1] == "-layout5":
   remove = 1
if remove != 1:
   os.system("parted -s "+hd+" rm 1")
   os.system("parted -s "+hd+" rm 2")
   os.system("parted -s "+hd+" rm 3")
   os.system("parted -s "+hd+" rm 4")
   os.system("parted -s "+hd+" rm 5")
   os.system("parted -s "+hd+" rm 6")
   os.system("parted -s "+hd+" rm 7")
   os.system("parted -s "+hd+" rm 8")
# Layout1 creates a big / partition and a 256mb swap partition.
if argv[1] == "-layout1":
   blocks = commands.getoutput("sfdisk -s "+hd)
   mb = int(blocks) / 1024
   end = mb - 256
   swapbeg = end + 1
   swapend = mb
   os.system("parted -s "+hd+" mkpart primary 0 "+str(end))
   os.system("parted -s "+hd+" mkpartfs primary linux-swap "+str(swapbeg)+" "+str(swapend))
   os.system("mkfs."+fs+" -q "+hd+"1")
   print "Hah! "+hd+" has been partitioned!!!"
   print mb
   print swapend
   print blocks
# Phew!! Python is a bitch!
# Layout 2 creates a big home partition and a big usr partition.
# It also creates a swap using 5% of the drive
# and a small boot partition is also created using another 5% of the drive
if argv[1] == "-layout2":
   blocks = commands.getoutput("sfdisk -s "+hd)
   mb = int(blocks) / 1024
   rootpartend = 0.10 * mb
   swappartbeg = rootpartend + 1
   swappartend = 0.05 * mb + rootpartend
   bootpartbeg = swappartend + 1
   bootpartend = 0.05 * mb + swappartend
   homepartbeg = bootpartend + 1
   homepartend = 0.5 * mb + bootpartend
   usrpartbeg = homepartend + 1
   usrpartend = 0.3 * mb + homepartend
   os.system("parted -s "+hd+" mkpart primary 0 "+str(rootpartend))
   os.system("parted -s "+hd+" mkpartfs primary linux-swap "+str(swappartbeg)+" "+str(swappartend))
   os.system("parted -s "+hd+" mkpart extended "+str(bootpartbeg)+" "+str(usrpartend))
   os.system("parted -s "+hd+" mkpart logical "+str(bootpartbeg)+" "+str(bootpartend))
   os.system("parted -s "+hd+" mkpart logical "+str(homepartbeg)+" "+str(homepartend))
   os.system("parted -s "+hd+" mkpart logical "+str(usrpartbeg)+" "+str(usrpartend))
   os.system("mkfs."+fs+" -q "+hd+"1")
   os.system("mkfs."+fs+" -q "+hd+"5")
   os.system("mkfs."+fs+" -q "+hd+"6")
   os.system("mkfs."+fs+" -q "+hd+"7")
   print "Hah! "+hd+" has been partitioned!!!"
# Layout 3.
# Windows resizing starts here.
# NOTICE: Only works on fat32 partitions!!!
# Resizes the Windows partition to 60% of the drive,
# and creates a root partition using 37%.
# The rest is used for linux-swap.
if argv[1] == "-layout3":
   blocks = commands.getoutput("sfdisk -s "+hd)
   mb = int(blocks) / 1024
   winpartend = 0.60 * mb
   
