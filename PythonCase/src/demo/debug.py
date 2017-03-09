#*-* coding:UTF-8 *-*
'''
Created on 2016��4��5��

@author: xsx
'''
import unittest

from python27 import order
from python27 import ordercreateandcheck
from python27 import ordersearch
suite = unittest.TestSuite()






suite.addTest(order.orderTest("testAccredit"))


suite.addTest(ordercreateandcheck.ordercreateandcheckTest("testCreateorder"))

suite.addTest(ordersearch.orderSearchtest("testCreatesearchorder"))
suite.addTest(ordersearch.orderSearchtest("testSearchcompare"))
#suite.addTest(ordercreateandcheck.ordercreateandcheckTest("testWritedate"))
suite.addTest(ordercreateandcheck.ordercreateandcheckTest("testOrdercheck"))

runner = unittest.TextTestRunner()
runner.run(suite)
