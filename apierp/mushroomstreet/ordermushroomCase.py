#*-* coding:UTF-8 *-*
from common import base
from common import ordercompare
import unittest
import traceback
import re
import requests
import json
import time
import datetime
import sys

reload(sys)
sys.setdefaultencoding( "utf-8" )

basec=base.baseCommon()

class ordermushroomTest(unittest.TestCase):


    def setUp(self):
        self.driver=basec.startBrowser('chrome')
        basec.set_up(self.driver)
        #get the session cookie
        cookie = [item["name"] + "=" + item["value"] for item in self.driver.get_cookies()]
        #print cookie
        self.cookiestr = ';'.join(item for item in cookie)
        time.sleep(2)
        pass


    def tearDown(self):
        self.driver.close()
        print u"蘑菇街订单接口测试完成"
        pass


    def testorderMushroom(self):
        u'''蘑菇街..将接口数据和页面数据进行对比'''
        #获取订单页面数据并放入列表

        aa='http://beefun.wsgjp.com/EShopDeliver/EShopDeliverList.gspx?caption=%B6%A9%B5%A5%B4%A6%C0%ED&tag=SimpleProcessStatus'
        headers = {'cookie':self.cookiestr,'Content-Type': 'application/json'}
        payloads={"pagerId":"$390deff7$deliverMainGrid_pager1","queryParams":{"processtype":0,"quickQuery":"0","tradeid":"","freightbillno":"","customershopaccount":"","customerreceiver":"","customerreceivermobile":"","customerreceiverphone":"","Summary":"","PtypeName":"","SellerMemo":"","BuyerMessage":"","Address":"","SubFreightBillNo":"","isExact":False,"keyword":"","timetype":3,"begintime":"2016-05-27 00:00:00","endTime":"2016-06-03 23:59:59","eshopid":["869326195688954"],"logisticid":[],"ktypeid":[],"province":[],"city":[],"district":[],"refundstatus":-1,"sellerflag":"-1","tradestatus":"-1","processstatus":-1,"invoicestatus":-1,"tradetype":-1,"createtype":-1,"eshoptype":-1,"printfreightstatus":-1,"printsendstatus":-1,"printassignstatus":-1,"customsprocessstatus":"-1","mixqty":None,"maxqty":None,"mixptypekindcount":None,"maxptypekindcount":None,"mixweight":None,"maxweight":None,"mixvolume":None,"maxvolume":None,"mixtotal":None,"maxtotal":None,"needinvoice":-1,"saletype":-1,"filtertype":"tradeid","collectType":-2,"BatchId":0},"orders":None,"filter":None,"first":0,"count":50}

        #取页面数据
        bb=basec.postRead(self.driver,aa,payloads,headers)
        lis=basec.erpOrder(bb)


        #b=basec.handleorderRead(self.driver,aa, headers)
        #lis=basec.erpOrder(b)

        #取接口数据并进行比对
        timelist=basec.getTime()
        start=timelist[1]
        end=timelist[0]
        flag=0

        apiurl="https://www.mogujie.com/openapi/api_v1_api/index"
        sql="SELECT token FROM eshop WHERE etypeid='2605638079543105363'"
        tokenall=basec.gettokeneach(sql)
        token=str(tokenall[2])
        token=re.findall('\'(.*?)\'',token)
        token=token[0].strip()
        print "token.................."
        print token

        now=datetime.datetime.now()
        nowtime=now.strftime("%Y-%m-%d %H:%M:%S")
        print nowtime

        #每一个订单数据进行对比
        flagid=''
        for k in range(0,len(lis)):
            try:
                if flagid!=lis[k][0]:
                    if lis[k][99]=='869378240461870':
                        print "api:"+str(lis[k][0])
                        id=lis[k][0]
                        payload={"access_token":token,"method":"youdian.trade.get","app_key":"6186bd31891451899b385b2aa8ce3713","tid":id}
                        apires=requests.post(url=apiurl,data=payload)
                        print apires.text
                        apidata=json.loads(apires.text)
                        print apidata
                        orcompary=ordercompare.ordercompary(lis,(k))

                        #付款时间
                        apitime=apidata['result']['data']['pay_time']
                        orcompary.pay_times(apitime)

                        #卖家备注
                        apisalenote=apidata['result']['data']['trade_memo'].strip()
                        orcompary.sale_note(str(apisalenote))

                        #买家备留言
                        apibuynote=apidata['result']['data']['buyer_memo']
                        orcompary.buyer_note(apibuynote)

                        #订单金额
                        '''
                        totalmoney=apidata['result']['data']['total_trade_fee']
                        expressmoney=apidata['result']['data']['ship_expense']
                        apimoney=totalmoney-expressmoney
                        if apimoney!=0:
                            apimoney=str(apimoney*0.01)
                            apimoney=float(apimoney)
                            apimoney=str("%.2f"%apimoney)
                        else:
                            apimoney='0.00'
                        '''
                        apimoney=apidata["result"]["data"]["goods_price"]
                        apimoney=str("%.2f"%apimoney)
                        orcompary.money_fee(apimoney)


                        #订单优惠金额

                        dis1=apidata["result"]["data"]["goods_discount_fee"]*0.01
                        dis2=apidata["result"]["data"]["orders_discount_fee"]*0.01
                        apidis=dis1+dis2
                        apidis=str("%.2f"%apidis)
                        orcompary.dis_money(apidis)

                        #金额

                        orcompary.order_money(apimoney)

                        itdiscount=float(apidis)/(float(apimoney)+float(apidis))

                        #省份
                        apiprovince=apidata['result']['data']['receiver_state']
                        orcompary.province(apiprovince)

                        #物流公司
                        express={"shunfeng":"顺丰速运","yunda":"韵达快运","yuantong":"圆通速递","shentong":"申通快递","zhongtong":"中通速递","tiantian":"天天快递","huitongkuaidi":"汇通快运","ems":"EMS","emsguoji":"EMS国际","youzhengguonei":"邮政包裹","youshuwuliu":"优速快递","guotongkuaidi":"国通快递","quanfengkuaidi":"全峰快递","zhaijisong":"宅急送","kuaijiesudi":"快捷速递"}
                        if apidata['result']['data']['logistics_name']==None:
                            apiexpress='null'
                        else:
                            apiexpress=apidata['result']['data']['logistics_name']
                            apiexpress=express[apiexpress]
                        orcompary.express_company(apiexpress)

                        #物流单号
                        if apidata['result']['data']['logistics_no']==None:
                            apino=''
                        else:
                            apino=apidata['result']['data']['logistics_no']
                        orcompary.express_no(apino)

                        #网店名称
                        apisalername=apidata['result']['data']['seller_uname']
                        orcompary.shopname(apisalername)

                        #退款状态
                        refundstatus=apidata['result']['data']['pay_status']
                        if refundstatus=='REFUNDING':
                            refund='1'
                        elif refundstatus=='REFUND_PART' or refundstatus=='REFUND_ALL':
                            refund='2'
                        else:
                            refund='0'
                            print str(refundstatus)
                        orcompary.refund_status(refund)


                        #交易状态
                        trstatus=apidata['result']['data']['status']
                        paystatus=apidata['result']['data']['pay_status']
                        shipstatus=apidata['result']['data']['ship_status']
                        if trstatus=='TRADE_CLOSED':
                            status='5'
                        elif trstatus=='TRADE_FINISHED':
                            status='4'
                        elif trstatus=='TRADE_UNPAYED' and paystatus=='PAY_NO':
                            status='1'
                        elif trstatus=='TRADE_ACTIVE' and paystatus=='PAY_FINISH' and shipstatus=='SHIP_NO':
                            status='2'
                        elif shipstatus=='SHIP_PREPARE'or shipstatus=='SHIP_RECEIVED':
                            status='3'
                        else:
                            status=apidata['result']['data']['status']
                            print paystatus
                            print shipstatus
                        orcompary.trade_status(status)


                        #买家运费
                        if apidata['result']['data']['ship_expense']!=0:
                            apifee=str(apidata['result']['data']['ship_expense']*0.01)
                            apifee=float(apifee)
                            apifee=str("%.2f"%apifee)
                        else:
                            apifee='0.00'
                        orcompary.post_fee(apifee)

                        #收货地址
                        pro=apidata['result']['data']['receiver_state'].strip()
                        city=apidata['result']['data']['receiver_city'].strip()
                        district=apidata['result']['data']['receiver_district'].strip()
                        add=apidata['result']['data']['receiver_address'].strip()
                        adds=pro+city+district+add
                        orcompary.address(adds)

                        #交易类型
                        typetrade=apidata['result']['data']['tradetype']
                        if typetrade=='fixed':
                            type='0'
                        elif typetrade=='presell':
                            type='1'
                        else:
                            print str(typetrade)
                            type=typetrade
                        orcompary.trade_type(type)

                        #子订单
                        detailnum=len(apidata['result']['data']['orders'])
                        for n in range(0,detailnum):
                            print "api:"+apidata['result']['data']['orders'][n]['title']
                            print "erp:"+lis[k+n+1][28]
                            #线上宝贝名称
                            apiitemname=apidata['result']['data']['orders'][n]['title']
                            orcompary.item_name(apiitemname,n+1)

                            #线上销售属性
                            try:
                                apiitemtype=apidata['result']['data']['orders'][n]['sku_properties']+';'
                                apiitemtype=re.findall(':(.*?);',apiitemtype)
                                de=''
                                for detail in range(len(apiitemtype)):
                                    de=de+apiitemtype[detail]+'_'
                                apiitemtype=de[:-1]
                            except:
                                apiitemtype=''
                            orcompary.item_type(apiitemtype,n+1)

                            #线上商家编码
                            apiitemcode=apidata['result']['data']['orders'][n]['sku_bn']
                            orcompary.item_salecode(apiitemcode,n+1)

                            #商品数量
                            itemsnum=apidata['result']['data']['orders'][n]['items_num']
                            orcompary.item_num(int(itemsnum),n+1)

                            #订单金额
                            orderprice=apidata['result']['data']['orders'][n]['total_order_fee']
                            if orderprice!=0:
                                orderprice=str(orderprice*0.01)
                                orderprice=float(orderprice)*(1-itdiscount)
                                orderprice=str("%.2f"%orderprice)
                            else:
                                orderprice='0.00'
                            orcompary.order_price(orderprice,n+1)

                            #金额

                            orcompary.order_moneydetail(orderprice,n+1)

                            #单价
                            sigle=float(orderprice)/float(itemsnum)
                            sigle=str("%.2f"%sigle)
                            orcompary.item_order(sigle)

                            #优惠
                            itdis=float(apidata["result"]["data"]["orders"][n]["sale_price"])*itdiscount*0.01*int(itemsnum)
                            itdis=str("%.2f"%itdis)
                            orcompary.item_dis(itdis)

                flagid=lis[k][0]
                #flag=flag+1
                #print "flag-------------------------------:"+str(flag)

            except:
                #flag=flag+1
                flagid=lis[k][0]
                print(u"订单数据比对失败")
                print(traceback.format_exc())


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testAccredit']
    unittest.main()