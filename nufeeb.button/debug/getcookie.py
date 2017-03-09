#*-* coding:UTF-8 *-*
import random
import re

print random.randint(100000000, 1000000000)
print random.sample(range(1,1000000,1),1)

a="1233_abcd"
print a[:4]


mygenerator = (x*x  for  x  in  range( 3 ))
for i in mygenerator :
    print i

for i in mygenerator :
    print i

print "yield..."
def createGenerator() :
    mylist = range( 3 )
    for i in mylist :
        yield i*i

mygenerator = createGenerator()
print (mygenerator)
for i in  mygenerator:
    print i

for i in  mygenerator:
    print i

def gen():
    print "gen()"
    yield 2
x=gen()
print x
'''
for a in x:
    print a
'''

def h():

        print 'Wen Chuan',
        m = yield 5  # Fighting!
        print m
        d = yield 12
        print d
        print 'We are together!'
        f=yield 10

c = h()
m1=c.next()
f1=c.send("m")
n1=c.send("f")
#c.next()
#c.send("f")  #(yield 5)表达式被赋予了'Fighting!'

print f1,m1,n1

def a():
    for n in range(2):
        print "start.............."
        yield 1
        print "first"
        yield 2
        print "secound"
        print "end"
n=a()
for m in n:
    print m
print "ahhahahha"
for m in n:
    print m

k="<span>AAAaaa</span><span class=\"contentForAll\">bbb</span>"
print k
m=re.findall("span(.*?)</span",k)
print m

'''
import redis
r=redis.Redis(host='localhost',port=6379,db=0)
a=r.get("mykey")

r.set("a","1")
r.set("b","2")
r.set("c","3")
print r.dbsize()
r.set("visit:1237:totals",34634)
r.incr("visit:1237:totals")
print r.get("visit:1237:totals")
r.hset("jhon","name","Jhon Green")
r.hset("jhon","email","xx@cc.com")
print r.hgetall("jhon")
print r.hkeys("jhon")
r.sadd("list1","a","v")
r.sadd("list1","b")
r.sadd("list2","w","v")
r.sadd("list2","b")
print r.smembers("list1")
print r.sinter("list1","list2")
print r.sunion("list1","list2")
print r.keys("*st")
print r.set("name","exist")
r.set("name","change")
print r.get("name")
print r.keys()
'''

dic={}
dic2={}
lis=[]
dic['number']='12345'
dic2['key']='222'
lis.append(dic)
lis.append(dic2)
print lis
print lis[0]['number']

k=1
def a():
    if k==1:
        pass
    else:
        print "hahahahha"
a()


