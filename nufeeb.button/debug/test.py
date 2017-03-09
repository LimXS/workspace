#*-* coding:UTF-8 *-*
#闭包
def close(x):
     def inner():
         print x # 1
     return inner
print1 = close("close1")
print1()

#decorator
def outer(x):
     def inner(a):
         print "decorator"
         x(a)
     return inner

def hello(a):
    print "hello",a
#等价于@outer hello(2)
print1=outer(hello)
print1(2)

#decorator improver
def improveouter(arg):
    print "arg:",arg
    def innerdec(dec):
        print "decorator"
        def fun1(a,b):
            dec(a,b)
            print "deeppest:",str(a+b)
        return fun1
    return innerdec

#@improveouter('222')
def hello2(a,b):
    print "hello:",a+b

#hello2(1,2)
x1=improveouter(100)
x2=x1(hello2)
x3=x2(1,888)


