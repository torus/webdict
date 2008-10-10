#!/usr/bin/env perl
# -*- coding: utf-8 -*-

use warnings;
use strict;

use CGI;
use CGI::Carp qw (fatalsToBrowser);

my $q = new CGI;

my $word = $ARGV[0] || $q->param('q');

print $q->header (-charset => "utf-8");

my $pid = open IN, "/usr/local/bin/sary '$word' /home/toru/src/eijiro/eijiro_all.utf8 |" or die;

print $q->start_ul;

for (1 .. 10) {
    my $l = <IN>;
    last unless $l;
    $l =~ s/^\^//;
    print $q->li ($q->escapeHTML ($l));
}

kill 15, $pid;
close IN;

print $q->end_ul;
