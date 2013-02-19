#!/usr/bin/python
# smsread.py 
# by KrishnaChaitanya Yarramsetty
# www.foundstone.com



import sqlite3 as lite
import sys
import smtplib
import time


def sendEmail(msg):
	fromaddr = 'abc@gmail.com'
	toaddrs  = 'xyz@gmail.com'
	
	# Credentials 
	username = 'abc'
	password = '****'

	# The actual mail send snippet
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	server.login(username,password)
	server.sendmail(fromaddr, toaddrs, msg)
	server.quit()


#Set path for SMS directory
#smsfromaddress will be used a filter. filter restricts only to those sms that have FROM address as mentioned below. FROM addresses can be multiple as well.
#"address" is the column name.

smspath="/var/mobile/Library/SMS/"
smsfromaddress=('AXARWINF','6564567890',)

#Poll for any new messages waiting to be delivered in an infinite loop with 60 second interval. 
#though it is not one of the efficient methods, considering the purpose of the script it was taken for granted

while 1==1:
	#Connect to the database and read sms from 'message2' table.
	con = lite.connect(smspath+'sms.db')
	with con:
		con.row_factory = lite.Row
		cur = con.cursor()
		cur2 = con.cursor()
		cur.execute('SELECT * from message2 where emailsent=0 and address=?',smsfromaddress)
		rows = cur.fetchall()
		for row in rows:
			msg='Address is ' + row["address"] + '  Text Message is  ' + row["text"]			
			sendEmail(msg)
			ROWID = (row["ROWID"],)
			cur2.execute('UPDATE message2 SET emailsent=1 WHERE ROWID=?', ROWID)
		con.commit()
	time.sleep(60)


