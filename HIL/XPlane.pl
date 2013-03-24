#!/usr/bin/perl -w

use strict;
use IO::Socket;
use IO::Select;
$| = 1;

use constant DATA_num_channels => 113;
use constant DATA_num_elements => 8;
use constant DATA_header_size	=> 5;
use constant DATA_packet_size	=> DATA_num_channels * DATA_num_elements + DATA_header_size;
use constant DATA_max_element	=> 7;
use constant DATA_element_size => (DATA_num_elements + 1) * 4; # 4-byte elements
use constant DATA_inbound_pack => "A4c";
use constant DATA_inbound_header => ('DATA',0);

my $rh;
my $x_plane_ip		= '127.0.0.1';
my $ser_port	 	= 5331;
my $receive_port	= 49005;
my $transmit_port	= 49000;
my $destination_os = 'Mac';
my $throttle_test = 0;
my $check_a = 0;
my $check_b = 0;
my $count = 0;

my $roll_out = 0;
my $pitch_out = 0;
my $throttle_out = 0;
my $wp_distance = 0;
my $wp_index = 0;
my $control_mode = 0;
my $bearing_error = 0;

my $diyd_header = "DIYd";

my $Xplane_in_sock = IO::Socket::INET->new(
	LocalPort => $receive_port,
	LocalAddr => $x_plane_ip,
	Proto		 => 'udp')
	or die "error creating receive port for $x_plane_ip: $@\n";

my $receive = IO::Select->new();


my $Xplane_out_sock = IO::Socket::INET->new(
	PeerPort	=> $transmit_port,
	PeerAddr	=> $x_plane_ip,
	ReusePort => 1,
	Proto		 => 'udp')
	or die "error creating transmit port for $x_plane_ip: $@\n";

my $transmit = IO::Select->new();



#open sockets on 7070
my $arduSocket = IO::Socket::INET->new(	Proto => 'tcp',
											PeerAddr =>	'127.0.0.1',
										   	PeerPort => $ser_port
										   	) or die $!;
										   	#,Type = 'SOCK_STREAM'
										   	
										   	
$receive->add($Xplane_in_sock);
$transmit->add($Xplane_out_sock);
$receive->add($arduSocket);
$arduSocket->autoflush(1);




my $DATA_buffer = {};

# These formats are represented by X-Plane as floating point
#
my @float_formats = qw( f deg mph pct );

# {{{ Field type formats
# Some fields need special formatting.
#
#my $typedef = {
#	deg => { format => "%+03.3f", len => 8 },
#	mph => { format => "%03.3f", len => 7 },
#	pct => { format => "%+01.3f", len => 6 },
#};

# {{{ The DATA packet structure
#
# The packet header goes on later.
#
my $DATA_packet = {
	# The outer hash reference contains a sparse array of data frames
	0 => {
		# The inner hash reference contains a sparse array of data elements
		0 => { type => 'f', label => 'Frame Rate'},
	},
	
	3 => {
		6 => { type => 'f', label => 'Air Speed'},
		7 => { type => 'f', label => 'Ground Speed'},
	},
	
	#12 => {
	#	0 => { type => 'bool', label => 'Gear'},
	#	1 => { type => 'f', label => 'Brakes'},
	#},
	8 => {
		0 => { type => 'deg', label => 'Pitch'},
		1 => { type => 'deg', label => 'Roll'},
		2 => { type => 'deg', label => 'heading'},
	},
	
	11 => {
		0 => { type => 'f', label => 'elev'},
		1 => { type => 'f', label => 'aileron'},
	},
	18 => {
		0 => { type => 'deg', label => 'Pitch'},
		1 => { type => 'deg', label => 'Roll'},
		2 => { type => 'deg', label => 'heading'},
	},
	
	20 => {
		0 => { type => 'deg', label => 'Latitude'},
		1 => { type => 'deg', label => 'Longitude'},
		2 => { type => 'f', label => 'Altitude'},
	},
	
	25 => {
		0 => { type => 'deg', label => 'Throttle cmd'},
	},
	26 => {
		0 => { type => 'deg', label => 'Throttle'},
	},

};


# X-Plane uniformly sends 4-byte floats outbound,
# but accepts a mixture of floats and integers inbound.

sub create_pack_strings {
	for my $row (values %$DATA_packet) {
		$row->{unpack} = 'x4';
		$row->{pack} = 'l';
		for my $j (0..DATA_max_element) {
			if(exists $row->{$j}) {
				my $col = $row->{$j};
				$row->{pack} .= (grep { $col->{type} eq $_ } @float_formats) ? 'f' : 'l';
				$row->{unpack} .= 'f';
			}
			else {
				$row->{pack} .= 'f';
				$row->{unpack} .= 'x4';
			}
		}
	}
}


# {{{ Transmit a message
sub transmit_message {
	my ($socket,$pack_format,@message) = @_;
	my ($server) = $socket->can_write(60);
	$server->send(pack($pack_format,@message));
}


