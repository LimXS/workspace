#*-* coding:UTF-8 *-*

import random
from common import browserClass
browser=browserClass.browser()

print random.choice(["JGood", "is", "a", "handsome", "boy"])

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
