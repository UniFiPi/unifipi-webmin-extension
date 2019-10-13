#!/usr/bin/perl

require './unifi-lib.pl';

&ui_print_header(undef, $text{'index_title'}, "", undef, 1, 1, 0,
	undef , undef, undef,
	&text('index_version', $version{'full'}));

print $text{'index_body'};


&ui_print_footer("/", $text{"index"});

