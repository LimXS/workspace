#*-* coding:UTF-8 *-*

import sys
import os
import unittest
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

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


suite = unittest.TestSuite()


##suite.addTest(notedraftCase.notedraftTest("testnoteDraft"))
#suite.addTest(notecentralCase.notecentralTest("testnoteCentral"))
##suite.addTest(stockstateCase.stockstateTest("teststockState"))

##suite.addTest(iteminfoCase.iteminfoTest("testitemInfo"))
##suite.addTest(skumanageCase.skumanageTest("testskuManage"))
##suite.addTest(itempackagemanCase.itempackagemanTest("testitempackageMan"))
##suite.addTest(itemcombineCase.itemcombineTest("testitemCombine"))

##suite.addTest(newstockordersCase.newstockordersTest("testnewstockorders"))
##suite.addTest(newstockordersCase.newstockordersTest("test_assnskSave"))
##suite.addTest(stockmanageCase.stockmanageTest("teststockmanage"))
#suite.addTest(stockmanageCase.stockmanageTest("assertskmanagebeforecheck"))
##suite.addTest(stockintocateCase.stockintocateTest("teststockintoCate"))
##suite.addTest(stockintocateCase.stockintocateTest("testitemseriesCate"))
##suite.addTest(stockreturnCase.stockreturnTest("teststockReturn"))
##suite.addTest(stockexchangeCase.stockexchangeTest("teststockExchange"))
##suite.addTest(paynotecCase.stockpayTest("teststockPay"))
##suite.addTest(stocknoteCase.stocknoteTest("teststockNote"))


##suite.addTest(newsaleorderCase.newsaleorderTest("testnewsaleOrder"))
##suite.addTest(saleordermanCase.saleordermanTest("testnewsaleorderMan"))
##suite.addTest(saleoutCase.saleoutTest("testsaleOut"))
##suite.addTest(saleoutCase.saleoutTest("testsaleitemseriseOut"))
##suite.addTest(salereturnCase.salereturnTest("testsaleReturn"))
##suite.addTest(saleexchangeCase.saleexchangeTest("testsaleExchange"))
##suite.addTest(salepayCase.salepayTest("testsalePay"))
##suite.addTest(entrustsaleCase.entrustsaleTest("testentrustSale"))
##suite.addTest(entrustreturnCase.entrustreturnTest("testentrustReturn"))
##suite.addTest(entrustaccCase.entrustaccTest("testentrustAcc"))
##suite.addTest(entruststockselCase.entruststockselTest("testentruststockSel"))
#suite.addTest(lsopenCase.lsopenTest("testlsOpen"))
#suite.addTest(lsreturnCase.lsreturnTest("testlsReturn"))
##suite.addTest(salenoteselCase.salenoteselTest("testsalenoteSel"))
#suite.addTest(itempricemanCase.itempricemanTest("testitempriceMan"))
#suite.addTest(saledistraceCase.saledistraceTest("testsaledisTrace"))

#suite.addTest(getlessnoteCase.getlessnoteTest("testgetlessNote"))
#suite.addTest(getlessnoteCase.getlessnoteTest("testgetitemseriesLess"))
#suite.addTest(getmorenoteCase.getmorenoteTest("testgetmoreNote"))
#suite.addTest(getmorenoteCase.getmorenoteTest("testgetitemseriesMore"))
##suite.addTest(transnoteCase.transnoteTest("testtransNote"))
#suite.addTest(transnoteCase.transnoteTest("testtranitemseries"))
#suite.addTest(changepriceCase.changepriceTest("testchangePrice"))
#suite.addTest(proasseCase.proasseTest("testproAsse"))
#suite.addTest(otherintoCase.otherintoTest("testotherInto"))
#suite.addTest(otherintoCase.otherintoTest("testotheritemSeriesinto"))
#suite.addTest(otheroutCase.otheroutTest("testotherOut"))
#suite.addTest(otheroutCase.otheroutTest("testotheritemseriesout"))
#suite.addTest(stockgridCase.stockgridTest("teststockGrid"))
##suite.addTest(gatherstockCase.gatherstockTest("testgatherStock"))
#suite.addTest(stockinventoryCase.stockinvTest("teststockInv"))
#suite.addTest(alarmsetCase.alarmsetTest("testalarmSet"))
#suite.addTest(alarmstartCase.alarmstartTest("testalarmStart"))
##suite.addTest(alarmupCase.alarmupTest("testalarmUp"))
##suite.addTest(alarmdownCase.alarmdownTest("testalarmDown"))
suite.addTest(seriesnotraceCase.seriesnotraceTest("testseriesnoTrace"))
#suite.addTest(seriesnostataselCase.seriesnostateselTest("testseriesnostateSale"))
#suite.addTest(test_innerdrawCase.innerdrawTest("test_innerDraw"))

