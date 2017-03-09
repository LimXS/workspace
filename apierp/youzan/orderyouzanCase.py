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

class orderyouzanTest(unittest.TestCase):


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
        print u"有赞订单接口测试完成"
        pass


    def testorderYouzan(self):
        u'''有赞...将接口数据和页面数据进行对比'''
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

        apiurl="https://open.koudaitong.com/api/oauthentry/"
        sql="SELECT token FROM eshop WHERE shopAccount='15608199188'"
        token=basec.gettoken(sql)

        now=datetime.datetime.now()
        nowtime=now.strftime("%Y-%m-%d %H:%M:%S")
        print nowtime


        '''
        publics={"method":"vdian.order.get","access_token":token,"version":"1.0","format":"json"}
        #判断订单是否有遗漏下载
        paramsb={"page_num":1,"order_type":"","add_start":start,"add_end":end}
        publicsb={"method":"vdian.order.list.get","access_token":token,"version":"1.1","format":"json"}
        payloadb={"param":json.dumps(paramsb),"public":json.dumps(publicsb)}
        apiresb=requests.post(apiurl,data=payloadb)
        apidatab=json.loads(apiresb.text)
        total=str(apidatab['result']['total_num'])

        if total!=str(len(lis)):
            print "接口返回的订单数目和页面显示的订单数目不一致，请检查是否有遗漏下载"
        '''


        #每一个订单数据进行对比
        flagid=''
        for k in range(0,len(lis)):
            try:
                if flagid!=lis[k][0]:
                    if lis[k][99]=='869326195688954':
                        print "api:"+str(lis[k][0])
                        id=lis[k][0]
                        payload={"access_token":token,"method":"kdt.trade.get","tid":id}
                        apires=requests.post(apiurl,data=payload)
                        print apires.text
                        apidata=json.loads(apires.text)
                        print apidata

                        orcompary=ordercompare.ordercompary(lis,(k))

                        #付款时间
                        apitime=apidata["response"]["trade"]["pay_time"]
                        orcompary.pay_times(apitime)


                        #卖家备注
                        apisalenote=str(apidata["response"]["trade"]["trade_memo"]).strip()
                        orcompary.sale_note(str(apisalenote))

                        #买家备留言
                        apibuynote=apidata["response"]["trade"]["buyer_message"].strip()
                        orcompary.buyer_note(apibuynote)


                        #订单金额
                        apimoney=apidata["response"]["trade"]["total_fee"]
                        orcompary.money_fee(apimoney)

                        #订单优惠金额

                        #print type(apidata["data"]["parent_order_ump"].encode('utf-8'))
                        if len(apidata["response"]["trade"]["adjust_fee"])>0:
                            apidis1=float(apidata["response"]["trade"]["adjust_fee"]["pay_change"])
                        else:
                            apidis1=0.00
                        apidis2=float(apidata["response"]["trade"]["discount_fee"])
                        #print "apdis..............................."
                        #print apidis
                        apidisw=str("%.2f"%(apidis1+apidis2))
                        #print apidisw

                        disw=str("%.2f"%apidisw)

                        orcompary.dis_money(disw)

                        #金额
                        comtr=str(apidata["response"]["trade"]["total_fee"])
                        orcompary.order_money(comtr)
                        




                        #省份
                        apiprovince=apidata["response"]["trade"]["receiver_state"]
                        orcompary.province(apiprovince)

                        #物流公司&物流单号
                        payload2={"access_token":token,"method":"kdt.logistics.trace.search","tid":id}
                        apires2=requests.post(apiurl,data=payload2)
                        #print apires2.text
                        apidata2=json.loads(apires2.text)
                        #print "物流信息......................................................"
                        #print apidata2
                        try:
                            company_name=apidata2["response"]["company_name"]
                            out_sid=apidata2["response"]["out_sid"]
                            company=1
                        except:
                            company=0
                            company_name='null'
                            out_sid=''

                        orcompary.express_company(company_name)
                        orcompary.express_no(out_sid)



                        #网店名称
                        apisalername=apidata["response"]["trade"]["orders"][0]["seller_nick"]
                        orcompary.shopname(apisalername)


                        #退款状态为正常
                        refund_status=apidata["response"]["trade"]["refund_state"]
                        if refund_status=='NO_REFUND':
                            refund='0'
                        elif refund_status=='PARTIAL_REFUNDING' or refund_status=='PARTIAL_REFUNDED' or refund_status=='PARTIAL_REFUNDING' :
                            refund='1'
                        elif refund_status=='PARTIAL_REFUNDED' and refund_status=='FULL_REFUNDED':
                            refund='3'
                        else:
                            refund=refund_status
                            print refund_status
                        orcompary.refund_status(refund)


                        #交易状态
                        trstatus=apidata["response"]["trade"]["status"]
                        if trstatus=='WAIT_BUYER_PAY':
                            status='1'
                        elif trstatus=='WAIT_SELLER_SEND_GOODS' or trstatus=='WAIT_GROUP':
                            status='2'
                        elif trstatus=='WAIT_BUYER_CONFIRM_GOODS'or trstatus=='TRADE_BUYER_SIGNED':
                            status='3'
                        elif trstatus=='TRADE_CLOSED_BY_USER':
                            status='5'
                        elif trstatus=='TRADE_CLOSED':
                            status='4'
                        else:
                            status=trstatus
                        orcompary.trade_status(status)



                        #买家运费

                        apifee=float(apidata["response"]["trade"]["post_fee"])
                        apifee=str("%.2f"%apifee)
                        orcompary.post_fee(apifee)

                        #收货地址
                        pro=apidata["response"]["trade"]["receiver_district"].strip()
                        city=apidata["response"]["trade"]["receiver_name"].strip()
                        district=apidata["response"]["trade"]["receiver_state"].strip()
                        add=apidata["response"]["trade"]["receiver_address"].strip()
                        adds=district+pro+add
                        orcompary.address(adds)

                        #交易类型
                        typetrade=apidata["response"]["trade"]["type"]
                        if typetrade.strip()=='COD':
                            trtype='3'
                        elif typetrade=='FIXED':
                            trtype='0'
                        else:
                            trtype=typetrade
                            print typetrade
                        orcompary.trade_type(trtype)

                        #订单详情
                        for n in range(len(apidata["response"]["trade"]["orders"])):
                            print "api:"+apidata["response"]["trade"]["orders"][n]['title']
                            print "erp:"+lis[k+n+1][28]

                            #线上宝贝名称
                            apiitemname=apidata["response"]["trade"]['orders'][n]['title']
                            orcompary.item_name(apiitemname,n+1)

                            #线上销售属性
                            try:
                                apiitemtype=apidata["response"]["trade"]['orders'][n]['sku_properties_name']+';'
                                apiitemtype=re.findall(':(.*?);',apiitemtype)
                                de=''
                                for detail in range(len(apiitemtype)):
                                    de=de+apiitemtype[detail]+'_'
                                apiitemtype=de[:-1]
                            except:
                                apiitemtype=apiitemname
                            orcompary.item_type(apiitemtype,n+1)

                            #线上商家编码
                            apiitemcode=apidata["response"]["trade"]['orders'][n]['outer_sku_id']
                            orcompary.item_salecode(apiitemcode,n+1)

                            #商品数量
                            itemsnum=apidata["response"]["trade"]['orders'][n]['num']
                            orcompary.item_num(int(itemsnum),n+1)

                            discount=float(apidisw)/(float(apimoney)+float(apidisw))

                            #订单金额
                            orderprice=apidata["response"]["trade"]["orders"][n]['total_fee']
                            detailprice=float(orderprice)*(1-discount)
                            detailprice=str("%.2f"%detailprice)
                            orcompary.order_price(detailprice,n+1)

                            #金额
                            orcompary.order_moneydetail(detailprice,n+1)

                            #单价
                            sigle=float(orderprice)/float(itemsnum)
                            sigle=str("%.2f"%sigle)
                            orcompary.item_order(sigle)

                            #优惠

                            itdis=float(apidata["response"]["trade"]["orders"][n]["price"])*discount*int(itemsnum)
                            itdis=str("%.2f"%itdis)
                            orcompary.item_dis(itdis)



                #flag=flag+1
                flagid=lis[k][0]
                #print "flag-------------------------------:"+str(flag)

            except:
                #flag=flag+1
                flagid=lis[k][0]
                print(u"订单数据比对失败")
                print(traceback.format_exc())




if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testAccredit']
    unittest.main()