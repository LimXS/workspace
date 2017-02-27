
#*-* coding:UTF-8 *-*
import  MySQLdb
from common import browserClass
from common import loggingClass
browser=browserClass.browser()
a=[]
conn= MySQLdb.connect(host='172.16.0.96',user='website',passwd='test@2011',db='beefun',port = 4306)
cur = conn.cursor()
sqlreault=cur.execute("SELECT btypeid,etypeid,ktypeid FROM dlyndxOrder  WHERE number='JHD-20161221-038'")
data = cur.fetchone()
#print data

sql1="SELECT FullName FROM btype WHERE id=(SELECT btypeid FROM dlyndxOrder  WHERE number='JHD-20161221-038')"
sql2="SELECT FullName FROM employee WHERE id=(SELECT etypeid FROM dlyndxOrder  WHERE number='JHD-20161221-038')"
sql3="SELECT FullName FROM stock WHERE id=(SELECT ktypeid FROM dlyndxOrder  WHERE number='JHD-20161221-038')"
#data=browser.mysqlsqls(sql1,sql2,sql3)
#print data

#print data[0]
datas=browser.getmysqldlyndxOrder("JHD-20161221-038","12-21into")
print "datas.........................."
print datas
for n in datas:
    print n


item=browser.getmysqlitems("JHD-20161221-038","12-21into")
print item
print len(item)
for k in item:
    print len(k)
    print k

for m in item:
    print "itemdetail......."
    for n in m:
        print n


li=[1,23,4,5]
print li
del li[1]
print li
from stock import stockcompareapi
com=stockcompareapi.stockcompary()
com.commonfun("1","2","no equal")

a=100
b="200.34"

print a,b
print float(a),float(b)

a = ("%.4f" % float(b))
print a

print browser.strconfloat("999.34")

divjq=[0,1,5,20]
for i in divjq:
    print i

