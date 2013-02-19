#!/usr/bin/python

import sqlite3 as lite
import sys

smspath="/var/mobile/Library/SMS/"

con = lite.connect(smspath + 'sms.db')

with con:
	con.row_factory = lite.Row
	cur = con.cursor()
	
	#cur.execute('DROP TABLE message2;')
	#cur.execute('DROP TRIGGER insert_newest_message_email;')
	cur.execute('CREATE TABLE message2 (ROWID INTEGER PRIMARY KEY, address TEXT, date INTEGER, text TEXT, emailsent INTEGER);')
	cur.execute('CREATE TRIGGER insert_newest_message_email AFTER INSERT ON message WHEN new.ROWID >= 0 BEGIN INSERT INTO "message2" select ROWID,address,date,text,0 from message where ROWID=new.ROWID; END;')
	print 'Done.'