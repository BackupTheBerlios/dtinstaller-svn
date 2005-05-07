#!/usr/bin/perl
# Exigo partition autolayout handler v 0.0.3
# By letme0ut ( letme0ut@exigo.distrotalk.net ).
# This code and software is licensed under the BSD License.
# For more details, see the LICENSE file in the source directory,
# or http://www.opensource.org/licenses/bsd-license.php on the Internet.
# Syntax is ./dtpart.pl <-layout1> /dev/hdx <filesystem-type>

$hd = $ARGV[1];
$hd=~s/-//gi;
$fs = $ARGV[2];
# Sets the default filesystem to reiserfs.
if($fs eq "") { $fs = "reiserfs" };
# Deletes old partitions to make room for new ones,
# unless you select layout3 which resizes an existing partition.
if($ARGV[0] ne "-layout3") {
  `parted -s $hd rm 1`;
  `parted -s $hd rm 2`;
  `parted -s $hd rm 3`;
  `parted -s $hd rm 4`;
  `parted -s $hd rm 5`;
  `parted -s $hd rm 6`;
  `parted -s $hd rm 7`;
  `parted -s $hd rm 8`;}
# Layout1 creates a big / partition and a 256mb swap partition.
if($ARGV[0] eq "-layout1") {
   $blocks = `sfdisk -s $hd` ;
   $mb = ($blocks / 1024) ;
   $end = ($mb - 256) ;
   $swaps = ($end + 1);
   $swape = ($mb - 10);
   `parted -s $hd mkpart primary 0 $end`;
   `mkfs.$fs -q $hd'1'`;
   `parted -s $hd mkpartfs primary linux-swap $swaps $swape`;
    print("Hah! $hd has been partitioned!\n");
# Layout 2 creates a big home partition and a big usr partition.
# It also creates a swap using 5% of the drive
# and a small boot partition is also created using another 5% of the drive
}elsif($ARGV[0] eq "-layout2"){
   $blocks = `sfdisk -s $hd`;
   $mb = ($blocks / 1024);
   $rootpartend = (.10 * $mb);
   $swappartbeg = ($rootpartend +1);
   $swappartend = (.05 * $mb + $rootpartend);
   $bootpartbeg = ($swappartend +1);
   $bootpartend = (.05 * $mb + $swappartend);
   $homepartbeg = ($bootpartend + 1);
   $homepartend = (.50 * $mb + $bootpartend);
   $usrpartbeg = ($homepartend + 1);
   $usrpartend = (.30 * $mb + $homepartend);
   `parted -s $hd mkpart primary 0 $rootpartend` ;
   `parted -s $hd mkpartfs primary linux-swap $swappartbeg $swappartend`;
   `parted -s $hd mkpart extended $bootpartbeg $usrpartend`;
   `parted -s $hd mkpart logical $bootpartbeg $bootpartend`;
   `parted -s $hd mkpart logical $homepartbeg $homepartend`;
   `parted -s $hd mkpart logical $usrpartbeg $usrpartend`;
   `mkfs.$fs -q $hd'1'`;
   `mkfs.$fs -q $hd'5'`;
   `mkfs.$fs -q $hd'6'`;
   `mkfs.$fs -q $hd'7'`;
    print("Hah! $hd has been partitioned!\n");
# Layout 3.
# Windows resizing starts here.
# NOTICE: Only works on fat32 partitions!!!
# Resizes the Windows partition to 60% of the drive,
# and creates a root partition using 37%.
# The rest is used for linux-swap.
}elsif($ARGV[0] eq "-layout3"){
   $blocks = `sfdisk -s $hd`;
   $mb = ($blocks / 1024); 
   $winpartend = (.60 * $mb);
   `parted -s $hd resize 1 0 $winpartend`;
   $rootpartbeg = (.60 * $mb + 1);
   $rootpartend = (.37 * $mb + $rootpartbeg);
   $swappartbeg = ($rootpartend + 1);
   $swappartend = (.03 * $mb + $rootpartend);
   `parted -s $hd mkpart primary  $rootpartbeg $rootpartend`;
   `parted -s $hd mkpartfs primary linux-swap $swappartbeg $swappartend`;
   `mkfs.$fs -q $hd'2'`;
    print("Hah! $hd has been partitioned!\n");
# Layout 4.
# Web server layout, creates a large /var partition,
# and creates a %40 of hard drive / partition, as well as a %10 swap.
}elsif($ARGV[0] eq "-layout4"){
   $blocks = `sfdisk -s $hd`;
   $mb = ($blocks / 1024);
   $rootpartend = (.40 * $mb);
   $varpartbeg = ($rootpartend + 1);
   $varpartend = (.50 * $mb + $rootpartend);
   $swappartbeg = ($varpartend + 1);
   $swappartend = (.10 * $mb + $varpartend);
   `parted -s $hd mkpart primary 0 $rootpartend`;
   `parted -s $hd mkpart primary $varpartbeg $varpartend`;
   `parted -s $hd mkpartfs primary linux-swap $swappartbeg $swappartend`;
   `mkfs.$fs -q $hd'1'`;
   `mkfs.$fs -q $hd'2'`;
    print("Hah! $hd has been partitioned!\n");
# If no correct layout was given: 
}else{ print("Layout not available\n")}