sub receive_DATA 	{
	my ($message) = @_;
	$DATA_buffer = { };
	for (my $i = 0; $i < (length($message) - &DATA_header_size - 1) / DATA_element_size; $i++) {
		my $channel = substr($message, $i * DATA_element_size + DATA_header_size, DATA_element_size);

		my $index = unpack "l", $channel;
		next unless exists $DATA_packet->{$index};

		my $row = $DATA_packet->{$index};
		my @element = unpack $row->{unpack}, $channel;
		my $ctr = 0;
		for my $j (0..DATA_max_element) {
			next unless exists $row->{$j};
			my $col = $row->{$j};
			$DATA_buffer->{$index}{$j} = $element[$ctr];
			#print "row ".$row ." ";
			
			#print "index ".$index ." ";
			#print $element[$ctr]."\n";
			$ctr++;
		}
	}
}



# {{{ transmit_DATA
sub transmit_DATA {
	my ($socket, @message) = @_;
	my $pack_str = DATA_inbound_pack;
	for(my $packet = 0;
		$packet < @message;
		$packet += (DATA_num_elements + 1)) {
		$pack_str .= $DATA_packet->{$message[$packet]}{pack};
	}
	transmit_message($socket,$pack_str,DATA_inbound_header,@message,0);
}


# {{{ Fill in a DATA channel
sub _fill_channel {
	my ($packet) = @_;
	my @buffer = (-999) x DATA_num_elements;
	for(0..7) {
		$buffer[$_] = $packet->{$_} if defined $packet->{$_};
	}
	return @buffer;
}


# {{{ Send outbound messages if there are any
sub transmit_socket {
	my ($socket,$ch) = @_;
	if($ch eq 'g') {
		transmit_DATA($socket, 12, $DATA_buffer->{12}{0} ? 0 : 1,(-999) x 7);

	}elsif($ch eq 't') {
		transmit_DATA($socket, 25, $throttle_out,(-999) x 7);

	}elsif($ch eq 'c') {
		transmit_DATA($socket, 11, $pitch_out, $roll_out, $roll_out*.2 , (-999), ($roll_out * 5) , -999, -999, -999 );

	}elsif($ch eq 'j') {
		transmit_DATA($socket, 8, $pitch_out, $roll_out, $roll_out*.2 , (-999) x 5);

	}elsif($ch eq 'i') {
		my @engine = map { $_ != -999 ? $_ + 0.1 : -999 } _fill_channel($DATA_buffer->{23});
		transmit_DATA( $socket, 23, @engine );

	}elsif($ch eq 'k') {
		my @engine =
			map { $_ != -999 ? $_-0.1 : -999 }
			_fill_channel($DATA_buffer->{23});
		transmit_DATA( $socket, 23, @engine );
	}
}


