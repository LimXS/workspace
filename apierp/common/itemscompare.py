#*-* coding:UTF-8 *-*
import re
import base
basec=base.baseCommon()
class commonitemscompary():

    def __init__(self,resault):
        self.iresault=resault

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def commonfun(self,apievery,x,msg):
        #随意
        try:
            assert self.iresault[x]==apievery
            print "assert  ok"
        except AssertionError,msg:
            print msg
            print u"订单编号："+self.lis[self.n][0].strip()
            print u"接口返回："+str(apievery)
            print u"页面："+str(self.lis[self.n][x].strip())+"\n"


    def item_name(self,apiname):
        #名字/sku具体型号
        erpname=self.iresault[12]
        try:
            assert apiname==erpname
            print "assert title ok"
        except AssertionError:
            print "商品名字不一致"
            print str(apiname)
            print erpname


    def item_num(self,apinum):
        #库存/sku库存
        erpnum=self.iresault[10]
        erpnum=erpnum[:-5]
        try:
            assert str(apinum)==str(erpnum)
            print "assert stock ok"
        except AssertionError:
            print "商品库存不一致"
            print str(apinum)
            print erpnum


    def item_type(self,apiid):
        #型号
        erpid=self.iresault[14]
        try:
            assert apiid==erpid
            print "assert total ok"
        except AssertionError:
            print "商品型号不一致"
            print str(apiid)
            print erpid

    def item_skuid(self,apiid):
        #sku具体编号
        erpid=self.iresault[9]
        try:
            assert apiid==erpid
            print "assert total ok"
        except AssertionError:
            print "sku商品型号不一致"
            print str(apiid)
            print erpid







