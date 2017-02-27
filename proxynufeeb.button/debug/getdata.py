#*-* coding:UTF-8 *-*

import random
from common import browserClass
browser=browserClass.browser()

print random.choice(["JGood", "is", "a", "handsome", "boy"])

x=["JGood", "is", "a", "handsome", "boy"]
random.shuffle(x)
print x

print random.randint(10,20)

print random.uniform(2,10)

print range(10,100,5)

a=str(random.sample(range(1,100,1),3))
print a

def h():
    print 'Wen Chuan',
    m = yield 5  # Fighting!
    print m
    d = yield 12
    print d
    print 'We are together!'
    f=yield 10


c=h()
print c.next()
k=c.send("haha")
print k
print c.next()

'''
def m(start):
    count=start
    while True:
        val=yield count
        if val is not None:
            count=val
        else:
            count+=5

n=m(100)
print n.next()
print n.send(20)
print n.next()
'''
import random
etypeid={'1151581351029634':'（京东）君问手机旗舰店','28455803329945743':'yhhycg','3293278338924174660':'天机数码店','3293278520339531720':'2',
         '7608004971719290048':'亚马逊问问店','8080322324297667222':'拍拍问问店','8489586093684841544':'3','8623847055876651182':'1',
         '8623847055891053928':'4','9584807475043094946':'供销平台','12184225228657647994':'5','12184225317590870082':'9',
         '12184225317595413496':'8','17440768759282257092':'6','17440768759282258064':'君问数码官方旗舰店','17440768759282258217':'7'
         }

k=random.choice(etypeid.keys())
print k
print etypeid[k]

import  re

fc=open(r"E:\new.txt")
item=fc.read()
#print item
#print str(item).encode('utf-8')

itemlist=re.findall("values(.*?);",item)
itemnow=random.choice(itemlist)
#print itemnow
itemdata=re.findall("'(.*?)'",itemnow)
#print itemdata[1]

import time
import datetime
todaytime=datetime.datetime.now()
overtime=todaytime+datetime.timedelta(days=-1)
todaytime=todaytime.strftime('%Y-%m-%d %H:%M:%S')
print todaytime
overtime=overtime.strftime('%Y-%m-%d %H:%M:%S')
print overtime

a=[1,2,3,4,5,6,7,8,9,10,11,12,13]
print a[:-1]





fc=open(r"E:\vcsenditem2.txt")
item=fc.read()
#print item
all=re.findall("values\('(.*?)'",item)
#print all
#print all[0]
#print len(all)



def changes(a,b):
    #list 分段函数,a:数据[(1),(2)]b:长度
    k=[]
    for i in xrange(0,len(a),b):
        k.append(a[i:i+b])
    return k
datas=[]
m=changes(all,10)
#print len(m)
for gro in m:
    print gro
    #print k[0],k[1],k[2],k[3],k[4],k[5]
    billdata={"vchcodes":[gro[0],gro[1],gro[2],gro[3],gro[4],gro[5]]}
    #print billdata
    datas.append(billdata)
#print datas



x=["JGood", "is", "a", "handsome", "boy"]
random.shuffle(x)
print x

print datas
random.shuffle(datas)
print datas