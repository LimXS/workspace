#-*- coding: UTF-8 -*-
import time
from common import baseClass
base=baseClass.base()

# 定义一个计时器，传入一个，并返回另一个附加了计时功能的方法
def timeit(func):
     
    # 定义一个内嵌的包装函数，给传入的函数加上计时功能的包装
    def wrapper(a,b):
        start = time.clock()
        refun=func(a,b)
        end =time.clock()
        print 'used:', end - start
        return refun+1
    # 将包装后的函数返回
    return wrapper
#@timeit
def foo(a,b):
    print 'in foo()'
    print a+b
    return a+b

#coo = timeit(foo(2,3))
coo = timeit(foo)
m=coo(2,3)
print m

foo(4,5)


def timechange(func):
    # 定义一个内嵌的包装函数，给传入的函数加上计时功能的包装
    def wrapper(a,b):
        start = time.clock()
        refun=func(a,b)
        end =time.clock()

        return refun+1
    # 将包装后的函数返回
    return wrapper




def fun(a,*c):
    print a
    print c
    print len(c)
    print c[0]
fun(100,10)

def fun2(a,**c):
    print a
    print c
fun2(200,b="1",d="2")

a="22221111"
print a[:4]


m="new Date(1472572800000)"
print m[9:-1]

