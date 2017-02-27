#*-* coding:UTF-8 *-*
import MySQLdb
conn= MySQLdb.connect(host='172.16.0.96',user='website',passwd='test@2011',db='beefun',port = 4306)
cur = conn.cursor()
sql="SELECT token FROM eshop WHERE etypeid='2605638079543105363'"
aa=cur.execute(sql)
print aa


k=cur.fetchone()
print k[0]
cur.scroll(2,'absolute')
info = cur.fetchmany(aa)
print info
#print cur.scroll(0,'absolute')

for ii in info:
    print ii

cur.close()
conn.commit()
conn.close()
