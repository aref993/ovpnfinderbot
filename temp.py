# -*- coding: utf-8 -*-
import StringIO
import json
import logging
import random
import urllib
import urllib2
import os
import base64,re
import csv,io


rawdata=open("/home/aref/Desktop/vpngate.txt",'rb')
vpngate=rawdata.read()
p = re.compile('^\w+')
c = re.compile(',').split(vpngate)
#print c[28].split("\n")[0]
vpngate=vpngate.replace("*","")
myfile= io.BytesIO(vpngate)
with myfile as csvfile:
	reader=csv.reader(csvfile,delimiter=',')
	
	next(reader)
	next(reader)
	for row in reader:
		try:
			if int(row[2])>200000 and int(row[2])<400000 and int(row[7])>0 and int(row[3])<100:
				filename=row[6]+"-"+row[1]+".ovpn"
				print row[2]+","+row[7]+","+row[5]
		except Exception as e:
			break
		else:
			pass
		finally:
			pass
#print base64.b64decode(c[42].split("\n")[0])
#print c[33]+"-"+c[29]
