import sqlite3

conn = sqlite3.connect("db.sqlite3")
cur = conn.cursor()
f = open("bp","r")
for line in f.read().split("\n"):
	my = []
	for col in line.split(";"):
		my += [col,]
	cur.execute("INSERT INTO serials_post(name,title,serie,episode,url1,url1_cc,url2,url2_cc,url1_cz,url2_cz,created_date) VALUES (?,?,?,?,?,?,?,?,?,?,?)",(my[0],my[0],my[1],my[2],my[3],0,'',0,'',my[4],6))

conn.commit()
conn.close()
