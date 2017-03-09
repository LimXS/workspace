#*-* coding:UTF-8 *-*
from common import base
import unittest
import traceback
import re
import requests
import json
import time
import gettokenmeng
basec=base.baseCommon()

class itemsmengTest(unittest.TestCase):


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
        print u"萌店商品接口测试完成"
        pass


    def testitemsMeng(self):
        u'''萌店...将商品数据和页面数据进行对比'''
        #获取商品页面数据并放入列表
        '''
        alert=self.driver.switch_to_alert()
        alert.accept()
        '''
        module="//*[@id='$80d499b2$ManagerMenuBar3']/div"
        modulename=".//*[@id='$80d499b2$ManagerMenuBar3_2']/td[3]"
        shop=".//*[@id='$19b126ff$treeEShopClass']/div/table[3]/tbody/tr/td[2]/div"
        basec.findXpath(self.driver,module).click()
        basec.findXpath(self.driver,modulename).click()
        basec.findXpath(self.driver,shop).click()

        #取接口所有商品
        is_onsale=2
        page_no=10
        page_size=20
        s={"is_onsale":2,"page_no":1, "page_size":20, "include_description": True}
        payload={"is_onsale":2,"page_no":1,"page_size":20}
        #token="5c2afaf22ec26df59b5ec9aa996514d9d72b5eeec18741185aa08890a678a84db1aafd4963886a8cff70d45867cce1974ef7380d37d2c714da178cbec505be90"
        '''
        f=open(r'D:\api\mengtoken.txt','r')
        token=f.read()
        f.close()
        '''
        token=gettokenmeng.getmengToken()
        print "token:"+token
        url="https://open.mengdian.com/api/mname/WE_MALL/cname/spuFullInfoGet?accesstoken="+token
        apires=requests.post(url,data=json.dumps(payload))
        print apires.text
        apidata=json.loads(apires.text)
        #apiitemsnum=len(apidata['data']['page_data'])
        apinum=len(apidata['data']['page_data'])
        #print apidata["data"]
        print "apinum:"+str(apinum)

        #去页面数据,并放入列表
        url2="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerData"
        headers={'Content-Type': 'application/json; charset=gb2312','cookie':self.cookiestr,}
        payload2={"pagerId":"$19b126ff$gridPType_pager1","queryParams":{"eshopId":"2605638451560822494","ismall":False,"classTypeId":"","platFullname":"","RelationStatus":0,"StockStatus":3,"isShowZeroQty":False,"notShowZeroQty":False,"isRepeatXcode":False,"isGiftSku":False,"isDifrentXcoe":False,"isDifrentSkuXcode":False},"orders":None,"filter":None,"first":0,"count":20}

        data=json.dumps(payload2)
        res=basec.postRead(self.driver,url2,data,headers)
        itemlist=basec.erpItems(res)
        print len(itemlist)

        #页面中每一行商品，并取接口数据进行比较

        itemCount=re.findall("itemCount\":(.*?)\}",res)
        count=int(itemCount[0])
        flagid=""
        #apiflag=-1
        erpflag=0
        flag=0
        print apidata['data']
        print "开始比较..................................."
        for data in itemlist:
            itemlis=re.compile("\"")
            resault=itemlis.sub('',data)
            iresault=re.findall(":(.*?),",resault)
            id=iresault[11]
            print iresault[12]
            if id!=flagid:
                #apiflag=apiflag+1
                flagid=id
                #print itemlist


                #判断是否有sku
                #页面和接口数据进行比较
                # print "type"
                #print type (apidata['data'])
                for apiflag in range(0,apinum):
                    if id==str(apidata['data']['page_data'][apiflag]['spu']['spu_id']):
                        break
                print "id:"+str(id)
                print "apiflag:"+str(apiflag)
                sku=len(apidata['data']['page_data'][apiflag]['skus'])
                print sku

                if sku>1:
                    #有SKU

                    if str(id)==str(apidata['data']['page_data'][apiflag]['spu']['spu_id']):
                        print "erpid:"+str(id)
                        print "apiid:"+str(apidata['data']['page_data'][apiflag]['spu']['spu_id'])
                        #名字
                        try:
                            self.assertEqual(apidata['data']['page_data'][apiflag]['spu']['spu_name'], iresault[12],msg="商品SKU名字不一致")
                            print "assert item_name ok"
                        except AssertionError,msg:
                            print msg
                            print str(apidata['data']['page_data'][apiflag]['spu']['spu_name'])
                            print str(iresault[12])
                            #print "apiflag:"+str(apiflag)
                            print "\n"
                            #总数量
                        try:
                            b=iresault[10]
                            #print "b:"
                            #print b
                            m=re.findall("(.*?)\.",b)
                            #print "m:"+str(m[0])

                            self.assertEqual(str(apidata['data']['page_data'][apiflag]['spu']['inventory']), str(m[0]),msg="商品SKU库存不一致")
                            #print "n:"+str(n)
                            print "assert stock ok"
                        except AssertionError,msg:
                            print msg
                            print str(apidata['data']['page_data'][apiflag]['spu']['inventory'])
                            print str(m[0])
                        #大类型号
                        try:
                            self.assertEqual(apidata['data']['page_data'][apiflag]['spu']['spu_code'], str(iresault[14]),msg="商品SKU大类型号不一致")
                            print "assert spu_code ok"
                        except AssertionError,msg:
                            print msg
                            print str(apidata['data']['page_data'][apiflag]['spu']['spu_code'])
                            print str(iresault[9])
                        #具体各个型号商品


                        for num in range(0,sku):
                            flag=flag+1
                            iresault=basec.erpmengpageItems(itemlist[flag])
                            print "items list:"+str(flag)
                            #型号
                            try:
                                self.assertEqual(apidata['data']['page_data'][apiflag]['skus'][num]['sku_attrs']['skuval'][0]["val"], iresault[12],msg="sku商品型号不一致")
                                #print str(apidata['result']['skus'][num]['title'])
                                print "assert title ok"

                            except AssertionError,msg:
                                print msg
                                print str(apidata['data']['page_data'][apiflag]['skus'][num]['sku_attrs']['skuval'][0]["val"])
                                print iresault[12]
                            #编号
                            try:
                                self.assertEqual(apidata['data']['page_data'][apiflag]['skus'][num]['sku_code'], iresault[14],msg="sku商品编号不一致")
                                #print str(apidata['data']['page_data'][2]['skus'][0]['sku_code'])
                                print "assert sku_merchant_code ok"

                            except AssertionError,msg:
                                print msg
                                print str(apidata['data']['page_data'][apiflag]['skus'][num]['sku_code'])
                                print iresault[14]
                            #库存
                            try:
                                b1=iresault[10]
                                #print b
                                m1=re.findall("(.*?)\.",b1)
                                #print m[0]
                                self.assertEqual(str(apidata['data']['page_data'][apiflag]['skus'][num]['inventory']), str(m1[0]),msg="sku商品库存不一致")
                                #print str(apidata['result']['skus'][num]['stock'])
                                print "assert stock ok"
                            except AssertionError,msg:
                                print msg
                                print str(apidata['data']['page_data'][apiflag]['skus'][num]['inventory'])
                                print m1[0]

                else:
                    #无sku

                    if str(id)==str(apidata['data']['page_data'][apiflag]['spu']['spu_id']):
                        print "erpid:"+str(id)
                        print "apiid:"+str(apidata['data']['page_data'][apiflag]['spu']['spu_id'])
                        #商品名字
                        try:
                            self.assertEqual(apidata['data']['page_data'][apiflag]['skus'][0]['sku_name'], iresault[12],msg="此商品无SKU，商品名字不一致")
                            print "assert no sku item_name ok"
                        except AssertionError,msg:
                            print msg
                            print str(apidata['data']['page_data'][apiflag]['skus'][0]['sku_name'])
                            print iresault[12]


                        #商品编号
                        try:
                            self.assertEqual(apidata['data']['page_data'][apiflag]['skus'][0]['sku_code'], iresault[14],msg="此商品无SKU，商品编号不一致")
                            print "assert no sku merchant_code ok"
                        except AssertionError,msg:
                            print msg
                            print str(apidata['data']['page_data'][apiflag]['skus'][0]['sku_code'])
                            print iresault[14]

                        #商品库存
                        try:
                            c=iresault[10]
                            #print b
                            m=re.findall("(.*?)\.",c)
                            #print m[0]
                            self.assertEqual(str(apidata['data']['page_data'][apiflag]['skus'][0]['inventory']), str(m[0]),msg="此商品无SKU，商品库存不一致")
                            print "assert no sku stock ok"
                        except AssertionError,msg:
                            print msg
                            print str(apidata['data']['page_data'][apiflag]['skus'][0]['inventory'])
                            print str(m[0])
                flag=flag+1
                #print "after flag"+str(flag)
                if flag-1>len(itemlist):
                    print "商品下载遗漏sku明细"
                if apinum>count:
                    print "商品下载遗漏，商品大类"
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testAccredit']
    unittest.main()