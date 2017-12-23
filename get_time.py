import subprocess
import smtplib
from email.mime.text import MIMEText


SERVER = "localhost"
while True:

    ## get the baxter time
#    cmd = "ssh baxter 'date +%s%N'"
#    out_baxter = subprocess.check_output(cmd, shell=True)
#
#    cmd = "date +%s%N"
#    out = subprocess.check_output(cmd, shell=True)
#    print " baxter_time =" ,out_baxter[:-1], " system_time = ", out[:-1], " diff = " ,int(out_baxter[:-1]) - int(out[:-1]) , " nsec"
#    '''if int(out_baxter[:-1]) - int(out[:-1]) > 45116473:

	  #with open("textfile.txt", 'rb') as fp:
    	  # Create a text/plain message
    	  msg = MIMEText(fp.read())
	  msg['Subject'] = 'The contents of %s' 
          msg['From'] =" lekhaemerald@gmail.com"
          msg['To'] = "lekhaemerald@gmail.com"
          # envelope header.
	  s = smtplib.SMTP('localhost')
          s.sendmail(me, [you], msg.as_string())
          s.quit()
          FROM = "lekhaemerald@gmail.com"
          TO = ["lekhaemerald@gmail.com"] # must be a list
          message = "check NTP"
          server = smtplib.SMTP(SERVER)
          server.sendmail(FROM,TO,message)
          server.quit()
    '''	
    
