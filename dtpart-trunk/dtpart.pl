#!/usr/bin/perl
# Exigo partition autolayout handler v 0.0.2
# By letme0ut ( letme0ut@exigo.distrotalk.net ).
# This code and software is licensed under the BSD License.
# For more details, see the LICENSE file in the source directory,
# or http://www.opensource.org/licenses/bsd-license.php on the Internet.

$hd = $ARGV[1] ;
$hd=~s/-//gi;
$fs = $ARGV[2] ;
if($fs eq "") { $fs = "reiserfs" };
 `parted -s $hd rm 8` ;
 `parted -s $hd rm 1` ;
 `parted -s $hd rm 2` ;
 `parted -s $hd rm 3` ;
 `parted -s $hd rm 4` ;
 `parted -s $hd rm 5` ;
 `parted -s $hd rm 6` ;
 `parted -s $hd rm 7` ;
if($ARGV[0] eq "-layout1") {
  $blocks = `sfdisk -s $hd` ;
  $mb = ($blocks / 1024);
  $end = ($mb - 256);
  $swaps = ($end + 1);
  $swape = ($mb - 10);
  `parted -s $hd mkpart primary 0 $end` ;
  `mkfs.$fs -q $hd'1'`;
  `parted -s $hd mkpartfs primary linux-swap $swaps $swape`;
   print("Hah! $hd has been partitioned!\n");
}elsif($ARGV[0] eq "-layout2"){
  $blocks = `sfdisk -s $hd` ;
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
  `parted -s $hd mkpartfs primary linux-swap $swappartbeg $swappartend` ;
  `parted -s $hd mkpart extended $bootpartbeg $usrpartend` ;
  `parted -s $hd mkpart logical $bootpartbeg $bootpartend` ;
  `parted -s $hd mkpart logical $homepartbeg $homepartend` ;
  `parted -s $hd mkpart logical $usrpartbeg $usrpartend` ;
  `mkfs.$fs -q $hd'1'`;
  `mkfs.$fs -q $hd'5'`;
  `mkfs.$fs -q $hd'6'`;
  `mkfs.$fs -q $hd'7'`;
   print("Hah! $hd has been partitioned!\n");
} else {
 print("Layout not available\n");
}
