import ftplib
import subprocess
import time

while True:
	
	command = ('cp weber_ID.png homeVision_ID.png')
	subprocess.Popen(command, shell=True)

	global FTP
	session = ftplib.FTP('ftp.broi.it','vo10288@broi.it','rir38fe')
	#FTP.pwd()
	#FTP.cwd('htdocs')
	file = open('homeVision_ID.png','rb')                  # file to send
	session.storbinary('STOR htdocs/homeVision_ID.png', file)     # send the file
	session.quit()
	file.close()     
	time.sleep(30)
