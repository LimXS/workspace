#*-* coding:UTF-8 *-*
from common import base
from common import ordercompare
import unittest
import traceback
import re
import requests
import json
import time

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import gettokenwei
basec=base.baseCommon()

class orderweiTest(unittest.TestCase):


    def setUp(self):
        self.driver=basec.startBrowser('chrome')
        basec.set_up(self.driver)
        #get the session cookie
        cookie = [item["name"] + "=" + item["value"] for item in self.driver.get_cookies()]
        #print cookie
        self.cookiestr = ';'.join(item for item in cookie)
        time.sleep(2)
        gettokenwei.gettokenWei()
        pass


    def tearDown(self):
        self.driver.close()
        print u"微店订单接口测试完成"
        pass


    def testorderWei(self):
        u'''微店...将接口数据和页面数据进行对比'''
        #获取订单页面数据并放入列表

        aa='http://beefun.wsgjp.com/EShopDeliver/EShopDeliverList.gspx?caption=%B6%A9%B5%A5%B4%A6%C0%ED&tag=SimpleProcessStatus'
        headers = {'cookie':self.cookiestr,'Content-Type': 'application/json'}

        #取页面数据
        b=basec.handleorderRead(self.driver,aa, headers)
        lis=basec.erpOrder(b)

        #取接口数据并进行比对
        timelist=basec.getTime()
        start=timelist[1]
        end=timelist[0]
        flag=0
        apiurl='http://api.vdian.com/api'
        f=open(r"C:\workspace\apierp\sp.dat","r")
        token=f.read()
        print "token:"+token
        publics={"method":"vdian.order.get","access_token":token,"version":"1.0","format":"json"}
        #判断订单是否有遗漏下载
        paramsb={"page_num":1,"order_type":"","add_start":start,"add_end":end}
        publicsb={"method":"vdian.order.list.get","access_token":token,"version":"1.1","format":"json"}
        payloadb={"param":json.dumps(paramsb),"public":json.dumps(publicsb)}
        apiresb=requests.post(apiurl,data=payloadb)
        apidatab=json.loads(apiresb.text)
        print apidatab
        print token
        total=str(apidatab['result']['total_num'])
        if total!=str(len(lis)):
            print "接口返回的订单数目和页面显示的订单数目不一致，请检查是否有遗漏下载"
        #每一个订单数据进行对比
        flagid=''
        for k in range(0,len(lis)):
            try:
                if flagid!=lis[k][0]:
                    if lis[k][99]=='2605638400292508735':
                        print "api:"+str(lis[k][0])
                        id=lis[k][0]
                        params={"order_id":id }
                        publics={"method": "vdian.order.get","access_token": token,"version": "1.0","format": "json"}
                        payload={"param":json.dumps(params),"public":json.dumps(publics)}
                        apires=requests.post(apiurl,data=payload)
                        apidata=json.loads(apires.text)
                        print apidata

                        orcompary=ordercompare.ordercompary(lis,(k))

                        #付款时间
                        #提取页面时间戳
                        apitime=apidata[u'result']["pay_time"].strip()
                        orcompary.pay_times(apitime)


                        #卖家备注
                        apisalenote=apidata[u'result']["express_note"].strip()
                        orcompary.sale_note(str(apisalenote))


                        #买家备留言
                        apibuynote=apidata[u'result']["note"]
                        orcompary.buyer_note(apibuynote)


                        #订单金额
                        apimoney=apidata[u'result']["price"]
                        orcompary.money_fee(apimoney)

                        #订单优惠金额
                        disam=float(apidata[u'result']["discount_amount"])
                        totalor=float(apidata[u'result']["original_total_price"])
                        apidis=disam+totalor-float(apimoney)
                        apidis=str("%.2f"%apidis)
                        orcompary.dis_money(apidis)

                        #金额
                        apiordermoney=apimoney
                        apiordermoney=str("%.2f"%apiordermoney)
                        orcompary.order_money(apiordermoney)


                        #省份
                        apiprovince=apidata[u'result']["buyer_info"]["province"]+str("省")
                        orcompary.province(apiprovince)


                        #物流公司
                        if apidata[u'result']['express']==None:
                            apiexpress='null'
                        else:
                            apiexpress=str(apidata[u'result']['express']).strip()
                        orcompary.express_company(apiexpress)


                        #物流单号
                        if apidata[u'result']['express_no']==None:
                            apino=''
                        else:
                            apino=apidata[u'result']['express_no']
                        orcompary.express_no(apino)


                        #网店名称
                        apisalername=apidata[u'result']['seller_name']
                        orcompary.shopname(apisalername)



                        #退款状态为正常
                        restatus=apidata[u'result']['refund_info']['refund_time']
                        if restatus==None:
                            refund='0'
                        else:
                            refund=restatus
                        orcompary.refund_status(refund)



                        #交易状态
                        trstatus=apidata[u'result'][u'status']
                        if trstatus=='unpay':
                            status='1'
                        elif trstatus=='pay':
                            status='2'
                        elif trstatus=='ship':
                            status='3'
                        elif trstatus=='close':
                            status='5'
                        elif trstatus=='finish':
                            status='4'
                        else:
                            print trstatus
                            status=trstatus
                        orcompary.trade_status(status)

                        #买家运费
                        if apidata[u'result']['express_fee']!=0:
                            apifee=str(apidata[u'result']['express_fee'])
                            apifee=float(apifee)
                            apifee=str("%.2f"%apifee)
                        else:
                            apifee='0.00'
                        orcompary.post_fee(apifee)


                        #收货地址
                        adds=apidata[u'result']['buyer_info']['address'].replace(' ','省')
                        orcompary.address(adds)


                        #交易类型
                        typetrade=apidata['result']['order_type']
                        if typetrade=='1':
                            trtype='3'
                        elif typetrade=='2' or typetrade=='3':
                            trtype='0'
                        else:
                            print typetrade
                            trtype=typetrade
                        orcompary.trade_type(trtype)

                        #订单明细
                        detailnum=len(len(apidata["result"]["items"]))
                        for n in range(0,detailnum):
                            print "api:"+apidata["result"]["items"][n]["item_name"]
                            print "erp:"+lis[k+n+1][28]
                            #线上宝贝名称
                            apiitemname=apidata["result"]["items"][n]["item_name"]
                            orcompary.item_name(apiitemname,n+1)

                            #线上销售属性
                            apiitemtype=apidata["result"]["items"][0]["sku_title"]
                            if apiitemtype==None:
                                apiitemtype=''
                            orcompary.item_type(apiitemtype,n+1)

                            #线上商家编码
                            apiitemcode=apidata["result"]["items"][n]['sku_merchant_code']
                            orcompary.item_salecode(apiitemcode,n+1)

                            #商品数量
                            itemsnum=apidata["result"]["items"][n]["quantity"]
                            orcompary.item_num(int(itemsnum),n+1)

                            #订单金额
                            orderprice=float(apidata["result"]["items"][n]["total_price"])
                            orderprice=str("%.2f"%orderprice)

                            orcompary.order_price(orderprice,n+1)

                            #金额
                            orcompary.order_moneydetail(orderprice,n+1)

                            #单价
                            sigle=float(orderprice)/float(itemsnum)
                            sigle=str("%.2f"%sigle)
                            orcompary.item_order(sigle)

                            #优惠
                            itdis=float(apidata["result"]["items"][n]["price"])*int(itemsnum)-float(apidata["result"]["items"][n]["total_price"])
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