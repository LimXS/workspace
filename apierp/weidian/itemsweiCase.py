#*-* coding:UTF-8 *-*
from common import base
from common import itemscompare
import unittest
import traceback
import re
import requests
import json
import time
basec=base.baseCommon()

class itemsweiTest(unittest.TestCase):


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
        print u"微店商品接口测试完成"
        pass


    def testitemsWei(self):
        u'''微店...将商品数据和页面数据进行对比'''
        #获取商品页面数据并放入列表

        module=".//*[@id='$80d499b2$ManagerMenuBar3']/div"
        modulename=".//*[@id='$80d499b2$ManagerMenuBar3_2']/td[3]"
        shop=".//*[@id='$19b126ff$treeEShopClass']/div/table[2]/tbody/tr/td[2]/div"
        basec.findXpath(self.driver,module).click()
        basec.findXpath(self.driver,modulename).click()
        basec.findXpath(self.driver,shop).click()


        url="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerData"
        headers={'Content-Type': 'application/json; charset=gb2312','cookie':self.cookiestr,}
        payload={"pagerId":"$19b126ff$gridPType_pager1","queryParams":{"eshopId":"2605638400292508735","ismall":False,"classTypeId":"","platFullname":"","RelationStatus":0,"StockStatus":3,"isShowZeroQty":False,"notShowZeroQty":False,"isRepeatXcode":False,"isGiftSku":False,"isDifrentXcoe":False,"isDifrentSkuXcode":False},"orders":None,"filter":None,"first":0,"count":20}


        #去页面数据,并放入列表

        data=json.dumps(payload)
        res=basec.postRead(self.driver,url,data,headers)
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
            print iresault[12]
            '''
            print "iresault....................."
            print iresault
            '''


            itcompare=itemscompare.commonitemscompary(iresault)
            #print itemlist

            #取接口数据
            if id!=nowid:
                f=open(r"C:\workspace\apierp\sp.dat","r")
                token=f.read()
                #print "token:"+token


                params={"itemid":id}
                publics={"method":"vdian.item.get","access_token":token,"version":"1.0","format":"json"}

                payload={"param":json.dumps(params),"public":json.dumps(publics)}
                url="http://api.vdian.com/api"
                apires=requests.post(url,data=payload)
                apidata=json.loads(apires.text)
                '''
                print "api........................."
                print apidata
               '''
                print "开始比较..........................."
                print "商品编号为："+str(id)
                print iresault[12]
                #是否有sku
                sku=apidata['result']['skus']
                print "sku:"+str(len(sku))
                #页面和接口数据进行比较
                if len(sku)>0:
                    #有SKU
                    #名字
                    apiname=apidata['result']['item_name']
                    itcompare.item_name(apiname)
                    #总数量
                    try:
                        b=iresault[10]
                        #print "b:"
                        #print b
                        m=re.findall("(.*?)\.",b)
                        #print "m:"+str(m[0])
                        n=0
                        for i in range(0,len(sku)):
                            n=apidata['result']['skus'][i]['stock']+n
                        self.assertEqual(str(n), str(m[0]),msg="SKU商品库存不一致")
                        #print "n:"+str(n)
                        print "assert stock ok"
                    except AssertionError,msg:
                        print msg
                        print str(n)
                        print str(m[0])
                    '''
                 #大类型号，微店没有
                 try:
                     self.assertEqual(str(apidata['data']['page_data'][2]['inventory']), str(iresault[9]),msg="商品sku大类型号不一致")
                 except:
                    print msg
                    print str(apidata['data']['page_data'][2]['inventory)
                    print str(iresault[9])
                   '''
                    #具体各个型号商品
                    #型号

                    for num in range(0,len(sku)):
                        itemlis=re.compile("\"")
                        resault=itemlis.sub('',itemlist[flag+num+1])
                        iresault=re.findall(":(.*?),",resault)
                        try:
                            self.assertEqual(apidata['result']['skus'][num]['title'], iresault[12],msg="sku商品型号不一致")
                            #print str(apidata['result']['skus'][num]['title'])
                            print "assert title ok"

                        except AssertionError,msg:
                            print msg
                            print str(apidata['result']['skus'][num]['title'])
                            print iresault[12]
                        #编号
                        try:
                            self.assertEqual(apidata['result']['skus'][num]['sku_merchant_code'], iresault[9],msg="sku商品编号不一致")
                            #print str(apidata['result']['skus'][num]['sku_merchant_code'])
                            print "assert sku_merchant_code ok"

                        except AssertionError,msg:
                            print msg
                            print str(apidata['result']['skus'][num]['sku_merchant_code'])
                            print iresault[9]
                        #库存
                        try:
                            b1=iresault[10]
                            #print b
                            m1=re.findall("(.*?)\.",b1)
                            #print m[0]
                            self.assertEqual(str(apidata['result']['skus'][num]['stock']), str(m1[0]),msg="sku商品库存不一致")
                            #print str(apidata['result']['skus'][num]['stock'])
                            print "assert stock ok"
                        except AssertionError,msg:
                            print msg
                            print str(apidata['result']['skus'][num]['stock'])
                            print m1[0]

                else:
                    #无sku
                    #商品名字
                    try:
                        self.assertEqual(apidata['result']['item_name'], iresault[12],msg="商品名字不一致")
                        print "assert no sku item_name ok"
                    except AssertionError,msg:
                        print msg
                        print str(apidata['result']['item_name'])
                        print iresault[12]


                    #商品编号
                    try:
                        self.assertEqual(apidata['result']['merchant_code'], iresault[14],msg="商品编号不一致")
                        print "assert no sku merchant_code ok"
                    except AssertionError,msg:
                        print msg
                        print str(apidata['result']['merchant_code'])
                        print iresault[14]

                    #商品库存
                    try:
                        b=iresault[10]
                        #print b
                        m=re.findall("(.*?)\.",b)
                        #print m[0]
                        self.assertEqual(str(apidata['result']['stock']), str(m[0]),msg="商品库存不一致")
                        print "assert no sku stock ok"
                    except AssertionError,msg:
                        print msg
                        print str(apidata['result']['stock'])
                        print str(m[0])

            nowid=id
            flag=flag+1

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testAccredit']
    unittest.main()