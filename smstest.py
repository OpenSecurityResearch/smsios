#!/usr/bin/python
# smstest.py
# by KrishnaChaitanya Yarramsetty
# www.foundstone.com

import sqlite3 as lite
import sys
import smtplib

smspath="/var/mobile/Library/SMS/"

con = lite.connect(smspath+'sms.db')
msg=""


with con:
	con.row_factory = lite.Row
	cur = con.cursor()
	cur.execute('SELECT text from message where read=0 order by date desc')
	rows = cur.fetchall()
	#data = cur.fetchone()
	counter=0
	print "Latest displayed first"
	for row in rows:
		counter+=1
		print "Unread Message: %s" % counter
		print "Text: %s" % row["text"]
		msg=row["text"]
