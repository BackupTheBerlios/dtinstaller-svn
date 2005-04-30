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
  $rootpartend = (.15 * $mb);
  $homepartbeg = ($rootpartend + 1);
  $homepartend = (.50 * $mb + $rootpartend);
  $usrpartbeg = ($homepartend + 1);
  $usrpartend = (.30 * $mb + $homepartend);
  $swappartbeg = ($usrpartend +1);
  $swappartend = (.05 * $mb + $usrpartend);
  `parted -s $hd mkpart primary 0 $rootpartend` ;
  `parted -s $hd mkpart primary $homepartbeg $homepartend` ;
  `parted -s $hd mkpart primary $usrpartbeg $usrpartend` ;
  `parted -s $hd mkpartfs primary linux-swap $swappartbeg $swappartend` ;
  `mkfs.$fs -q $hd'1'`;
  `mkfs.$fs -q $hd'2'`;
  `mkfs.$fs -q $hd'3'`;
   print("Hah! $hd has been partition!\n");
} else {
 print("Layout not available\n");
 }
