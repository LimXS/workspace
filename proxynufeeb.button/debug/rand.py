import random
a=random.sample(range(1,100,1),99)
print a
print a[0]
k=a[0]
a.remove(k)
print a

import  MySQLdb
sql="SELECT vchcode FROM eshop_saleorder WHERE tradeid LIKE 'AToday%'"
conn= MySQLdb.connect(host='172.16.0.96',user='website',passwd='test@2011',db='beefun',port = 4306)
cur = conn.cursor()
res=cur.execute(sql)
data=cur.fetchmany(res)
for k in data:
    print k[0]
