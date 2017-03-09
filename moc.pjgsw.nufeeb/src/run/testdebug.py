#*-* coding:UTF-8 *-*

import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)




from onlinestore import loginCase
from onlinestore import accreditCase
from onlinestore import createorderCase
from onlinestore import dealorderCase
from onlinestore import itemsdownCase


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
from salereports import lssalemoneyCase
from salereports import lssaleitemCase
from salereports import lssalediscountCase
from salereports import lsvipchargeCase
from salereports import lsvipscoresCase
from salereports import lscashsalelogCase
from salereports import lsstorecountCase

import unittest
suite = unittest.TestSuite()


suite.addTest(newstockorderCase.newstockTest("testnewStock"))
#suite.addTest(stockordermangeCase.stockordermanageTest("teststockManage"))
#suite.addTest(intorepertoryCase.intorepertoryTest("testintoRepertory"))
#suite.addTest(returnstockCase.returnstockTest("testReturnstock"))
#suite.addTest(exchangestockCase.exchangestockTest("testExchangestock"))

#suite.addTest(createstockmoreCase.createstockmoreTest("testcreatestockMore"))
#suite.addTest(createstockfewCase.createstockfewTest("testcreatestockFew"))
#suite.addTest(createstockotherintoCase.createstockotherintoTest("testcreatestockotherInto"))
#suite.addTest(createstockotheroutCase.createstockotheroutTest("testcreatestockotherOut"))
#suite.addTest(createstocktranferCase.createstocktranferTest("testcreatestockTranfer"))
#suite.addTest(createstockspannerCase.createstockspannerTest("testcreatestockSpanner"))

#suite.addTest(createnewsaleorderCase.createnewsaleorderTest("testcreatenewsaleOrder"))
#suite.addTest(createsalemanageCase.createsalemanageTest("testcreatesaleManage"))
#suite.addTest(createsaleoutCase.createsaleoutTest("testcreatesaleOut"))
#suite.addTest(createsaleoutCase.createsaleoutTest("testcreateornewsaleOut"))
#suite.addTest(createsalereturnCase.createsalereturnTest("testcreatesaleReturn"))
#suite.addTest(createsalereturnCase.createsalereturnTest("testororderReturn"))
#suite.addTest(createsaleexchangeCase.createsaleexchangeTest("testcreatesaleExchange"))
#suite.addTest(createlssaleCase.lssaleTest("testLssale"))
#suite.addTest(createlssaleCase.lssaleTest("testLssalere"))
#suite.addTest(createlsreturnCase.lssalereturnTest("testLssalereturn"))
#suite.addTest(createlsreturnCase.lssalereturnTest("testLssalereturnor"))




#suite.addTest(newstockreportCase.newstockreportTest("testnewstockReport"))

#suite.addTest(newandreturnstockreportCase.nowanrestockreportTest("testnowanrestockReport"))

#suite.addTest(stockfewerCase.stockfewerTest("teststockFewer"))
#suite.addTest(stockmoreCase.stockmoreTest("teststockMore"))

#suite.addTest(stockotherintoCase.stockotherintoTest("teststockotherInto"))
#suite.addTest(stockotheroutCase.stockotheroutTest("teststockotherOut"))

#suite.addTest(stocktransferCase.stocktransferTest("teststockTransfer"))
#suite.addTest(stockspannerCase.stockspannertTest("teststockSpanner"))

#suite.addTest(saleorderreportCase.saleorderTest("testsaleOrder"))
#suite.addTest(itemsalereportCase.itemsaleTest("testitemSale"))
#suite.addTest(itemreturnreportCase.itemreturnTest("testitemReturn"))
#suite.addTest(saleincomecountCase.saleincountTest("testSaleincount"))

#suite.addTest(lssaleitemCase.lssaleitenTest("testLssaleitemTest"))
#suite.addTest(lssalemoneyCase.lssalemoneyTest("testLssalemoney"))
#suite.addTest(lssalediscountCase.lssalediscountTest("testLssalediscount"))
#suite.addTest(lsvipchargeCase.lsvipchargeTest("testLsvipcharge"))
#suite.addTest(lsvipscoresCase.lsvipscoreschargeTest("testLsvipscorescharge"))
#suite.addTest(lscashsalelogCase.lscashsalelogTest("testLscashsalelog"))
#suite.addTest(lsstorecountCase.lsstorecountTest("testLsstorecount"))


'''
#suite.addTest(loginCase.loginTest("testcorrectLogin"))
suite.addTest(accreditCase.accTest("testAccrediton"))
suite.addTest(createorderCase.createTest("testCreateorder"))
suite.addTest(createorderCase.createTest("testSubmitorder"))
suite.addTest(dealorderCase.dealTest("testgetandcompareData"))
suite.addTest(dealorderCase.dealTest("testsendItems"))
suite.addTest(itemsdownCase.itemsdownCase("testitemsDown"))
'''
runner = unittest.TextTestRunner()
runner.run(suite)





