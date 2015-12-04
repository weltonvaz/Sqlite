#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
os.system("clear")

import csv, sqlite3

con = sqlite3.connect("mega.db")
cur = con.cursor()

with open("mega.txt", "rb") as f:
	reader = csv.reader(f, delimiter=',')
	for row in reader:
		to_db = [unicode(row[0], "utf8"), unicode(row[1], "utf8"), unicode(row[2], "utf8"),unicode(row[3], "utf8"),unicode(row[4], "utf8"),unicode(row[5], "utf8")] # Appends data from CSV file representing and handling of text
		cur.execute("INSERT INTO dezenas (dezena1, dezena2, dezena3, dezena4, dezena5, dezena6) VALUES(?, ?, ?, ?, ?, ?);", to_db)
		con.commit()
con.close()
