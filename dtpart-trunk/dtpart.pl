#!/usr/bin/perl
# Exigo partition autolayout handler v 0.0.4
# By letme0ut ( letme0ut@exigo.distrotalk.net ).
# This code and software is licensed under the BSD License.
# For more details, see the LICENSE file in the source directory,
# or http://www.opensource.org/licenses/bsd-license.php on the Internet.
# Syntax is ./dtpart.pl -layout1 /dev/hdx filesystem-type
# Also if you really want to understand this program you will need to 
# read the man files on parted, sfdisk, and mkfs.

$hd = $ARGV[1];
$hd=~s/-//gi;
$fs = $ARGV[2];
# Sets the default filesystem to reiserfs.
if($fs eq "") { $fs = "reiserfs" };
# Deletes old partitions to make room for new ones,
# unless you select layout3 which resizes an existing partition.
if($ARGV[0] eq "-layout3"){$remove = 1}
if($ARGV[0] eq "-layout5"){$remove = 1}
if($remove != 1) {
  `parted -s $hd rm 1`;
  `parted -s $hd rm 2`;
  `parted -s $hd rm 3`;
  `parted -s $hd rm 4`;
  `parted -s $hd rm 5`;
  `parted -s $hd rm 6`;
  `parted -s $hd rm 7`;
  `parted -s $hd rm 8`;}
 Layout1 creates a big / partition and a 256mb swap partition.
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
# Layout 5.
# Used for a hard drive that already has unpartitioned space.
# Creates a / partition using 95% of the free space.
# Creates a swap using the remaing 5% of the free space.
# Only works if at least 100 mb are free.
# Once again only works if there are no more than 3 primary partitions and 0 extended ones.
}elsif($ARGV[0] eq "-layout5"){
    $total = `sfdisk -s $hd`;
    $totalmb = ($total / 1024);
    $p10 = `sfdisk -s $hd'10'`; if($p10 == 0){$lastpart = 10}
    $p9 = `sfdisk -s $hd'9'`; if($p9 == 0){$lastpart = 9}
    $p8 = `sfdisk -s $hd'8'`; if($p8 == 0){$lastpart = 8}
    $p7 = `sfdisk -s $hd'7'`; if($p7 == 0){$lastpart = 7}
    $p6 = `sfdisk -s $hd'6'`; if($p6 == 0){$lastpart = 6}
    $p5 = `sfdisk -s $hd'5'`; if($p5 == 0){$lastpart = 5}
    $p4 = `sfdisk -s $hd'4'`; if($p4 == 0){$lastpart = 4}
    $p3 = `sfdisk -s $hd'3'`; if($p3 == 0){$lastpart = 3}
    $p2 = `sfdisk -s $hd'2'`; if($p2 == 0){$lastpart = 2}
    $p1 = `sfdisk -s $hd'1'`; if($p1 == 0){$lastpart = 1}
    $used = ($p1 + $p2 + $p3 + $p4 + $p5 + $p6 + $p7 + $p8 + $p9 + $p10);
    $usedmb = ($used / 1024);
    $free = ($totalmb - $usedmb);
    $rootpartbeg = ($usedmb + 1);
    $rootpartend = (.95 * $free + $rootpartbeg);
    $swappartbeg = ($rootpartend + 1);
    $swappartend = (.05 * $free + $rootpartend);
    if($free > 100){
    `parted -s $hd mkpart extended $rootpartbeg $swappartend`;
    `parted -s $hd mkpart logical $rootpartbeg $rootpartend`;
    `parted -s $hd mkpartfs logical linux-swap $swappartbeg $swappartend`;
    `mkfs.$fs -q $hd'5'`;
     print("Hah! $hd has been partitioned! 1st part made: $lastpart free space: $free used: $usedmb \n");
     }else{print("Hah! $hd has not been partitioned! not enough space!\n");
# If no correct layout was given: 
}}else{ print("Layout not available\n")}
