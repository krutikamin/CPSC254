import string
import datetime
import socket
import os
import sys
from datetime import timedelta

fileRead = open(sys.argv[1], 'r')
#fileRead = open('test.html', 'r')
fileWrite = open(sys.argv[2], 'w')
#fileWrite = open('output.html', 'w')
dateString = '%DATE%'
hostnameString = '%HOSTNAME%'
uptimeString = '%UPTIME'

for line in fileRead:
	line.rstrip('\n')
	if(dateString in line):
		today = datetime.date.today()
		print today
		today = str(today)
		line.replace("%DATE", "today")
		print 'after removing %DATE%'	
		print line
		#print 'line after adding dateString'
		fileWrite.write(line)#print line
	elif(hostnameString in line):
		line.rstrip(hostnameString)
		import socket
		line = socket.gethostname()
		fileWrite.write(line)#print line
	elif(uptimeString in line):
		# from http://planzero.org/blog/2012/01/26/system_uptime_in_python,_a_better_way
		with open('/proc/uptime', 'r') as f:
			uptime_seconds = float(f.readline().split()[0])
			uptime_string = str(timedelta(seconds = uptime_seconds))

		fileWrite.write(uptime_string)#print(uptime_string)
	else:
		fileWrite.write(line)

fileRead.close()
fileWrite.close()
