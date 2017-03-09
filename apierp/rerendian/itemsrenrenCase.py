#*-* coding:UTF-8 *-*
from common import base
import unittest
import traceback
import re
import requests
import json
import time
import hashlib
import datetime


import sys
reload(sys)
sys.setdefaultencoding('utf8')

basec=base.baseCommon()


class itemsrenrenTest(unittest.TestCase):


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
        print u"人人店商品接口测试完成"
        pass


    def testitemsRenren(self):
        u'''人人店...将商品数据和页面数据进行对比'''
        #获取商品页面数据并放入列表

        module=".//*[@id='$80d499b2$ManagerMenuBar3']/div"
        modulename=".//*[@id='$80d499b2$ManagerMenuBar3_2']/td[3]"
        shop=".//*[@id='$19b126ff$treeEShopClass']/div/table[2]/tbody/tr/td[2]/div"
        basec.findXpath(self.driver,module).click()
        basec.findXpath(self.driver,modulename).click()
        basec.findXpath(self.driver,shop).click()


        url="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerData"
        headers={'Content-Type': 'application/json; charset=gb2312','cookie':self.cookiestr,}
        payload={"pagerId":"$19b126ff$gridPType_pager1","queryParams":{"eshopId":"869277121746859","ismall":False,"classTypeId":"","platFullname":"","RelationStatus":0,"StockStatus":3,"isShowZeroQty":False,"notShowZeroQty":False,"isRepeatXcode":False,"isGiftSku":False,"isDifrentXcoe":False,"isDifrentSkuXcode":False},"orders":None,"filter":None,"first":0,"count":20}


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

                apiurl="http://api04.weiba04.com/router/rest"

                appid="5b11e5f1b3763ba5"
                method="weiba.wxrrd.trade.details"
                timestamp=nowtime
                sql="SELECT token FROM eshop WHERE shopAccount='xmy666'"
                token=basec.gettokeneach(sql)
                access_token=token[2]
                access_token=access_token[0]

                secret="eef1445431edb7f6d36c90dd70572b47"
                goods_id=id

                signbefore3="access_token="+access_token+"&appid=5b11e5f1b3763ba5&goods_id="+goods_id+"&method=weiba.wxrrd.goods.details&secret=eef1445431edb7f6d36c90dd70572b47&timestamp="+nowtime

                m2 = hashlib.md5()
                m2.update(signbefore3)
                sign3= m2.hexdigest().upper()
                url3=apiurl+"?appid="+appid+"&secret="+secret+"&method=weiba.wxrrd.goods.details&timestamp="+nowtime+"&access_token="+access_token+"&sign="+sign3+"&goods_id="+goods_id
                apires3=requests.get(url=url3)
                print apires3.text
                apidata=json.loads(apires3.text)
                #print apidata
                #是否有sku
                print "开始比较..........................."
                print "商品编号为："+str(id)
                print iresault[12]
                sku=apidata['data']['is_sku']
                print "sku:"+str(sku)
                #页面和接口数据进行比较
                if sku==1:
                    #有SKU
                    #名字
                    try:
                        #print iresault[12].decode("gbk")
                        #print chardet.detect(iresault[12])
                        #print chardet.detect(str(apidata['data']['title']))
                        #print chardet.detect(str(iresault[12]))
                        name=iresault[12]

                        self.assertEqual(apidata['data']['title'], name,msg="SKU商品名字不一致")
                        print "assert title ok"
                    except AssertionError,msg:
                        print msg
                        print apidata['data']['title']
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
                        self.assertEqual(str(apidata['data']['stock']), str(m[0]),msg="SKU商品库存不一致")
                        #print "n:"+str(n)
                        print "assert stock ok"
                    except AssertionError,msg:
                        print msg
                        print str(apidata['data']['stock'])
                        print str(m[0])

                    #大类型号，微店没有
                    try:
                        self.assertEqual(apidata['data']['goods_sn'], str(iresault[14]),msg="商品sku大类型号不一致")
                        print "assert total sku ok"
                    except AssertionError,msg:
                        print msg
                        print apidata['data']['goods_sn']
                        print str(iresault[14])

                    #具体各个型号商品
                    #型号

                    for num in range(0,len(apidata['data']['products'])):
                        print "sku具体信息"
                        print num+1
                        itemlis=re.compile("\"")
                        resault=itemlis.sub('',itemlist[flag+num+1])
                        iresault=re.findall(":(.*?),",resault)
                        shap=iresault[12].replace('_',':')
                        #print shap
                        try:
                            self.assertEqual(apidata['data']['products'][num]['props_str'], shap,msg="sku具体商品型号不一致")
                            #print str(apidata['result']['skus'][num]['title'])
                            print "assert title ok"

                        except AssertionError,msg:
                            print msg
                            print apidata['data']['products'][num]['props_str']
                            print iresault[12]
                        #编号
                        try:
                            self.assertEqual(apidata['data']['products'][num]['product_sn'], iresault[9],msg="sku具体商品编号不一致")
                            #print str(apidata['result']['skus'][num]['sku_merchant_code'])
                            print "assert sku_merchant_code ok"

                        except AssertionError,msg:
                            print msg
                            print apidata['data']['products'][num]['product_sn']
                            print iresault[9]
                        #库存
                        try:
                            b1=iresault[10]
                            #print b
                            m1=re.findall("(.*?)\.",b1)
                            #print m[0]
                            self.assertEqual(str(apidata['data']['products'][num]['stock']), str(m1[0]),msg="sku具体商品库存不一致")
                            #print str(apidata['result']['skus'][num]['stock'])
                            print "assert stock ok"
                        except AssertionError,msg:
                            print msg
                            print apidata['data']['products'][num]['stock']
                            print m1[0]

                elif sku==0:
                    #无sku
                    #商品名字
                    try:
                        name=iresault[12]
                        self.assertEqual(apidata['data']['title'],name ,msg="商品名字不一致")
                        print "assert no sku title ok"
                    except AssertionError,msg:
                        print msg
                        print str(apidata['data']['title'])
                        print name


                    #商品编号
                    try:
                        self.assertEqual(apidata['data']['goods_sn'], iresault[14],msg="商品编号不一致")
                        print "assert no sku goods_sn ok"
                    except AssertionError,msg:
                        print msg
                        print apidata['data']['goods_sn']
                        print iresault[14]

                    #商品库存
                    try:
                        b=iresault[10]
                        #print b
                        m=re.findall("(.*?)\.",b)
                        #print m[0]
                        self.assertEqual(str(apidata['data']['stock']), str(m[0]),msg="商品库存不一致")
                        print "assert no sku stock ok"
                    except AssertionError,msg:
                        print msg
                        print apidata['data']['stock']
                        print m[0]
                else:
                    print u"接口SKU标志返回错误，请查看文档"
                    print "标志为："+str(apidata['data']['is_sku'])
            nowid=id
            flag=flag+1

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testAccredit']
    unittest.main()