#*-* coding:UTF-8 *-*
import unittest
import traceback
import re
import requests
import json
import time
import sys
reload(sys)

sys.setdefaultencoding( "utf-8" )
from common import base
from common import ordercompare
import gettokenmeng
basec=base.baseCommon()

class orderMengTest(unittest.TestCase):


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
        print u"微店订单接口测试完成"
        pass


    def testorderMeng(self):
        u'''萌店...将接口数据和页面数据进行对比'''
        #获取订单页面数据并放入列表

        aa='http://beefun.wsgjp.com/EShopDeliver/EShopDeliverList.gspx?caption=%B6%A9%B5%A5%B4%A6%C0%ED&tag=SimpleProcessStatus'
        headers = {'cookie':self.cookiestr,'Content-Type': 'application/json'}

        #取页面数据
        b=basec.handleorderRead(self.driver,aa, headers)
        lis=basec.erpOrder(b)

        #取接口数据并进行比对
        flag=0
        '''
        f=open('D:\api\mengtoken.txt','r')
        token=f.read()
        '''
        token=gettokenmeng.getmengToken()
        print "token:"+token
        apiurl=apiurl='https://open.mengdian.com/api/mname/WE_MALL/cname/orderFullInfoGetHighly?accesstoken='+token


        '''
        #判断订单是否有遗漏下载
        timelist=basec.getTime()
        start=timelist[1]
        end=timelist[0]
        apiurl2='https://open.mengdian.com/api/mname/WE_MALL/cname/orderGetHighly?accesstoken='+token
        #payload2={"order_status":None,"pay_status":None,"delivery_status":None,"page_size":20,"page_no":1,"create_begin_time":start,"create_end_time":end}
        payload2={"order_status":None,"pay_status":None,"delivery_status":None,"page_size":20,"page_no":1}
        apires2=requests.post(apiurl2,data=json.dumps(payload2))
        print apires2.text
        apidata2=json.loads(apires2.text)
        print apidata2["data"]["row_count"]
        ordercount=apidata2["data"]["row_count"]
        if total!=str(len(lis)):
            print "接口返回的订单数目和页面显示的订单数目不一致，请检查是否有遗漏下载"
        '''
        flagid=''
        #每一个订单数据进行对比
        for k in range(0,len(lis)):
            try:
                if flagid!=lis[k][0]:
                    if lis[k][99]=='2605638451560822494':
                        print "api:"+str(lis[k][0])
                        id=lis[k][0]
                        print id
                        payload={"order_no":id}
                        apires=requests.post(apiurl,data=json.dumps(payload))
                        apidata=json.loads(apires.text)
                        print apidata
                        #print apidata['code']['errmsg']

                        orcompary=ordercompare.ordercompary(lis,(k))

                        #付款时间
                        #提取页面时间戳
                        orcompary.pay_times(apidata["data"]["pay_time"].strip())
                        '''
                    #卖家备注，萌店无卖家备注
                    if apidata[u'result']["express_note"].strip()!=lis[flag-1][6].strip():
                        print u"订单编号："+lis[flag-1][0]
                        print u"接口返回卖家备注express_note："+str(apidata[u'result']["express_note"][7])
                        print u"页面卖家备注："+lis[flag-1][6]+"\n"
                    '''
                        #买家备留言
                        apibuynote=apidata["data"]["remark"]
                        orcompary.buyer_note(apibuynote)

                        #订单金额
                        apimoney=apidata["data"]["order_details"][0]["price"]
                        if apimoney!=0:
                            apimoney=str(apimoney*0.01)
                            apimoney=float(apimoney)
                            apimoney=str("%.2f"%apimoney)
                        else:
                            apimoney='0.00'
                        orcompary.money_fee(apimoney)

                        '''
                    #暂时未处理，不知道如何处理优惠金额的
                    #订单优惠金额
                    mona=apidata[u'result']['items'][0]
                    print mona

                    mon=re.findall("price\':(.*?),",str(mona))
                    a1=mon[0].strip()
                    a2=mon[1].strip()

                    cc=eval(eval(a1))-eval(eval(a2))
                    apidis=float(cc)
                    apidisw=str("%.2f"%apidis)
                    #print apidisw
                    dis=float(lis[flag-1][18])
                    disw=str("%.2f"%dis)
                    if str(disw)!=str(apidisw):
                        print u"订单号为："+lis[flag-1][0]
                        print u"订单页面查询的优惠金额："+str(disw)
                        print u"api接口返回的数据 ："+str(apidisw)+"\n"

                    #金额
                    mytotal=float(lis[flag-1][19])
                    total=str("%.2f"%mytotal)
                    com=dis+money
                    comtr=str("%.2f"%com)
                    if total!=comtr:
                        print u"订单号为："+lis[flag-1][0]
                        print u"订单页面优惠金额："+str(dis)
                        print u"订单页面订单金额 ："+str(moneyw)
                        print u"订单页面金娥："+str(comtr)+"\n"
                    '''
                        #省份
                        apiprovince=apidata["data"]["receiver_region"]["province"]
                        orcompary.province(apiprovince)

                        #物流公司
                        try:
                            apiexpress=apidata["data"]["carrier_name"]
                            company=1
                        except:
                            company=0
                        if company==0:
                            apiexpress='null'


                        if company==1:
                            apiexpress=apidata["data"]["carrier_name"]
                        orcompary.express_company(apiexpress)

                        #物流单号
                        try:
                            apino=apidata["data"]["express_no"]
                            exprno=1
                        except:
                            exprno=0
                        if exprno==0:
                            apino=''

                        if exprno==1:
                            apino=apidata["data"]["express_no"]
                        orcompary.express_no(apino)


                        #网店名称
                        #接口获取店铺信息
                        apiurl3='https://open.mengdian.com/api/mname/WE_MALL/cname/shopGet?accesstoken='+token
                        payload3={"include_intro":False}
                        apires3=requests.post(apiurl3,data=json.dumps(payload3))
                        apidata3=json.loads(apires3.text)
                        apisalername=apidata3['data']['shop_name']
                        orcompary.shopname(apisalername)

                        #退款状态
                        return_id=str(apidata["data"]["order_details"][0]["return_id"])
                        return_qty=str(apidata["data"]["order_details"][0]["return_qty"])
                        return_type=str(apidata["data"]["order_details"][0]["return_type"])
                        return_status=str(apidata["data"]["order_details"][0]["return_status"])
                        if return_status==None:
                            refund='0'
                        elif return_status==1 or return_status==2 or return_status==3 or return_status==4 or return_status==5 or return_status==6:
                            refund='1'
                        elif return_status==8 or return_status==9:
                            refund='3'
                        else:
                            print return_status
                            refund=return_status
                        orcompary.refund_status(refund)


                        #交易状态
                        trstatus=apidata["data"]["order_status"]
                        shipstatus=apidata['result']['data']['delivery_time']
                        pay_status=apidata['result']['data']['pay_status']
                        if trstatus==3:
                            status='5'
                        elif trstatus==2:
                            status='4'
                        elif trstatus==1 :
                            if shipstatus!='' and pay_status==1:
                                status='3'
                            if shipstatus=='' and pay_status==1:
                                status='2'
                            if shipstatus=='' and pay_status==0:
                                status='1'
                        else:
                            status=apidata["data"]["order_status"]
                            print shipstatus
                            print pay_status
                        orcompary.trade_status(status)



                        #买家运费
                        if apidata["data"]["delivery_amount"]!=0:
                            apifee=str(apidata['result']['data']['ship_expense']*0.01)
                            apifee=float(apifee)
                            apifee=str("%.2f"%apifee)
                        else:
                            apifee='0.00'
                        orcompary.post_fee(apifee)

                        #收货地址
                        pro=apidata["data"]["receiver_region"]["province"].strip()
                        city=apidata["data"]["receiver_region"]["city"].strip()
                        district=apidata["data"]["receiver_region"]["district"].strip()
                        add=apidata["data"]["receiver_region"]["address"].strip()
                        adds=pro+city+district+add
                        orcompary.address(adds)

                        '''
                    #暂时未处理，不知道字段对应关系
                    #交易类型
                    if lis[flag-1][69].strip(' ')=='3' and apidata[u'result']["order_type_des"].strip(' ')!=u"货到付款":
                        print u"订单号为："+lis[flag-1][0]
                        print u"订单页面交易类型："+lis[flag-1][69]
                        print u"api接口返回的数据order_type_des："+str(apidata[u'result']["order_type_des"])
                        print u"接口和页面数据不同\n"

                    if  (apidata[u'result']["order_type_des"].strip(' ')==u"担保交易" or apidata[u'result']["order_type_des"].strip(' ')==u"直接交易" ) and lis[flag-1][69].strip(' ')!='0' :
                        print u"订单号为："+lis[flag-1][0]
                        print u"订单页面交易类型："+lis[flag-1][69]
                        print u"api接口返回的数据order_type_des："+str(apidata[u'result']["order_type_des"])
                        print u"接口和页面数据不同\n"

                    if lis[flag-1][69].strip(' ')!=('0'or '3'):
                        print u"订单号为："+lis[flag-1][0]
                        print u"订单页面交易类型："+lis[flag-1][69]
                        print u"api接口返回的数据order_type_des："+str(apidata[u'result']["order_type_des"])
                        print u"无此交易类型\n"
                    '''
                #flag=flag+1
                flagid=lis[k][0]
                #print "flag-------------------------------:"+str(flag)

            except:
                flagid=lis[k][0]
                print(u"订单数据比对失败")
                print(traceback.format_exc())




if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testAccredit']
    unittest.main()