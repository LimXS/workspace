#*-* coding:UTF-8 *-*
import re
import sys
import os
import random
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


import unittest
import HTMLTestRunner
import time


from frequentlyused import notedraftCase
from frequentlyused import notecentralCase
from frequentlyused import stockstateCase

from itemmodule import iteminfoCase
from itemmodule import skumanageCase
from itemmodule import itempackagemanCase
from itemmodule import itemcombineCase

from stock import newstockordersCase
from stock import stockmanageCase
from stock import stockintocateCase
from stock import stockreturnCase
from stock import stockexchangeCase
from stock import paynotecCase
from stock import stocknoteCase

from saleretail import newsaleorderCase
from saleretail import saleordermanCase
from saleretail import saleoutCase
from saleretail import salereturnCase
from saleretail import saleexchangeCase
from saleretail import salepayCase
from saleretail import entrustsaleCase
from saleretail import entrustreturnCase
from saleretail import entrustaccCase
from saleretail import entruststockselCase
from saleretail import lsopenCase
from saleretail import lsreturnCase
from saleretail import salenoteselCase
from saleretail import itempricemanCase
from saleretail import saledistraceCase

from instock import getlessnoteCase
from instock import getmorenoteCase
from instock import transnoteCase
from instock import changepriceCase
from instock import proasseCase
from instock import otherintoCase
from instock import otheroutCase
from instock import stockgridCase
from instock import gatherstockCase
from instock import stockinventoryCase
from instock import alarmstartCase
from instock import alarmsetCase
from instock import alarmupCase
from instock import alarmdownCase
from instock import seriesnotraceCase
from instock import seriesnostataselCase
from instock import test_innerdrawCase


from finance import test_paynoteCase
from finance import test_receiptnoteCase
from finance import test_accdocCase
from finance import test_companyrepaCase
from finance import test_costnoteCase
from finance import test_menexitranCase
from finance import test_otherreceiptCase
from finance import test_checkaccpayaddCase
from finance import test_checkaccpayreduceCase
from finance import test_checkaccreaddCase
from finance import test_checkaccrereduceCase
from finance import test_checkfundaddCase
from finance import test_checkfundreduceCase
from finance import test_fixcapbuyCase
from finance import test_fixcapdeprCase
from finance import test_fixcapsaleCase
from finance import test_fixcapsetCase
from finance import test_endmanageCase

from reports import test_instockorderCase
from reports import test_instockdetailreport
from reports import test_itemstockreoprt
from reports import test_repsaleordercountCase
from reports import test_resaleitemCase
from reports import test_resaleitemsareCase
from reports import test_resalebenefitCase
from reports import test_resaleyearreportCase

from reports import test_resalemonthCase
from reports import test_resaledetailCase
from reports import test_resaleprofitCase
from reports import test_resalelsmoneyCase
from reports import test_resalelsitemCase
from reports import test_resalemenberscoresCase
from reports import test_resalemenberchargeCase
from reports import test_resalestorelsCase
from reports import test_resalepossaleCase
from reports import test_resalepackageCase
from reports import test_instkdayCase
from reports import test_insklessCase
from reports import test_instkmoreCase
from reports import test_instktranCase
from reports import test_instkdismountCase
from reports import test_instkothintoCase
from reports import test_inskothoutCase
from reports import test_inskinnerCase

from reports import test_finbusinessCase
from reports import test_finbusinessdailyCase
from reports import test_finbenfitCase
from reports import test_finbalanceCase
from reports import test_finbossCase

from reports import test_cominstockCase
from reports import test_cominkreturnCase
from reports import test_comsalereturnCase
from reports import test_combackmoneyCase
from reports import test_comcostgridCase
from reports import test_combusinessCase

from reports import test_depcostgridCase
from reports import test_depbusinessCase
from reports import test_deppeogetCase
from reports import test_deppeocostgridCase
from reports import test_deppeobusinessCase
from reports import test_depmkpeogetCase

