#*-* coding:UTF-8 *-*

import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


import unittest
import HTMLTestRunner
import time

from onlinestore import loginCase
from onlinestore import accreditCase
from onlinestore import createorderCase
from onlinestore import dealorderCase


from inventory import newstockorderCase
from inventory import stockordermangeCase
from inventory import intorepertoryCase
from inventory import returnstockCase
from inventory import exchangestockCase

from invenstock import createstockfewCase
from invenstock import createstockmoreCase
from invenstock import createstockotherintoCase
from invenstock import createstockotheroutCase
from invenstock import createstockspannerCase
from invenstock import createstocktranferCase

from salecreate import createnewsaleorderCase
from salecreate import createsalemanageCase
from salecreate import createsaleoutCase
from salecreate import createsalereturnCase
from salecreate import createsaleexchangeCase
from salecreate import createlssaleCase
from salecreate import createlsreturnCase


from reports import newstockreportCase
from reports import newandreturnstockreportCase


from reports import stockfewerCase
from reports import stockmoreCase

from reports import stockotherintoCase
from reports import stockotheroutCase

from reports import stocktransferCase
from reports import stockspannerCase

from salereports import saleorderreportCase
from salereports import itemsalereportCase
from salereports import itemreturnreportCase
from salereports import saleincomecountCase

from salereports import lssaleitemCase
from salereports import lssalemoneyCase
from salereports import lssalediscountCase
from salereports import lsvipchargeCase
from salereports import lsvipscoresCase
from salereports import lscashsalelogCase
from salereports import lsstorecountCase

from common import baseClass

bas=baseClass.base()
testunit=unittest.TestSuite()

'''
testunit.addTest(unittest.makeSuite(accreditCase.accTest))
testunit.addTest(unittest.makeSuite(loginCase.loginTest))
testunit.addTest(unittest.makeSuite(createorderCase.createTest))
testunit.addTest(unittest.makeSuite(dealorderCase.dealTest))
'''

testunit.addTest(unittest.makeSuite(newstockorderCase.newstockTest))
testunit.addTest(unittest.makeSuite(stockordermangeCase.stockordermanageTest))
testunit.addTest(unittest.makeSuite(intorepertoryCase.intorepertoryTest))
testunit.addTest(unittest.makeSuite(returnstockCase.returnstockTest))
testunit.addTest(unittest.makeSuite(exchangestockCase.exchangestockTest))


testunit.addTest(unittest.makeSuite(createstockmoreCase.createstockmoreTest))
testunit.addTest(unittest.makeSuite(createstockfewCase.createstockfewTest))
testunit.addTest(unittest.makeSuite(createstockotherintoCase.createstockotherintoTest))
testunit.addTest(unittest.makeSuite(createstockotheroutCase.createstockotheroutTest))
testunit.addTest(unittest.makeSuite(createstocktranferCase.createstocktranferTest))
testunit.addTest(unittest.makeSuite(createstockspannerCase.createstockspannerTest))


testunit.addTest(unittest.makeSuite(createnewsaleorderCase.createnewsaleorderTest))
testunit.addTest(unittest.makeSuite(createsalemanageCase.createsalemanageTest))
testunit.addTest(unittest.makeSuite(createsaleoutCase.createsaleoutTest))
testunit.addTest(unittest.makeSuite(createsalereturnCase.createsalereturnTest))
testunit.addTest(unittest.makeSuite(createsaleexchangeCase.createsaleexchangeTest))
testunit.addTest(unittest.makeSuite(createlssaleCase.lssaleTest))
testunit.addTest(unittest.makeSuite(createlsreturnCase.lssalereturnTest))


testunit.addTest(unittest.makeSuite(newstockreportCase.newstockreportTest))
testunit.addTest(unittest.makeSuite(newandreturnstockreportCase.nowanrestockreportTest))

testunit.addTest(unittest.makeSuite(stockfewerCase.stockfewerTest))
testunit.addTest(unittest.makeSuite(stockmoreCase.stockmoreTest))

testunit.addTest(unittest.makeSuite(stockotheroutCase.stockotheroutTest))
testunit.addTest(unittest.makeSuite(stockotherintoCase.stockotherintoTest))

testunit.addTest(unittest.makeSuite(stocktransferCase.stocktransferTest))
testunit.addTest(unittest.makeSuite(stockspannerCase.stockspannertTest))

testunit.addTest(unittest.makeSuite(saleorderreportCase.saleorderTest))
testunit.addTest(unittest.makeSuite(itemsalereportCase.itemsaleTest))
testunit.addTest(unittest.makeSuite(itemreturnreportCase.itemreturnTest))
testunit.addTest(unittest.makeSuite(saleincomecountCase.saleincountTest))
testunit.addTest(unittest.makeSuite(lssaleitemCase.lssaleitenTest))
testunit.addTest(unittest.makeSuite(lssalemoneyCase.lssalemoneyTest))
testunit.addTest(unittest.makeSuite(lssalediscountCase.lssalediscountTest))
testunit.addTest(unittest.makeSuite(lsvipchargeCase.lsvipchargeTest))
testunit.addTest(unittest.makeSuite(lsvipscoresCase.lsvipscoreschargeTest))
testunit.addTest(unittest.makeSuite(lscashsalelogCase.lscashsalelogTest))
testunit.addTest(unittest.makeSuite(lsstorecountCase.lsstorecountTest))






#testunit.addTest(unittest.makeSuite(end.endTest))

timeStamp=time.time()
timeArray = time.localtime(timeStamp)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S" , timeArray)

filename='D:\\beefunresault.html'
fp=file(filename,'wb')
runner=HTMLTestRunner.HTMLTestRunner(
       stream=fp,
       title=u'测试报告',
       description=u'用例执行情况'                              
                                     )
runner.run(testunit)



