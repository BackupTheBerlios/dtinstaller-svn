# !/usr/bin/perl
# Exigo partition autolayout handler.
# By letme0ut ( letme0ut@exigo.distrotalk.net ).
# This code and software is licensed under the BSD License.
# For more details, see the LICENSE file in the source directory,
# or http://www.opensource.org/licenses/bsd-license.php on the Internet.

$hd = $ARGV[1] ;
$hd=~s/-//gi;
$fs = $ARGV[2] ;
if($ARGV[0] eq "-layout1") {
 $blocks = `sfdisk -s $hd` ;
 $mb = ($blocks / 1024);
 $end = ($mb - 256);
 $swaps = ($end + 1);
 $swape = ($mb - 10);
 `parted -s $hd rm 0` ;
 `parted -s $hd rm 1` ;
 `parted -s $hd rm 2` ;
 `parted -s $hd rm 3` ;
 `parted -s $hd mkpart primary 0 $end` ;
 `parted -s $hd mkpartfs primary linux-swap $swaps $swape`;
  print("Hah! $hd has been partitioned!\n");
} else {
 print("Layout not available\n");
 }