from common import baseClass
bas=baseClass.base()
testunit=unittest.TestSuite()
'''
f=open(r'C:\workspace\proxynufeeb.button\run\cases','r')
k=f.read()
a=re.findall("Suite\((.*?)\)",k)
print a
for i in a:
    print i+","
'''
cases=[notedraftCase.notedraftTest,
stockstateCase.stockstateTest,
iteminfoCase.iteminfoTest,
skumanageCase.skumanageTest,
itempackagemanCase.itempackagemanTest,
itemcombineCase.itemcombineTest,
newstockordersCase.newstockordersTest,
stockmanageCase.stockmanageTest,
stockintocateCase.stockintocateTest,
stockreturnCase.stockreturnTest,
stockexchangeCase.stockexchangeTest,
paynotecCase.stockpayTest,
stocknoteCase.stocknoteTest,
newsaleorderCase.newsaleorderTest,
saleordermanCase.saleordermanTest,
saleoutCase.saleoutTest,
notecentralCase.notecentralTest,
salereturnCase.salereturnTest,
saleexchangeCase.saleexchangeTest,
salepayCase.salepayTest,
entrustsaleCase.entrustsaleTest,
entrustreturnCase.entrustreturnTest,
entrustaccCase.entrustaccTest,
entruststockselCase.entruststockselTest,
lsopenCase.lsopenTest,
lsreturnCase.lsreturnTest,
salenoteselCase.salenoteselTest,
itempricemanCase.itempricemanTest,
saledistraceCase.saledistraceTest,
seriesnotraceCase.seriesnotraceTest,
seriesnostataselCase.seriesnostateselTest,
getlessnoteCase.getlessnoteTest,
getmorenoteCase.getmorenoteTest,
transnoteCase.transnoteTest,
changepriceCase.changepriceTest,
proasseCase.proasseTest,
otherintoCase.otherintoTest,
otheroutCase.otheroutTest,
stockgridCase.stockgridTest,
gatherstockCase.gatherstockTest,
stockinventoryCase.stockinvTest,
alarmsetCase.alarmsetTest,
alarmstartCase.alarmstartTest,
alarmupCase.alarmupTest,
alarmdownCase.alarmdownTest,
test_innerdrawCase.innerdrawTest,
test_paynoteCase.paynoteTest,
test_receiptnoteCase.receiptnoteTest,
test_costnoteCase.costnoteTest,
test_otherreceiptCase.otherreceiptTest,
test_menexitranCase.menexitranTest,
test_accdocCase.accdocTest,
test_companyrepaCase.companyrepaTest,
test_checkfundaddCase.checkfundaddTest,
test_checkfundreduceCase.checkfundreduceTest,
test_checkaccreaddCase.checkaccreaddTest,
test_checkaccrereduceCase.checkaccrereduceTest,
test_checkaccpayaddCase.checkaccpayaddTest,
test_checkaccpayreduceCase.checkaccpayreduceTest,
test_fixcapsetCase.fixcapsetTest,
test_fixcapsaleCase.fixcapsaleTest,
test_fixcapbuyCase.fixcapbuyTest,
test_fixcapdeprCase.fixcapdeprTest,
test_endmanageCase.endmanageTest,
test_instockorderCase.instockorderreportTest,
test_instockdetailreport.instockdetailreoportTest,
test_itemstockreoprt.itemstockreoportTest,
test_repsaleordercountCase.resaleorderTest,
test_resaleitemCase.resaleitemTest,
test_resaleitemsareCase.resaleitemsareTest,
test_resalebenefitCase.resalebenefitTest,
test_resaleyearreportCase.resaleyearTest,
test_resalemonthCase.resalemonthTest,
test_resaledetailCase.resaledetailTest,
test_resaleprofitCase.resaleprofitTest,
test_resalelsmoneyCase.resalelsmoneyTest,
test_resalelsitemCase.resalelsitemTest,
test_resalemenberscoresCase.resalemenberscoreTest,
test_resalemenberchargeCase.resalemenberchargeTest,
test_resalestorelsCase.resalestorelsTest,
test_resalepossaleCase.resalepossaleTest,
test_resalepackageCase.resalepackageTest,
test_instkdayCase.inskdayTest,
test_insklessCase.insklessTest,
test_instkmoreCase.inskmoreTest,
test_instktranCase.insktranTest,
test_instkdismountCase.inskdismountTest,
test_instkothintoCase.inskothintoTest,
test_inskothoutCase.inskothoutTest,
test_inskinnerCase.inskinnerTest,
test_finbusinessCase.finbusinessTest,
test_finbusinessdailyCase.finbusinessdailyTest,
test_finbenfitCase.finbenfitTest,
test_finbalanceCase.finbalanceTest,
test_finbossCase.finbossTest,
test_cominstockCase.cominstockTest,
test_cominkreturnCase.cominkreturnTest,
test_comsalereturnCase.comsalereturnTest,
test_combackmoneyCase.combackmoneyTest,
test_comcostgridCase.comcostgridTest,
test_combusinessCase.combusinessTest,
test_depcostgridCase.depcostgridTest,
test_depbusinessCase.depbusinessTest,
test_deppeogetCase.deppeogetTest,
test_deppeocostgridCase.deppeocostgridTest,
test_deppeobusinessCase.deppeobusinessTest,
test_depmkpeogetCase.depmkpeogetTest,]
while len(cases)>0:
    b=random.choice(cases)
    cases.remove(b)
    testunit.addTest(unittest.makeSuite(b))
