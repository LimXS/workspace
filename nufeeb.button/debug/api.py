#*-* coding:UTF-8 *-*
import unittest
class A():
    def __init__(self,methodName='runTest',):
        self._testMethodName = methodName

        testMethod = getattr(self, methodName)
        #testMethod("ken")
        print testMethod()
        self.x=testMethod.__doc__
        print self.x

    def hello(self,a,b):
        print a,b

class B(A):
    '23333'
    name = 'aj'
    def __init__(self,lis,know,funpro):
        self._testFunc = funpro
        A.__init__(self,"bf")

        print "b init"

        #print know
        self.lis=lis
        self.know=know
        #self.a="1234"

    def bf(self):
        '''doc'''
        print "232"
        #print name
        self._testFunc()
        return 1000

    def tx(self,m):
        return getattr(self,m)()

    def c(self):
        print "factory"

    def d(self):
        print "factory2"
        return 999
def fun():
    '''3'''
    print "fun"

f=B(2,3,fun)
f.tx('d')



'''
class ordercompary(unittest.TestCase):

    def __init__(self,lis,n):
        #unittest.TestCase.__init__(self,'commonfun')
        self.lis=lis
        self.n=n

    def orhell(self):
        self.assertEqual(self.lis,self.n,"no equal")

m=ordercompary(1,2)
m.orhell()
'''

