#*-* coding:UTF-8 *-*
from common import base

import unittest
import re
import requests
import json
import time
import datetime


import sys
reload(sys)
sys.setdefaultencoding('utf8')

basec=base.baseCommon()


class itemsyouzanTest(unittest.TestCase):


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
        print u"有赞商品接口测试完成"
        time.sleep(2)
        pass


    def testitemsYouzan(self):
        u'''有赞...将商品数据和页面数据进行对比'''
        #获取商品页面数据并放入列表

        module=".//*[@id='$80d499b2$ManagerMenuBar3']/div"
        modulename=".//*[@id='$80d499b2$ManagerMenuBar3_2']/td[3]"
        shop=".//*[@id='$19b126ff$treeEShopClass']/div/table[2]/tbody/tr/td[2]/div"
        basec.findXpath(self.driver,module).click()
        basec.findXpath(self.driver,modulename).click()
        basec.findXpath(self.driver,shop).click()


        url="http://beefun.wsgjp.com.cn/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerData"
        headers={'Content-Type': 'application/json; charset=gb2312','cookie':self.cookiestr,}
        payload={"pagerId":"$19b126ff$gridPType_pager1","queryParams":{"eshopId":"869326195688954","ismall":False,"classTypeId":"","platFullname":"","RelationStatus":0,"StockStatus":3,"isShowZeroQty":False,"notShowZeroQty":False,"isRepeatXcode":False,"isGiftSku":False,"isDifrentXcoe":False,"isDifrentSkuXcode":False},"orders":None,"filter":None,"first":0,"count":20}


        #去页面数据,并放入列表

        data=json.dumps(payload)
        res=basec.postRead(self.driver,url,data,headers)
        '''
        f=open(r"D:\api\renrenitemserp.txt",'w')
        f.write(res)
        f.close()
        f=open(r"D:\api\renrenitemserp.txt",'r')
        res=f.read()
        itemsno=re.findall("itemCount\":(.*?)}",res)
        itemexist=int(itemsno[0])
        print "itemscount:"+str(itemexist)

        before=re.findall("row(.*)itemCount",res)
        itemlist=re.findall("\[\"(.*?)-1\],",before[0])
        '''
        itemlist=basec.erpItems(res)
        print len(itemlist)
        itemCount=re.findall("itemCount\":(.*?)\}",res)
        count=int(itemCount[0])

        #页面中每一行商品，并取接口数据进行比较
        nowid=""
        flag=0
        for data in itemlist:
            itemlis=re.compile("\"")
            resault=itemlis.sub('',data)
            iresault=re.findall(":(.*?),",resault)
            id=iresault[11]

            #print itemlist

            #取接口数据
            if id!=nowid:
                now=datetime.datetime.now()
                nowtime=now.strftime("%Y-%m-%d %H:%M:%S")
                print nowtime

                apiurl="https://open.koudaitong.com/api/oauthentry/"
                sql="SELECT token FROM eshop WHERE shopAccount='15608199188'"
                token=basec.gettoken(sql)
                payloads={"access_token":token,"method":"kdt.item.get","num_iid":id}
                apires=requests.post(apiurl,data=payloads)
                #print apires.text
                apidata=json.loads(apires.text)

                #print apidata
                #是否有sku
                print "开始比较..........................."
                print "商品编号为："+str(id)
                print iresault[12]
                sku=len(apidata["response"]["item"]["skus"])
                print "sku:"+str(sku)
                #页面和接口数据进行比较
                if sku>0:
                    #有SKU
                    #名字
                    try:
                        #print iresault[12].decode("gbk")
                        #print chardet.detect(iresault[12])
                        #print chardet.detect(str(apidata['data']['title']))
                        #print chardet.detect(str(iresault[12]))
                        name=iresault[12]

                        self.assertEqual(apidata["response"]["item"]["title"], name,msg="SKU商品名字不一致")
                        print "assert title ok"
                    except AssertionError,msg:
                        print msg
                        print iresault[12]
                        print str(apidata["response"]["item"]["title"])
                        print name
                        #print "\n"
                    #总数量
                    try:
                        b=iresault[10]
                        #print "b:"
                        #print b
                        m=re.findall("(.*?)\.",b)
                        #print "m:"+str(m[0])
                        n=0
                        self.assertEqual(str(apidata["response"]["item"]["num"]), str(m[0]),msg="SKU商品库存不一致")
                        #print "n:"+str(n)
                        print "assert num ok"
                    except AssertionError,msg:
                        print msg
                        print iresault[12]
                        print str(apidata["response"]["item"]["num"])
                        print str(m[0])

                    #大类型号，微店没有
                    try:
                        self.assertEqual(apidata["response"]["item"]["outer_id"], str(iresault[14]),msg="商品sku大类型号不一致")
                        print "assert total sku ok"
                    except AssertionError,msg:
                        print msg
                        print iresault[12]
                        print apidata["response"]["item"]["outer_id"]
                        print str(iresault[14])

                    #具体各个型号商品
                    #型号

                    for num in range(0,sku):
                        print "sku具体信息"
                        print num+1
                        itemlis=re.compile("\"")
                        resault=itemlis.sub('',itemlist[flag+num+1])
                        iresault=re.findall(":(.*?),",resault)
                        shap=iresault[12]
                        #print shap
                        try:
                            aa=json.loads(apidata["response"]["item"]["skus"][num]["properties_name_json"])
                            numbers=len(aa)
                            skuname=''
                            for vv in range (numbers):
                                f=aa[vv]['v']
                                skuname=skuname+f+"_"
                            skuname=skuname[:-1]
                            self.assertEqual(skuname, shap,msg="sku具体商品型号不一致")
                            #print str(apidata['result']['skus'][num]['title'])
                            print "assert title ok"

                        except AssertionError,msg:
                            print msg
                            print iresault[12]
                            print skuname

                        #编号
                        try:
                            self.assertEqual(apidata["response"]["item"]["skus"][num]["outer_id"], iresault[9],msg="sku具体商品编号不一致")
                            #print str(apidata['result']['skus'][num]['sku_merchant_code'])
                            print "assert sku_merchant_code ok"

                        except AssertionError,msg:
                            print msg
                            print iresault[12]
                            print str(apidata["response"]["item"]["skus"][num]["outer_id"])
                            print iresault[9]
                        #库存
                        try:
                            b1=iresault[10]
                            #print b
                            m1=re.findall("(.*?)\.",b1)
                            #print m[0]
                            self.assertEqual(str(apidata["response"]["item"]["skus"][num]["quantity"]), str(m1[0]),msg="sku具体商品库存不一致")
                            #print str(apidata['result']['skus'][num]['stock'])
                            print "assert stock ok"
                        except AssertionError,msg:
                            print msg
                            print iresault[12]
                            print apidata["response"]["item"]["skus"][num]["quantity"]
                            print m1[0]

                elif sku==0:
                    #无sku
                    #商品名字
                    try:
                        name=iresault[12]
                        self.assertEqual(apidata["response"]["item"]["title"],name ,msg="商品名字不一致")
                        print "assert no sku title ok"
                    except AssertionError,msg:
                        print msg
                        print iresault[12]
                        print str(apidata["response"]["item"]["title"])
                        print name


                    #商品编号
                    try:
                        self.assertEqual(apidata["response"]["item"]["outer_id"],iresault[14],msg="商品编号不一致")
                        print "assert no sku goods_sn ok"
                    except AssertionError,msg:
                        print msg
                        print iresault[12]
                        print apidata["response"]["item"]["outer_id"]
                        print iresault[14]

                    #商品库存
                    try:
                        b=iresault[10]
                        #print b
                        m=re.findall("(.*?)\.",b)
                        #print m[0]
                        self.assertEqual(str(apidata["response"]["item"]["num"]), str(m[0]),msg="商品库存不一致")
                        print "assert no sku stock ok"
                    except AssertionError,msg:
                        print msg
                        print iresault[12]
                        print apidata["response"]["item"]["num"]
                        print m[0]
                else:
                    print u"接口SKU标志返回错误，请查看文档"
                    print "标志为："+str(apidata["response"]["item"]["skus"])
            nowid=id
            flag=flag+1

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testAccredit']
    unittest.main()