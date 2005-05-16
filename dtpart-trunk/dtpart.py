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

import sys
from os import system
from commands import getoutput

argv = sys.argv
hd = argv[2]
fs = argv[3]

# Checking to see if the layout needs to delete all existing 
# partitions first.
remove = 0
if argv[1] == "-layout3":
   remove = 1
if argv[1] == "-layout5":
   remove = 1
if remove != 1:
   system("parted -s "+hd+" rm 1")
   system("parted -s "+hd+" rm 2")
   system("parted -s "+hd+" rm 3")
   system("parted -s "+hd+" rm 4")
   system("parted -s "+hd+" rm 5")
   system("parted -s "+hd+" rm 6")
   system("parted -s "+hd+" rm 7")
   system("parted -s "+hd+" rm 8")
   
# Layout1 creates a big / partition and a 256mb swap partition.
if argv[1] == "-layout1":
   blocks = getoutput("sfdisk -s "+hd)
   mb = int(blocks) / 1024
   end = mb - 256
   swapbeg = end + 1
   swapend = mb
   system("parted -s "+hd+" mkpart primary 0 "+str(end))
   system("parted -s "+hd+" mkpartfs primary linux-swap "+str(swapbeg)+" "+str(swapend))
   system("mkfs."+fs+" -q "+hd+"1")
   print "Hah! "+hd+" has been partitioned!!!"
   
# Phew!! Python is a bitch!
# Layout 2 creates a big home partition and a big usr partition.
# It also creates a swap using 5% of the drive
# and a small boot partition is also created using another 5% of the drive
if argv[1] == "-layout2":
   blocks = getoutput("sfdisk -s "+hd)
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
   system("parted -s "+hd+" mkpart primary 0 "+str(rootpartend))
   system("parted -s "+hd+" mkpartfs primary linux-swap "+str(swappartbeg)+" "+str(swappartend))
   system("parted -s "+hd+" mkpart extended "+str(bootpartbeg)+" "+str(usrpartend))
   system("parted -s "+hd+" mkpart logical "+str(bootpartbeg)+" "+str(bootpartend))
   system("parted -s "+hd+" mkpart logical "+str(homepartbeg)+" "+str(homepartend))
   system("parted -s "+hd+" mkpart logical "+str(usrpartbeg)+" "+str(usrpartend))
   system("mkfs."+fs+" -q "+hd+"1")
   system("mkfs."+fs+" -q "+hd+"5")
   system("mkfs."+fs+" -q "+hd+"6")
   system("mkfs."+fs+" -q "+hd+"7")
   print "Hah! "+hd+" has been partitioned!!!"
   
# Layout 3.
# Windows resizing starts here.
# NOTICE: Only works on fat32 partitions!!!
# Resizes the Windows partition to 60% of the drive,
# and creates a root partition using 37%.
# The rest is used for linux-swap.
if argv[1] == "-layout3":
   blocks = getoutput("sfdisk -s "+hd)
   mb = int(blocks) / 1024
   winpartend = 0.60 * mb
   system("parted -s "+hd+" resize 1 0 "+str(winpartend))
   rootpartbeg = 0.60 * mb + 1
   rootpartend = 0.37 * mb + rootpartbeg
   swappartbeg = rootpartend + 1
   swapparteng = 0.03 * mb + rootpartend
   system("parted -s "+hd+" mkpart primary "+str(rootpartbeg)+" "+str(rootpartend))
   system("parted -s "+hd+" mkpartfs primary linux-swap "+str(swappartbeg)+" "+str(swappartend))
   system("mkfs."+fs+" -q "+hd+"2")
   print "Hah! "+hd+" has been partitioned!!!"
   
# Layout 4.
# Web server layout, creates a large /var partition,
# and creates a %40 of hard drive / partition, as well as a %10 swap.
if argv[1] == "-layout4":
   blocks = getoutput("sfdisk -s "+hd)
   mb = int(blocks) / 1024
   rootpartend = 0.40 * mb
   varpartbeg = rootpartend + 1
   varpartend = 0.50 * mb + rootpartend
   swappartbeg = varpartend + 1
   swappartend = 0.10 * mb + varpartend
   system("parted -s "+hd+" mkpart primary 0 "+str(rootpartend))
   system("parted -s "+hd+" mkpart primary "+str(varpartbeg)+" "+str(varpartend))
   system("parted -s "+hd+" mkpartfs primary linux-swap "+str(swappartbeg)+" "+str(swappartend))
   system("mkfs."+fs+" -q "+hd+"1")
   system("mkfs."+fs+" -q "+hd+"2")
   print "Hah! "+hd+" has been partitioned!!!"

# Layout 5.
# Used for a hard drive that already has unpartitioned space.
# Creates a / partition using 95% of the free space.
# Creates a swap using the remaing 5% of the free space.
# Only works if at least 100 mb are free.
# Once again only works if there are no more than 3 primary partitions and 0 extended ones. 
if argv[1] == "-layout5":
   total = getoutput("sfdisk -s "+hd)
   totalmb = int(total) / 1024
   p10 = getoutput("sfdisk -s "+hd+"10")
   p9 = getoutput("sfdisk -s "+hd+"9")
   p8 = getoutput("sfdisk -s "+hd+"8")
   p7 = getoutput("sfdisk -s "+hd+"7")
   p6 = getoutput("sfdisk -s "+hd+"6")
   p5 = getoutput("sfdisk -s "+hd+"5")
   p4 = getoutput("sfdisk -s "+hd+"4")
   p3 = getoutput("sfdisk -s "+hd+"3")
   p2 = getoutput("sfdisk -s "+hd+"2")
   p1 = getoutput("sfdisk -s "+hd+"1")
   used = int(p1) + int(p2) + int(p3) + int(p4) + int(p5) + int(p6) + int(p7) + int(p8) + int(p9) + int(p10)
   usedmb = used / 1024
   free = totalmb - usedmb
   rootpartbeg = usedmb + 1
   rootpartend = 0.95 * free + rootpartbeg
   swappartbeg = rootpartend + 1
   swappartend = 0.05 * free + rootpartend
   if free > 100:
      system("parted -s "+hd+" mkpart extended "+str(rootpartbeg)+" "+str(swappartend))
      system("parted -s "+hd+" mkpart logical "+str(rootpartbeg)+" "+str(rootpartend))
      system("parted -s "+hd+" mkpartfs logical linux-swap "+str(swappartbeg)+" "+str(swappartend))
      system("mkfs."+fs+" -q "+hd+"5")
      print "Hah! "+hd+" has been partitioned!"
   else:
      print"Hah! "+hd+" has not been partitioned! not enough space!"
