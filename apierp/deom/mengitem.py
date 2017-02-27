def fun1(defun):
    def wap(a,b):
        print "wap start"
        defun(a,b)
        print "wap end"
    return wap
@fun1
def fun3(a,b):
    print a+b

fun3(2,4)

def log(text,text2):
    def decorator(func):
        print '%s %s():' % (text, func.__name__)
        def wrapper(a,b):
            print '%s %s():' % (text2, func.__name__)
            func(a,b)
        return wrapper
    return decorator

@log('ex1','ex2')
def fun2(a,b):
    print "hello",a+b

fun2(3,6)






def deco(arg):
    def _deco(func):
        def __deco(a,b):
            print("before %s called [%s]." % (func.__name__, arg))
            func(a,b)
            print("  after %s called [%s]." % (func.__name__, arg))
        return __deco
    return _deco

@deco("mymodule")
def myfunc():
    print(" myfunc() called.")

@deco("module2")
def myfunc2(a,b):
    print(" myfunc2() called.",a+b)