#suite.addTest(test_paynoteCase.paynoteTest("test_payNote"))
#suite.addTest(test_receiptnoteCase.receiptnoteTest("test_receiptNote"))
#suite.addTest(test_costnoteCase.costnoteTest("test_costNote"))
#suite.addTest(test_otherreceiptCase.otherreceiptTest("test_otherReceipt"))
#suite.addTest(test_menexitranCase.menexitranTest("test_menexiTran"))
#suite.addTest(test_accdocCase.accdocTest("test_accDoc"))
#suite.addTest(test_companyrepaCase.companyrepaTest("test_companyrePa"))
#suite.addTest(test_checkfundaddCase.checkfundaddTest("test_checkfundAdd"))
#suite.addTest(test_checkfundreduceCase.checkfundreduceTest("test_checkfundReduce"))
#suite.addTest(test_checkaccreaddCase.checkaccreaddTest("test_checkaccreAdd"))
#suite.addTest(test_checkaccrereduceCase.checkaccrereduceTest("test_checkaccreReduce"))
#suite.addTest(test_checkaccpayaddCase.checkaccpayaddTest("test_checkaccpayAdd"))
#suite.addTest(test_checkaccpayreduceCase.checkaccpayreduceTest("test_checkaccpayReduce"))
#suite.addTest(test_fixcapbuyCase.fixcapbuyTest("test_fixcapBuy"))
#suite.addTest(test_fixcapsaleCase.fixcapsaleTest("test_fixcapSale"))
#suite.addTest(test_fixcapdeprCase.fixcapdeprTest("test_fixcapDepr"))
#suite.addTest(test_fixcapsetCase.fixcapsetTest("test_fixcapSet"))
#suite.addTest(test_endmanageCase.endmanageTest("test_endManage"))


#suite.addTest(test_instockorderCase.instockorderreportTest("test_instockorderReport"))
#suite.addTest(test_itemstockreoprt.itemstockreoportTest("test_iteminstockReport"))
#suite.addTest(test_instockdetailreport.instockdetailreoportTest("test_instockdetailReport"))
##suite.addTest(test_repsaleordercountCase.resaleorderTest("test_resaleOrder"))
##suite.addTest(test_resaleitemCase.resaleitemTest("test_resaleItem"))
#suite.addTest(test_resaleitemsareCase.resaleitemsareTest("test_resaleitemsaRe"))
##suite.addTest(test_resalebenefitCase.resalebenefitTest("test_resaleBenefit"))
#suite.addTest(test_resaleyearreportCase.resaleyearTest("test_resaleYear"))
#suite.addTest(test_resalemonthCase.resalemonthTest("test_resaleMonth"))
##suite.addTest(test_resaledetailCase.resaledetailTest("test_resaleDetail"))
##suite.addTest(test_resaleprofitCase.resaleprofitTest("test_resaleProfit"))
#suite.addTest(test_resalelsmoneyCase.resalelsmoneyTest("test_resaleLsmoney"))
#suite.addTest(test_resalelsitemCase.resalelsitemTest("test_resalelsItem"))
#suite.addTest(test_resalemenberscoresCase.resalemenberscoreTest("test_resalemenberScores"))
#suite.addTest(test_resalemenberchargeCase.resalemenberchargeTest("test_resalemenberCharge"))
#suite.addTest(test_resalestorelsCase.resalestorelsTest("test_resalestoreLs"))
#suite.addTest(test_resalepossaleCase.resalepossaleTest("test_resaleposSale"))
#suite.addTest(test_resalepackageCase.resalepackageTest("test_resalePackage"))

#suite.addTest(test_instkdayCase.inskdayTest("test_invskdaily"))
##suite.addTest(test_insklessCase.insklessTest("test_invskless"))

##suite.addTest(test_instkmoreCase.inskmoreTest("test_invskmore"))
#suite.addTest(test_instktranCase.insktranTest("test_invsktran"))
#suite.addTest(test_instkdismountCase.inskdismountTest("test_invskdismount"))
##suite.addTest(test_instkothintoCase.inskothintoTest("test_invskothinto"))
##suite.addTest(test_inskothoutCase.inskothoutTest("test_invskothout"))
##suite.addTest(test_inskinnerCase.inskinnerTest("test_invstkInner"))

#suite.addTest(test_finbusinessCase.finbusinessTest("test_finBusiness"))
#suite.addTest(test_finbusinessdailyCase.finbusinessdailyTest("test_finbusinessDaily"))
##suite.addTest(test_finbenfitCase.finbenfitTest("test_finBenfit"))
#suite.addTest(test_finbalanceCase.finbalanceTest("test_finBalance"))
#suite.addTest(test_finbossCase.finbossTest("test_finBoss"))

##suite.addTest(test_cominstockCase.cominstockTest("test_comiInstock"))
##suite.addTest(test_cominkreturnCase.cominkreturnTest("test_comiInkreturn"))
##suite.addTest(test_comsalereturnCase.comsalereturnTest("test_comiSalereturn"))
#-nodata#suite.addTest(test_combackmoneyCase.combackmoneyTest("test_comBackmoney"))
##suite.addTest(test_comcostgridCase.comcostgridTest("test_comCostgrid"))
##suite.addTest(test_combusinessCase.combusinessTest("test_comBusiness"))

#suite.addTest(test_depcostgridCase.depcostgridTest("test_depCostgrid"))
#suite.addTest(test_depbusinessCase.depbusinessTest("test_depBusiness"))
#suite.addTest(test_deppeogetCase.deppeogetTest("test_depPeoget"))
#suite.addTest(test_deppeocostgridCase.deppeocostgridTest("test_depPeocostGrid"))
#suite.addTest(test_deppeobusinessCase.deppeobusinessTest("test_depPeobusiness"))
#suite.addTest(test_depmkpeogetCase.depmkpeogetTest("test_depMkpeoget"))

runner = unittest.TextTestRunner()
runner.run(suite)





