#*-* coding:UTF-8 *-*
import unittest
import time
import re
import base
basec=base.baseCommon()
class ordercompary(unittest.TestCase):

    def __init__(self,lis,n):
        unittest.TestCase.__init__(self,'commonfun')
        self.lis=lis
        self.n=n


    def commonfun(self,apievery,x,msg):
        #随意
        try:
            self.assertEqual(self.lis[self.n][x].strip(),apievery,msg=msg)
            print "assert ok"
        except AssertionError,msg:
            print msg
            print u"订单编号："+self.lis[self.n][0].strip()
            print u"接口返回："+str(apievery)
            print u"页面："+str(self.lis[self.n][x].strip())+"\n"


    def pay_times(self,apipaytime):
        #付款时间
        try:
            if self.lis[self.n][9].strip()!='null' and self.lis[self.n][9].strip()!='':
                timestr=re.findall("\((.*?)\)",self.lis[self.n][9])
                dst = '.'.join(timestr)

                print "dst-----------------------------"+str(dst)
                timeint=int(dst)/1000
            else:
                timeint=''
                #转换接口时间为时间戳
            if apipaytime!='' and apipaytime!='null' and apipaytime!= '0000-00-00 00:00:00':
                apipaytime = time.strptime(apipaytime, "%Y-%m-%d %H:%M:%S")
                apipaytime = str(time.mktime(apipaytime))
            else:
                apipaytime=''


        except:
            print u"时间转换失败"
            print u"订单编号："+self.lis[self.n][0]
            print u"接口返回付款时间pay_time："+str(apipaytime)
            print u"页面付款时间："+str(self.lis[self.n][9].strip())
        try:
            self.assertEqual(timeint,apipaytime,msg="付款时间不一致")
            print "assert pay_time ok"
        except AssertionError,msg:
            print msg
            print u"订单编号："+self.lis[self.n][0]
            print u"接口返回付款时间pay_time："+str(apipaytime)
            print u"页面付款时间："+str(self.lis[self.n][9].strip())



    def sale_note(self,apinote):
        #卖家备注
        try:
            self.assertEqual(str(self.lis[self.n][7].strip()),apinote,msg="卖家备注不一致")
            print "assert sale_noete ok"
        except AssertionError,msg:
            print msg
            print u"订单编号："+self.lis[self.n][0].strip()
            print u"接口返回卖家备注："+str(apinote)
            print u"页面卖家备注："+str(self.lis[self.n][7].strip())+"\n"


    def buyer_note(self,apibuynote):
        #买家备注
        try:
            self.assertEqual(self.lis[self.n][6].strip(),apibuynote,msg="买家备注不一致")
            print "assert buyer_note ok"
        except AssertionError,msg:
            print msg
            print u"订单编号："+self.lis[self.n][0].strip()
            print u"接口返回买家备注："+str(apibuynote)
            print u"页面买家备注："+str(self.lis[self.n][6].strip())+"\n"

    def province(self,apipro):
        #省份
        try:
            self.assertEqual(self.lis[self.n][53].strip(),apipro,msg="省份不一致")
            print "assert province ok"
        except AssertionError,msg:
            print msg
            print u"订单编号："+self.lis[self.n][0].strip()
            print u"接口返回省份："+str(apipro)
            print u"页面省份："+str(self.lis[self.n][53].strip())+"\n"


    def shopname(self,apishopname):
        #网店名称
        try:
            self.assertEqual(self.lis[self.n][69].strip(),apishopname,msg="网店名称不一致")
            print "assert shopname ok"
        except AssertionError,msg:
            print msg
            print u"订单编号："+self.lis[self.n][0].strip()
            print u"接口返回网店名称："+str(apishopname)
            print u"页面网店名称："+str(self.lis[self.n][69].strip())+"\n"


    def express_fee(self,apiexfee):
        #运费
        con=float(self.lis[self.n][42])
        conw=str("%.2f"%con)
        try:
            self.assertEqual(conw,apiexfee,msg="运费不一致")
            print "assert express_fee ok"
        except AssertionError,msg:
            print msg
            print u"订单编号："+self.lis[self.n][0].strip()
            print u"接口返回收货地址："+str(apiexfee)
            print u"页面收货地址："+str(conw)+"\n"


    def address(self,apiaddress):
        #收货地址
        try:
            self.assertEqual(self.lis[self.n][61].strip(),apiaddress,msg="收货地址不一致")
            print "assert address ok"
        except AssertionError,msg:
            print msg
            print u"订单编号："+self.lis[self.n][0].strip()
            print u"接口返回收货地址："+str(apiaddress)
            print u"页面收货地址："+str(self.lis[self.n][61].strip())+"\n"


    def express_company(self,apicompany):
        #物流公司
        erpcompany=self.lis[self.n][71].strip()

        try:
            self.assertEqual(self.lis[self.n][71].strip(),apicompany,msg=u"物流公司不一致")
            print "assert express_company ok"
        except AssertionError,msg:
            print u"订单号为："+self.lis[self.n][0].strip()
            print msg
            print u"订单页面物流公司："+self.lis[self.n][71].strip()
            print u"api接口返回的数据："+str(apicompany)+"\n"

        return erpcompany


    def express_no(self,apinum):
        #物流单号
        expressno=self.lis[self.n][4].strip()
        try:
            self.assertEqual(expressno,apinum,msg="快递单号不一致")
            print "assert express_no ok"
        except AssertionError,msg:
            print u"订单号为："+self.lis[self.n][0].strip()
            print msg
            print u"订单页面物流单号："+self.lis[self.n][4].strip()
            print u"api接口返回的数据："+str(apinum)+"\n"

        return expressno


    def refund_status(self,apirefundstatus):
        #退款状态
        erprefund=self.lis[self.n][62].strip()
        try:
            self.assertEqual(erprefund,apirefundstatus,msg="退款状态不一致")
            print "assert refundstatus ok"
        except  AssertionError,msg:
            print u"订单号为："+self.lis[self.n][0].strip()
            print msg
            print u"订单页面退款状态："+self.lis[self.n][62].strip()
            print u"api接口返回的数据："+str(apirefundstatus)+"\n"
        return  erprefund

    def trade_status(self,apitradestatus):
        #交易状态
        erpstatus=self.lis[self.n][26].strip()
        try:
            self.assertEqual(erpstatus,apitradestatus,msg="交易状态不一致")
            print "assert tradestatus ok"
        except  AssertionError,msg:
            print u"订单号为："+self.lis[self.n][0].strip()
            print msg
            print u"订单页面交易状态："+self.lis[self.n][26].strip()
            print u"api接口返回的数据："+str(apitradestatus)+"\n"
        return erpstatus

    def trade_type(self,apitype):
        #交易类型
        erptype=self.lis[self.n][70].strip()
        try:
            self.assertEqual(erptype,apitype,msg="交易类型不一致")
            print "assert tradetype ok"
        except  AssertionError,msg:
            print u"订单号为："+self.lis[self.n][0].strip()
            print msg
            print u"订单页面交易类型："+self.lis[self.n][70].strip()
            print u"api接口返回的数据："+str(apitype)+"\n"
        return erptype

    def post_fee(self,apifee):
        con=float(self.lis[self.n][42].strip())
        conw=str("%.2f"%con)
        try:
            self.assertEqual(conw,apifee,msg="快递金额不一致")
            print "assert postfee ok"
        except  AssertionError,msg:
            print u"订单号为："+self.lis[self.n][0].strip()
            print msg
            print u"订单页面运费："+self.lis[self.n][42].strip()
            print u"api接口返回的数据："+str(apifee)+"\n"
        return conw

    def money_fee(self,apimoney):
         mytotal=float(self.lis[self.n][85].strip())
         total=str("%.2f"%mytotal)
         try:
            self.assertEqual(total,apimoney,msg=u"金额不一致")
            print "assert money_fee ok"
         except  AssertionError,msg:
            print u"订单号为："+self.lis[self.n][0].strip()
            print msg
            print u"订单页面金额："+self.lis[self.n][85].strip()
            print u"api接口返回的数据："+str(apimoney)+"\n"
         return total

    def order_money(self,apiordermoney):
         ordermoney=float(self.lis[self.n][18].strip())
         ordermoney=str("%.2f"%ordermoney)
         try:
            self.assertEqual(ordermoney,apiordermoney,msg=u"订单金额不一致")
            print "assert order_money ok"
         except  AssertionError,msg:
            print u"订单号为："+self.lis[self.n][0].strip()
            print msg
            print u"订单页面订单金额："+self.lis[self.n][18].strip()
            print u"api接口返回的数据："+str(apiordermoney)+"\n"
         return ordermoney

    def dis_money(self,apidismoney):
         dismoney=float(self.lis[self.n][19].strip())
         dismoney=str("%.2f"%dismoney)
         try:
            self.assertEqual(dismoney,apidismoney,msg=u"订单优惠金额不一致")
            print "assert dis_money ok"
         except  AssertionError,msg:
            print u"订单号为："+self.lis[self.n][0].strip()
            print msg
            print u"订单页面订单优惠金额："+self.lis[self.n][19].strip()
            print u"api接口返回的数据："+str(apidismoney)+"\n"
         return dismoney

        #子订单
    def item_name(self,apiitemname,num):
        #线上宝贝名称
        erpname=self.lis[self.n+num][28].strip()
        try:
            self.assertEqual(erpname,apiitemname,msg="子订单线上宝贝名称不一致")
            print "assert item_name ok"
        except  AssertionError,msg:
            print u"订单号为："+self.lis[self.n+num][0].strip()
            print msg
            print u"订单页面线上宝贝名称："+self.lis[self.n+num][28].strip()
            print u"api接口返回的数据："+str(apiitemname)+"\n"
        return erpname

    def item_type(self,apiitemtype,num):
        #线上销售属性
        erptype=self.lis[self.n+num][45].strip()
        try:
            self.assertEqual(erptype,apiitemtype,msg="子订单线上销售属性不一致")
            print "assert item_type ok"
        except  AssertionError,msg:
            print u"订单号为："+self.lis[self.n+num][0].strip()
            print msg
            print u"订单页面线上销售属性名称："+self.lis[self.n+num][45].strip()
            print u"api接口返回的数据："+str(apiitemtype)+"\n"
        return erptype

    def item_salecode(self,apisalecode,num):
        #线上商家编码
        erpcode=self.lis[self.n+num][46].strip()
        try:
            self.assertEqual(erpcode,apisalecode,msg="子订单线上商家编码不一致")
            print "assert item_salecode ok"
        except  AssertionError,msg:
            print u"订单号为："+self.lis[self.n+num][0].strip()
            print msg
            print u"订单页面线上商家编码："+self.lis[self.n+num][46].strip()
            print u"api接口返回的数据："+str(apisalecode)+"\n"
        return erpcode

    def erpitem_name(self,apiname,num):
        #商品名称
        erpitemname=self.lis[self.n+num][53].strip()
        try:
            self.assertEqual(erpitemname,apiname,msg="子订单商品名称不一致")
            print "assert erpitem_name ok"
        except  AssertionError,msg:
            print u"订单号为："+self.lis[self.n+num][0].strip()
            print msg
            print u"订单页面商品名称："+self.lis[self.n+num][53].strip()
            print u"api接口返回的数据："+str(apiname)+"\n"
        return erpitemname

    def item_code(self,apidata,num):
        #商品编号
        erpitemcode=self.lis[self.n+num][54].strip()
        try:
            self.assertEqual(erpitemcode,apidata,msg="子订单线上商家编码不一致")
            print "assert item_salecode ok"
        except  AssertionError,msg:
            print u"订单号为："+self.lis[self.n+num][0].strip()
            print msg
            print u"订单页面线上商家编码："+self.lis[self.n+num][54].strip()
            print u"api接口返回的数据："+str(apidata)+"\n"
        return erpitemcode

    def item_skucode(self,apiskucode,num):
        #SKU编号
        erpskucode=self.lis[self.n+num][55].strip()
        try:
            self.assertEqual(erpskucode,apiskucode,msg="子订单SKU编号不一致")
            print "assert item_skucode ok"
        except  AssertionError,msg:
            print u"订单号为："+self.lis[self.n+num][0].strip()
            print msg
            print u"订单页面SKU编号："+self.lis[self.n+num][55].strip()
            print u"api接口返回的数据："+str(apiskucode)+"\n"
        return erpskucode

    def item_num(self,apidata,num):
        #商品数量
        itemnum=self.lis[self.n+num][2].strip()
        itemnum=float(itemnum)
        itemnum=int(itemnum)
        try:
            self.assertEqual(itemnum,apidata,msg="子订单商品数量不一致")
            print "assert item_num ok"
        except  AssertionError,msg:
            print u"订单号为："+self.lis[self.n+num][0].strip()
            print msg
            print u"订单页面商品数量："+self.lis[self.n+num][2].strip()
            print u"api接口返回的数据："+str(apidata)+"\n"
        return itemnum


    def item_order(self,apidata,num):
        #订单单价
        itemorder=self.lis[self.n+num][3].strip()
        itemorder=float(itemorder)
        itemorder=str("%.2f"%itemorder)
        try:
            self.assertEqual(itemorder,apidata,msg="子订单订单单价不一致")
            print "assert item_order ok"
        except  AssertionError,msg:
            print u"订单号为："+self.lis[self.n+num][0].strip()
            print msg
            print u"订单页面订单单价："+self.lis[self.n+num][3].strip()
            print u"api接口返回的数据："+str(apidata)+"\n"
        return itemorder

    def order_price(self,apidata,num):
        #订单金额
        orderprice=self.lis[self.n+num][4].strip()
        orderprice=float(orderprice)
        orderprice=str("%.2f"%orderprice)
        try:
            self.assertEqual(orderprice,apidata,msg="子订单订单金额不一致")
            print "assert order_price ok"
        except  AssertionError,msg:
            print u"订单号为："+self.lis[self.n+num][0].strip()
            print msg
            print u"订单页面订单金额："+self.lis[self.n+num][4].strip()
            print u"api接口返回的数据："+str(apidata)+"\n"
        return orderprice



    def order_moneydetail(self,apidata,num):
        #金额
        ordermoneydetail=self.lis[self.n+num][8].strip()
        ordermoneydetail=float(ordermoneydetail)
        ordermoneydetail=str("%.2f"%ordermoneydetail)
        try:
            self.assertEqual(ordermoneydetail,apidata,msg=u"子订单金额不一致")
            print "assert item_order ok"
        except  AssertionError,msg:
            print u"订单号为："+self.lis[self.n+num][0].strip()
            print msg
            print u"订单页面金额："+self.lis[self.n+num][8].strip()
            print u"api接口返回的数据："+str(apidata)+"\n"
        return ordermoneydetail

    def item_dis(self,apidata,num):
        #优惠
        ordersingle=self.lis[self.n+num][5].strip()
        ordersingle=float(ordersingle)
        ordersingle=str("%.2f"%ordersingle)
        try:
            self.assertEqual(ordersingle,apidata,msg=u"子订单优惠不一致")
            print "assert item_dis ok"
        except  AssertionError,msg:
            print u"订单号为："+self.lis[self.n+num][0].strip()
            print msg
            print u"订单页面明细优惠："+self.lis[self.n+num][5].strip()
            print u"api接口返回的数据："+str(apidata)+"\n"
        return ordersingle