else:
    timeStamp=time.time()
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S" , timeArray)

    filename='D:\\proxybeefunresault.html'
    fp=file(filename,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(
           stream=fp,
           title=u'测试报告',
           description=u'用例执行情况'
                                     )
    runner.run(testunit)


'''
testunit.addTest(unittest.makeSuite(notedraftCase.notedraftTest))

testunit.addTest(unittest.makeSuite(stockstateCase.stockstateTest))

testunit.addTest(unittest.makeSuite(iteminfoCase.iteminfoTest))
testunit.addTest(unittest.makeSuite(skumanageCase.skumanageTest))
testunit.addTest(unittest.makeSuite(itempackagemanCase.itempackagemanTest))
testunit.addTest(unittest.makeSuite(itemcombineCase.itemcombineTest))

testunit.addTest(unittest.makeSuite(newstockordersCase.newstockordersTest))
testunit.addTest(unittest.makeSuite(stockmanageCase.stockmanageTest))
testunit.addTest(unittest.makeSuite(stockintocateCase.stockintocateTest))
testunit.addTest(unittest.makeSuite(stockreturnCase.stockreturnTest))
testunit.addTest(unittest.makeSuite(stockexchangeCase.stockexchangeTest))
testunit.addTest(unittest.makeSuite(paynotecCase.stockpayTest))
testunit.addTest(unittest.makeSuite(stocknoteCase.stocknoteTest))


testunit.addTest(unittest.makeSuite(newsaleorderCase.newsaleorderTest))
testunit.addTest(unittest.makeSuite(saleordermanCase.saleordermanTest))
testunit.addTest(unittest.makeSuite(saleoutCase.saleoutTest))
testunit.addTest(unittest.makeSuite(notecentralCase.notecentralTest))
testunit.addTest(unittest.makeSuite(salereturnCase.salereturnTest))
testunit.addTest(unittest.makeSuite(saleexchangeCase.saleexchangeTest))
testunit.addTest(unittest.makeSuite(salepayCase.salepayTest))
testunit.addTest(unittest.makeSuite(entrustsaleCase.entrustsaleTest))
testunit.addTest(unittest.makeSuite(entrustreturnCase.entrustreturnTest))
testunit.addTest(unittest.makeSuite(entrustaccCase.entrustaccTest))
testunit.addTest(unittest.makeSuite(entruststockselCase.entruststockselTest))
testunit.addTest(unittest.makeSuite(lsopenCase.lsopenTest))
testunit.addTest(unittest.makeSuite(lsreturnCase.lsreturnTest))
testunit.addTest(unittest.makeSuite(salenoteselCase.salenoteselTest))
testunit.addTest(unittest.makeSuite(itempricemanCase.itempricemanTest))
testunit.addTest(unittest.makeSuite(saledistraceCase.saledistraceTest))
testunit.addTest(unittest.makeSuite(seriesnotraceCase.seriesnotraceTest))
testunit.addTest(unittest.makeSuite(seriesnostataselCase.seriesnostateselTest))

testunit.addTest(unittest.makeSuite(getlessnoteCase.getlessnoteTest))
testunit.addTest(unittest.makeSuite(getmorenoteCase.getmorenoteTest))
testunit.addTest(unittest.makeSuite(transnoteCase.transnoteTest))
testunit.addTest(unittest.makeSuite(changepriceCase.changepriceTest))
testunit.addTest(unittest.makeSuite(proasseCase.proasseTest))
testunit.addTest(unittest.makeSuite(otherintoCase.otherintoTest))
testunit.addTest(unittest.makeSuite(otheroutCase.otheroutTest))
testunit.addTest(unittest.makeSuite(stockgridCase.stockgridTest))
testunit.addTest(unittest.makeSuite(gatherstockCase.gatherstockTest))
testunit.addTest(unittest.makeSuite(stockinventoryCase.stockinvTest))
testunit.addTest(unittest.makeSuite(alarmsetCase.alarmsetTest))
testunit.addTest(unittest.makeSuite(alarmstartCase.alarmstartTest))
testunit.addTest(unittest.makeSuite(alarmupCase.alarmupTest))
testunit.addTest(unittest.makeSuite(alarmdownCase.alarmdownTest))
testunit.addTest(unittest.makeSuite(test_innerdrawCase.innerdrawTest))

testunit.addTest(unittest.makeSuite(test_paynoteCase.paynoteTest))
testunit.addTest(unittest.makeSuite(test_receiptnoteCase.receiptnoteTest))
testunit.addTest(unittest.makeSuite(test_costnoteCase.costnoteTest))
testunit.addTest(unittest.makeSuite(test_otherreceiptCase.otherreceiptTest))
testunit.addTest(unittest.makeSuite(test_menexitranCase.menexitranTest))
testunit.addTest(unittest.makeSuite(test_accdocCase.accdocTest))
testunit.addTest(unittest.makeSuite(test_companyrepaCase.companyrepaTest))
testunit.addTest(unittest.makeSuite(test_checkfundaddCase.checkfundaddTest))
testunit.addTest(unittest.makeSuite(test_checkfundreduceCase.checkfundreduceTest))
testunit.addTest(unittest.makeSuite(test_checkaccreaddCase.checkaccreaddTest))
testunit.addTest(unittest.makeSuite(test_checkaccrereduceCase.checkaccrereduceTest))
testunit.addTest(unittest.makeSuite(test_checkaccpayaddCase.checkaccpayaddTest))
testunit.addTest(unittest.makeSuite(test_checkaccpayreduceCase.checkaccpayreduceTest))
testunit.addTest(unittest.makeSuite(test_fixcapsetCase.fixcapsetTest))
testunit.addTest(unittest.makeSuite(test_fixcapsaleCase.fixcapsaleTest))
testunit.addTest(unittest.makeSuite(test_fixcapbuyCase.fixcapbuyTest))
testunit.addTest(unittest.makeSuite(test_fixcapdeprCase.fixcapdeprTest))
testunit.addTest(unittest.makeSuite(test_endmanageCase.endmanageTest))

testunit.addTest(unittest.makeSuite(test_instockorderCase.instockorderreportTest))
testunit.addTest(unittest.makeSuite(test_instockdetailreport.instockdetailreoportTest))
testunit.addTest(unittest.makeSuite(test_itemstockreoprt.itemstockreoportTest))

testunit.addTest(unittest.makeSuite(test_repsaleordercountCase.resaleorderTest))
testunit.addTest(unittest.makeSuite(test_resaleitemCase.resaleitemTest))
testunit.addTest(unittest.makeSuite(test_resaleitemsareCase.resaleitemsareTest))
testunit.addTest(unittest.makeSuite(test_resalebenefitCase.resalebenefitTest))
testunit.addTest(unittest.makeSuite(test_resaleyearreportCase.resaleyearTest))
testunit.addTest(unittest.makeSuite(test_resalemonthCase.resalemonthTest))
testunit.addTest(unittest.makeSuite(test_resaledetailCase.resaledetailTest))
testunit.addTest(unittest.makeSuite(test_resaleprofitCase.resaleprofitTest))
testunit.addTest(unittest.makeSuite(test_resalelsmoneyCase.resalelsmoneyTest))
testunit.addTest(unittest.makeSuite(test_resalelsitemCase.resalelsitemTest))
testunit.addTest(unittest.makeSuite(test_resalemenberscoresCase.resalemenberscoreTest))
testunit.addTest(unittest.makeSuite(test_resalemenberchargeCase.resalemenberchargeTest))
testunit.addTest(unittest.makeSuite(test_resalestorelsCase.resalestorelsTest))
testunit.addTest(unittest.makeSuite(test_resalepossaleCase.resalepossaleTest))
testunit.addTest(unittest.makeSuite(test_resalepackageCase.resalepackageTest))
testunit.addTest(unittest.makeSuite(test_instkdayCase.inskdayTest))
testunit.addTest(unittest.makeSuite(test_insklessCase.insklessTest))
testunit.addTest(unittest.makeSuite(test_instkmoreCase.inskmoreTest))
testunit.addTest(unittest.makeSuite(test_instktranCase.insktranTest))
testunit.addTest(unittest.makeSuite(test_instkdismountCase.inskdismountTest))
testunit.addTest(unittest.makeSuite(test_instkothintoCase.inskothintoTest))
testunit.addTest(unittest.makeSuite(test_inskothoutCase.inskothoutTest))
testunit.addTest(unittest.makeSuite(test_inskinnerCase.inskinnerTest))
testunit.addTest(unittest.makeSuite(test_finbusinessCase.finbusinessTest))
testunit.addTest(unittest.makeSuite(test_finbusinessdailyCase.finbusinessdailyTest))
testunit.addTest(unittest.makeSuite(test_finbenfitCase.finbenfitTest))
testunit.addTest(unittest.makeSuite(test_finbalanceCase.finbalanceTest))
testunit.addTest(unittest.makeSuite(test_finbossCase.finbossTest))
testunit.addTest(unittest.makeSuite(test_cominstockCase.cominstockTest))
testunit.addTest(unittest.makeSuite(test_cominkreturnCase.cominkreturnTest))
testunit.addTest(unittest.makeSuite(test_comsalereturnCase.comsalereturnTest))
testunit.addTest(unittest.makeSuite(test_combackmoneyCase.combackmoneyTest))
testunit.addTest(unittest.makeSuite(test_comcostgridCase.comcostgridTest))
testunit.addTest(unittest.makeSuite(test_combusinessCase.combusinessTest))
testunit.addTest(unittest.makeSuite(test_depcostgridCase.depcostgridTest))
testunit.addTest(unittest.makeSuite(test_depbusinessCase.depbusinessTest))
testunit.addTest(unittest.makeSuite(test_deppeogetCase.deppeogetTest))
testunit.addTest(unittest.makeSuite(test_deppeocostgridCase.deppeocostgridTest))
testunit.addTest(unittest.makeSuite(test_deppeobusinessCase.deppeobusinessTest))
testunit.addTest(unittest.makeSuite(test_depmkpeogetCase.depmkpeogetTest))


timeStamp=time.time()
timeArray = time.localtime(timeStamp)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S" , timeArray)

filename='D:\\proxybeefunresault.html'
fp=file(filename,'wb')
runner=HTMLTestRunner.HTMLTestRunner(
       stream=fp,
       title=u'测试报告',
       description=u'用例执行情况'                              
                                     )
runner.run(testunit)



'''

