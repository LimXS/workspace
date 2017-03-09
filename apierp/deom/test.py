#*-* coding:UTF-8 *-*
import unittest
class A(unittest.TestCase):

    def __init__(self,data):
        unittest.TestCase.__init__(self,"b")
        self.data=data
        #print self.data
        pass

    def c(self,n):
        try:
            self.assertEqual(n,self.data,msg='no equalc')
            #assert m==self.data
            print "assert  okc"

        except AssertionError,msg:
            print msg

    def b(self):
        print "b"



f=A(10)
f.c(10)