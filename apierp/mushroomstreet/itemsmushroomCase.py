#*-* coding:UTF-8 *-*
from common import base
from common import itemscompare
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


class itemsmushroomTest(unittest.TestCase):


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
        print u"蘑菇街商品接口测试完成"
        time.sleep(2)
        pass


    def testitemsMushroom(self):
        u'''蘑菇街...将商品数据和页面数据进行对比'''
        #获取商品页面数据并放入列表

        module=".//*[@id='$80d499b2$ManagerMenuBar3']/div"
        modulename=".//*[@id='$80d499b2$ManagerMenuBar3_2']/td[3]"
        shop=".//*[@id='$19b126ff$treeEShopClass']/div/table[2]/tbody/tr/td[2]/div"
        basec.findXpath(self.driver,module).click()
        basec.findXpath(self.driver,modulename).click()
        basec.findXpath(self.driver,shop).click()


        url="http://beefun.wsgjp.com.cn/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerData"
        headers={'Content-Type': 'application/json; charset=gb2312','cookie':self.cookiestr,}
        payload={"pagerId":"$19b126ff$gridPType_pager1","queryParams":{"eshopId":"869378240461870","ismall":False,"classTypeId":"","platFullname":"","RelationStatus":0,"StockStatus":3,"isShowZeroQty":False,"notShowZeroQty":False,"isRepeatXcode":False,"isGiftSku":False,"isDifrentXcoe":False,"isDifrentSkuXcode":False},"orders":None,"filter":None,"first":0,"count":20}


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
            itcompare=itemscompare.commonitemscompary(iresault)
            #print itemlist

            #取接口数据
            if id!=nowid:
                now=datetime.datetime.now()
                nowtime=now.strftime("%Y-%m-%d %H:%M:%S")
                print nowtime

                sql="SELECT token FROM eshop WHERE etypeid='2605638079543105363'"
                tokenall=basec.gettokeneach(sql)
                token=str(tokenall[2])
                print 'token....................................................................'
                token=re.findall('\'(.*?)\'',token)
                token=token[0].strip()
                #print len(token)
                print token
                apiurl="https://www.mogujie.com/openapi/api_v1_api/index"
                payloads={"access_token":token,"method":"youdian.item.getItemInfo","app_key":"6186bd31891451899b385b2aa8ce3713","itemId":id}
                apires=requests.post(apiurl,data=payloads)
                print apires.text

                apidata=json.loads(apires.text)
                #print apidata["status"]["msg"]
                #print apidata
                #是否有sku
                print "开始比较..........................."
                print "商品编号为："+str(id)
                print iresault[12]
                sku=len(apidata['result']['data']['item_skus'])
                print "sku:"+str(sku)
                #页面和接口数据进行比较
                if sku>1:
                    #有SKU
                    #名字
                    apiname=apidata['result']['data']['item_name']
                    itcompare.item_name(apiname)
                    #总数量
                    apistock=apidata['result']['data']['item_stock']
                    itcompare.item_num(apistock)
                    #大类型号，微店没有
                    apitype=apidata['result']['data']['item_code']
                    itcompare.item_type(apitype)

                    #具体各个型号商品
                    #型号

                    for num in range(0,sku):
                        print "sku具体信息"
                        print num+1
                        itemlis=re.compile("\"")
                        resault=itemlis.sub('',itemlist[flag+num+1])
                        iresault=re.findall(":(.*?),",resault)
                        itcompare=itemscompare.commonitemscompary(iresault)
                        #shap=iresault[12]
                        #print shap
                        apitype=''
                        valtpye=len(apidata['result']['data']['item_skus'][num]['sku_prop'])
                        for m in range(0,valtpye):
                            value=apidata['result']['data']['item_skus'][num]['sku_prop'][m]['value']
                            apitype=apitype+value+'_'
                        apitype=apitype[:-1]
                        itcompare.item_name(apitype)
                        #编号
                        skucode=apidata['result']['data']['item_skus'][num]['sku_code']
                        itcompare.item_skuid(skucode)
                        #库存
                        skustock=apidata['result']['data']['item_skus'][num]['sku_stock']
                        itcompare.item_num(skustock)

                elif sku==1:
                    #无sku
                    #商品名字
                    apiname=apidata['result']['data']['item_name']
                    itcompare.item_name(apiname)

                    #商品编号
                    apitype=apidata['result']['data']['item_code']
                    itcompare.item_type(apitype)

                    #商品库存
                    apistock=apidata['result']['data']['item_stock']
                    itcompare.item_num(apistock)
                else:
                    print u"接口SKU标志返回错误，请查看文档"
                    print "标志为："+str(apidata['result']['data']['item_skus'])
            nowid=id
            flag=flag+1

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testAccredit']
    unittest.main()