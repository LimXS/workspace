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
import hashlib
reload(sys)
sys.setdefaultencoding( "utf-8" )

basec=base.baseCommon()

class orderrenrenTest(unittest.TestCase):


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
        print u"人人店订单接口测试完成"
        pass


    def testorderRenren(self):
        u'''人人店...将接口数据和页面数据进行对比'''
        #获取订单页面数据并放入列表

        aa='http://beefun.wsgjp.com/EShopDeliver/EShopDeliverList.gspx?caption=%B6%A9%B5%A5%B4%A6%C0%ED&tag=SimpleProcessStatus'
        headers = {'cookie':self.cookiestr,'Content-Type': 'application/json'}

        #取页面数据
        b=basec.handleorderRead(self.driver,aa, headers)
        lis=basec.erpOrder(b)
        print "lis....................."
        print lis[0]
        #print lis[1]
        #取接口数据并进行比对
        timelist=basec.getTime()
        start=timelist[1]
        end=timelist[0]
        flag=0
        #apiurl='http://api.vdian.com/api'
        '''
        f=open('E:\wei\sp.dat','r')
        token=f.read()
        '''
        now=datetime.datetime.now()
        nowtime=now.strftime("%Y-%m-%d %H:%M:%S")
        print nowtime

        apiurl="http://api04.weiba04.com/router/rest"

        appid="5b11e5f1b3763ba5"
        method="weiba.wxrrd.trade.details"
        timestamp=nowtime
        sql="SELECT token FROM eshop WHERE shopAccount='xmy666'"
        token=basec.gettokeneach(sql)
        access_token=token[2]
        access_token=access_token[0]
        print "token:"+access_token
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
        #店铺名称
        signbefore2="access_token="+access_token+"&appid=5b11e5f1b3763ba5&format=json&method=weiba.wxrrd.shop.details&timestamp="+nowtime
        m2 = hashlib.md5()
        m2.update(signbefore2)
        sign2= m2.hexdigest().upper()
        payload2={"appid":appid,"method":"weiba.wxrrd.shop.details","timestamp":nowtime,"access_token":access_token,"format":"json","sign":sign2}
        apires2=requests.post(apiurl,data=payload2)
        apidata2=json.loads(apires2.text)
        #print apidata2
        print apidata2["data"]["name"]

        #每一个订单数据进行对比
        flagid=''
        for k in range(0,len(lis)):
            try:
                if flagid!=lis[k][0]:
                    if lis[k][99]=='869277121746859':
                        print "api:"+str(lis[k][0])
                        id=lis[k][0]
                        signbefore="access_token="+access_token+"&appid=5b11e5f1b3763ba5&method=weiba.wxrrd.trade.details&order_sn="+id+"&timestamp="+nowtime
                        #print signbefore
                        m2 = hashlib.md5()
                        m2.update(signbefore)
                        sign= m2.hexdigest().upper()
                        print sign
                        payload={"appid":appid,"method":method,"timestamp":nowtime,"access_token":access_token,"sign":sign,"order_sn":id}
                        apires=requests.post(apiurl,data=payload)
                        print apires.text
                        apidata=json.loads(apires.text)
                        print apidata

                        orcompary=ordercompare.ordercompary(lis,(k))

                        #付款时间
                        apitime=apidata['data']['pay_at']
                        orcompary.pay_times(apitime)

                        #卖家备注
                        apisalenote=apidata['data']['remarks']
                        if apisalenote==None:
                            apisalenote=''
                        orcompary.sale_note(apisalenote)

                        #买家备留言
                        apibuynote=apidata["data"]["memo"]
                        orcompary.buyer_note(apibuynote)

                        #订单金额

                        '''
                        if len(apidata["data"]["order_goods"])>0:
                            nogoods=float(apidata["data"]["order_goods"][0]["pay_price"])
                        else:
                            nogoods=0

                        if len(apidata["data"]["package"])>0:
                            yesgood=float(apidata["data"]["package"][0]["order"][0]["pay_price"])
                        else:
                            yesgood=0

                        if str(apidata["data"]["parent_order_ump"]).strip()=='':
                            mint=0
                        else:
                            mint=float(apidata["data"]["parent_order_ump"])
                        '''
                        amount=apidata["data"]["goods_amount"]
                        amount=str("%.2f"%amount)
                        orcompary.money_fee(amount)



                        #订单优惠金额
                        #print type(apidata["data"]["parent_order_ump"].encode('utf-8'))
                        if len(apidata["data"]["order_goods"])>0:
                            apidis=float(apidata["data"]["goods_amount"])-float(apidata["data"]["order_goods"][0]["pay_price"])
                        else:
                            a2=float(apidata["data"]["coupon_amount"])
                            if len(apidata["data"]["parent_order_ump"])==0:
                                cc=0
                            else:
                                cc=abs(float(apidata["data"]["parent_order_ump"]))
                            apidis=float(a2+cc)
                        apidisw=str("%.2f"%apidis)
                        orcompary.dis_money(apidisw)


                        #金额
                        '''
                        if len(apidata["data"]["goods_amount"])>0:
                            comtr=str(apidata["data"]["goods_amount"])
                        else:
                            comtr='0.00'
                        '''
                        orcompary.order_money(amount)


                        #省份
                        apiprovince=apidata["data"]["province_name"]
                        orcompary.province(apiprovince)


                        #物流公司&物流单号
                        if len(apidata["data"]["package"])>0:
                            #物流公司
                            if str(apidata["data"]["package"][0]["logis_name"]).strip()=='':
                                apiexpress='null'
                            else:
                                apiexpress=str(apidata["data"]["package"][0]["logis_name"]).strip()
                            orcompary.express_company(apiexpress)

                            #物流单号

                            if str(apidata["data"]["package"][0]["logis_no"]).strip()=='':
                                apino=''
                            else:
                                apino=str(apidata["data"]["package"][0]["logis_no"]).strip()
                            orcompary.express_no(apino)

                        #网店名称
                        apisalername=apidata2["data"]["name"]
                        orcompary.shopname(apisalername)


                         #退款状态为正常
                        if len(apidata["data"]["package"])>0:
                            refund_status=apidata["data"]["package"][0]["order"][0]["refund_status"]
                        else:
                            refund_status=0

                        if refund_status==0:
                            restatus='0'
                        elif refund_status==10 and refund_status==11 and refund_status==20 and refund_status==22 and refund_status==30:
                            restatus='1'
                        elif refund_status==31:
                            restatus=='2'
                        elif refund_status==40 or refund_status==41 or refund_status==21 :
                            restatus=='3'
                        else:
                            restatus=refund_status
                        orcompary.refund_status(restatus)



                         #交易状态
                        trstatus=apidata["data"]["status"]
                        if trstatus==10 or trstatus==11 or trstatus==12 or trstatus==13:
                            status='5'
                        elif trstatus==50:
                            status='4'
                        elif trstatus==19 or trstatus==20:
                            status='1'
                        elif trstatus==30 or trstatus==31 or trstatus==32:
                            status='2'
                        elif trstatus==40:
                            status='3'
                        else:
                            status=trstatus
                            print trstatus
                        orcompary.trade_status(status)


                        #买家运费
                        if apidata["data"]["shipment_fee"]!=0:
                            apifee=apidata["data"]["shipment_fee"]
                            apifee=float(apifee)
                            apifee=str("%.2f"%apifee)
                        else:
                            apifee='0.00'
                        orcompary.post_fee(apifee)

                        #收货地址

                        pro=apidata["data"]["province_name"].strip()
                        city=apidata["data"]["city_name"].strip()
                        district=apidata["data"]["district_name"].strip()
                        add=apidata["data"]["address"].strip()
                        adds=pro+city+district+add
                        orcompary.address(adds)

                        #交易类型
                        trtype=apidata["data"]["payment_name"]
                        if trtype==u"货到付款":
                            ttype='3'
                        elif trtype==None:
                            ttype='0'
                        else:
                            ttype=trtype
                            print trtype
                        orcompary.trade_type(ttype)

                        #订单明细
                        #已发货
                        if len(apidata["data"]["package"])>0:

                            for a in range(len[apidata["data"]["package"]]):
                                ordet=apidata["data"]["package"][n]
                                for n in range(len(ordet)):
                                    print "api:"+ordet[n]["goods_name"]
                                    print "erp:"+lis[k+n+1][28]
                                    #线上宝贝名称
                                    apiitemname=ordet[n]["goods_name"]
                                    orcompary.item_name(apiitemname,n+1)

                                    #线上销售属性
                                    apiitemtype=ordet[n]["props"]
                                    apiitemtype=apiitemtype.replace(':',"_")
                                    orcompary.item_type(apiitemtype,n+1)

                                    #线上商家编码
                                    apiitemcode=ordet[n]["product_sn"]
                                    orcompary.item_salecode(apiitemcode,n+1)

                                    #商品数量
                                    itemsnum=ordet[n]["quantity"]
                                    orcompary.item_num(itemsnum,n+1)

                                    #订单金额
                                    orderprice=ordet[n]["pay_price"]
                                    orcompary.order_price(orderprice,n+1)

                                    #金额
                                    orcompary.order_moneydetail(orderprice,n+1)

                                    #单价
                                    sigle=float(orderprice)/float(itemsnum)
                                    sigle=str("%.2f"%sigle)
                                    orcompary.item_order(sigle)

                                    #优惠
                                    itdis=float(ordet[n]["price"])*int(itemsnum)-float(ordet[n]["pay_price"])
                                    itdis=str("%.2f"%itdis)
                                    orcompary.item_dis(itdis)

                        #未发货
                        if len(apidata["data"]["order_goods"])>0:
                            for n in range(len(apidata["data"]["order_goods"])):
                                print "api:"+apidata["data"]["order_goods"][n]["goods_name"]
                                print "erp:"+lis[k+n+1][28]
                                #线上宝贝名称
                                apiitemname=apidata["data"]["order_goods"][n]["goods_name"]
                                orcompary.item_name(apiitemname,n+1)

                                #线上销售属性
                                apiitemtype=apidata["data"]["order_goods"][n]["props"]
                                apiitemtype=apiitemtype.replace(':',"_")
                                orcompary.item_type(apiitemtype,n+1)

                                #线上商家编码
                                apiitemcode=apidata["data"]["order_goods"][n]["product_sn"]
                                orcompary.item_salecode(apiitemcode,n+1)

                                #商品数量
                                itemsnum=apidata["data"]["order_goods"][n]["quantity"]
                                orcompary.item_num(int(itemsnum),n+1)

                                #订单金额
                                orderprice=apidata["data"]["order_goods"][n]["pay_price"]
                                orcompary.order_price(orderprice,n+1)

                                #金额
                                orcompary.order_moneydetail(orderprice,n+1)

                                #单价
                                sigle=float(orderprice)/float(itemsnum)
                                sigle=str("%.2f"%sigle)
                                orcompary.item_order(sigle)

                                #优惠
                                itdis=float(apidata["data"]["order_goods"][n]["price"])*int(itemsnum)-float(apidata["data"]["order_goods"][n]["pay_price"])
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
    #import sys;sys.argv = ['', '']
    unittest.main()