sub parseXplane {
	
	#convert data	
	my $lat 		= int($DATA_buffer->{20}{0} * 10000000);
	my $lng 		= int($DATA_buffer->{20}{1} * 10000000);
	my $altitude 	= int($DATA_buffer->{20}{2} * 3.048);		# altitude to meters
	my $speed 		= int($DATA_buffer->{3}{7} * 044.704);		# spped to meters/s
	my $airspeed 	= int($DATA_buffer->{3}{6} * 044.704);		# speed to meters/s
	my $pitch 		= int($DATA_buffer->{18}{0} * 100);
	my $roll 		= int($DATA_buffer->{18}{1} * 100);
	my $heading 	= int($DATA_buffer->{18}{2} * 100);
	
	#$pitch = 30;
	#$roll = 30;
	#$heading = 30;
	
	# format and publish the IMU style data to the Ardupilot
	my $outgoing = pack("CCs<3", 6,2, $roll, $pitch, $heading);
	$check_a = $check_b = 0;
	for( split(//,$outgoing) )
	{
		$check_a += ord;
		$check_a %= 256;
		$check_b += $check_a;
		$check_b %= 256;
		#print ord . "\n";
	}
	$outgoing = pack("a4CCs<3CC","DIYd", 6,2, $roll, $pitch, $heading,$check_a,$check_b);
	$arduSocket->send($outgoing);
	#print $outgoing . "\0";

	#my ($server) = $socket->can_write(60);
	#$server->send(pack($pack_format,@message));
	$count++;
	#my $mod = $count % 10;
	#print"$count .";
	if ($count == 10){
		#print"count $count \n";
		$count = 0;
		$outgoing = pack("CCl<2s<3", 14,3, $lng, $lat, $altitude, $speed, $heading);
		$check_a = $check_b = 0;
		for( split(//,$outgoing) )
		{
			$check_a += ord;
			$check_a %= 256;
			$check_b += $check_a;
			$check_b %= 256;
			#print ord . "\n";
		}
		$outgoing = pack("a4CCl<2s<3CC","DIYd", 14,3, $lng, $lat, $altitude, $speed, $heading, $check_a, $check_b);
		$arduSocket->send($outgoing);
		#print $outgoing . "\0";
	}
	$count = 0 if ($count > 50);
	
	#$throttle_test += .05;
	#if ($throttle_test > 1){
	#	$throttle_test = 0;
	#}
	
	#print "altitude $DATA_buffer->{20}{2} \n";
	#print "speed $DATA_buffer->{3}{7} \n";
	
}
sub parseMessage
{
	my ($data) = @_;
	#my($junk,$data) = split /AAA/,$message;
	#if($data){
	my @out = unpack("s5C2",$data);
	
	$roll_out = $out[0] *1 / 45  if (defined $out[0]);
	$roll_out = 1 if($roll_out > 1);
	$roll_out = -1 if($roll_out < -1);
	
	$pitch_out = $out[1] *1 / 45  if (defined $out[1]);
	$pitch_out = 1 if($pitch_out > 1);
	$pitch_out = -1 if($pitch_out < -1);

	$throttle_out = $out[2] * 1.2 / 100  if (defined $out[2]);


	$wp_distance = $out[3] * 1  if (defined $out[3]);
	$bearing_error = $out[4] / 100  if (defined $out[4]);
	$wp_index = $out[5]*1  if (defined $out[5]);
	if (defined $out[6]){
		$control_mode = $out[6]*1;

		SWITCH: {
		  $control_mode == 0 && do { $control_mode = "Manual"; last SWITCH; };
		  $control_mode == 1 && do { $control_mode = "CIRCLE"; last SWITCH; };
		  $control_mode == 2 && do { $control_mode = "STABILIZE"; last SWITCH; };
		  $control_mode == 3 && do { $control_mode = "FLY_BY_WIRE_A"; last SWITCH; };
		  $control_mode == 4 && do { $control_mode = "FLY_BY_WIRE_B"; last SWITCH; };
		 #$control_mode == 5 && do { $control_mode = "Manual"; last SWITCH; };
		  $control_mode == 6 && do { $control_mode = "AUTO"; last SWITCH; };
		  $control_mode == 7 && do { $control_mode = "RTL"; last SWITCH; };
		  $control_mode == 8 && do { $control_mode = "LOITER"; last SWITCH; };
		  $control_mode == 9 && do { $control_mode = "TAKEOFF"; last SWITCH; };
		  $control_mode == 10 && do{ $control_mode = "LAND"; last SWITCH; };
		}
	}	
	#print "ro: $roll_out po: $pitch_out to: $throttle_out wp_dist:$wp_distance bearing_err:$bearing_error mode:$control_mode\n";
	if ($count == 9){
		print "wp_dist: $wp_distance,   bearing_err: $bearing_error,   WP: $wp_index,   mode: $control_mode\n";
	}
	#print "roll_out $roll_out, pitch_out $pitch_out, throttle_out $throttle_out \n";
	transmit_socket($transmit,'t');
	transmit_socket($transmit,'j');
	transmit_socket($transmit,'c');
	#}
}

#!	IMU Message format
#!	Byte(s)		 Value
#!	0-3		 Header "DIYd"
#!	4						Payload length	= 6
#!	5						Message ID = 2
#!	6,7			roll		Integer (degrees*100)
#!	8,9			pitch		Integer (degrees*100)
#!	10,11		yaw			Integer (degrees*100)
#!	12,13					checksum
#!	
#!	
#!	GPS Message format
#!	Byte(s)		 Value
#!	0-3		 Header "DIYd"
#!	4								Payload length = 14
#!	5								Message ID = 3
#!	6-9			longitude			Integer (value*10**7)
#!	10-13		latitude			Integer (value*10**7)
#!	14,15		altitude			Integer (meters*10)
#!	16,17		gps speed			Integer (M/S*100)
#!	18,19		gps course			not used
#!	20,21		checksum

sub main_loop {
	my ($receive,$transmit) = @_;
	#my ($receive) = @_;
	my $recv_data = "";

	while(1) {
		#if(my $ch = $win->getch()) {
		 # last if $ch =~ /q/i;
			#transmit_socket($transmit,$ch);
		#}
	
		my ($rh_set) = IO::Select->select($receive, undef, undef, .1);


		foreach $rh (@$rh_set) {
			if ($rh == $Xplane_in_sock) {
				my $message;
				$rh->recv($message,DATA_packet_size);
				#print $message."\n";
				#print ".. \n";
				receive_DATA($message);
				parseXplane();
				
			}elsif ($rh == $arduSocket) {
				my $message = '';
				my $message2= '';
				
				$rh->recv($message,400);
				if($message =~ "\n"){
				
				}else{
					#print "!\n";
					$rh->recv($message2,100);
					$message .= $message2;
				}
				if($message =~ '^AAA'){
					$message = substr $message, 3, 12; 
					parseMessage($message);
				}elsif($message =~ '^XXX'){
					print ": $message ". time."\n";
				}else{
					#print "er:$message \n";
				}
				$rh->flush();
				#print "$message \n";
			}
		}

			#print time."\n";
			#print "in:${message}-";
		#
		#$arduSocket->recv($recv_data,12);
		#chop $recv_data;
		#if($recv_data){

	}
}

create_pack_strings();
main_loop($receive, $transmit);
