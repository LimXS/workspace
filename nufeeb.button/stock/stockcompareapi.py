#*-* coding:UTF-8 *-*
import unittest
from common import loggingClass
class stockcompary(unittest.TestCase):



    def __init__(self):
        unittest.TestCase.__init__(self,'commonfun')

    def commonfun(self,cases,pagedata,sqldata,msg):
        #随意
        try:
            self.assertEqual(str(pagedata).strip(),str(sqldata).strip(),msg=msg)
        except AssertionError,msg:
            print msg
            print "page:"+str(pagedata).strip()
            print "mysql:"+str(sqldata).strip()
            loggingClass.addlogmes("info",cases,str(msg)+";page:"+str(pagedata)+";mysql:"+str(sqldata))


