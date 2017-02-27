#*-* coding:UTF-8 *-*

import unittest
import json
import requests
import re
import time
from common import  browserClass
browser=browserClass.browser()

class itemsdownCase(unittest.TestCase):


    def setUp(self):
        self.driver=browser.startBrowser('chrome')
        browser.set_up(self.driver)


    def tearDown(self):
        print "test over"
        pass


    def testitemsDown(self):
        u'''下载商品'''
        #进入下载页面
        module=".//*[@id='$80d499b2$ManagerMenuBar3']/div"
        modulename=".//*[@id='$80d499b2$ManagerMenuBar3_2']/td[3]"
        shop=".//*[@id='$19b126ff$treeEShopClass']/div/table[2]/tbody/tr/td[2]/div"
        browser.openModule3(self.driver, module, modulename, shop)
        
        btndown=".//*[@id='$19b126ff$btnDownLoad']"
        stock=".//*[@id='$c8892a83$saveqty']"
        
        okbtn="html/body/table[8]/tbody/tr[2]/td/div/table/tbody/tr/td/table/tbody/tr[2]/td/button"
        
        startdown=".//*[@id='$c8892a83$btnStart']"
        canwin=".//*[@id='$c8892a83$btnCancel']"
        
        
        cookie = [item["name"] + "=" + item["value"] for item in self.driver.get_cookies()]  
        self.cookiestr = ';'.join(item for item in cookie) 
        ''' 
        browser.openModule4(self.driver,btndown,stock,okbtn,startdown)    
        time.sleep(5)
        browser.findXpath(self.driver, canwin).click()
        ''' 
        
        url="http://beefun.wsgjp.com/Carpa.Web/Carpa.Web.Script.DataService.ajax/GetPagerData"
        headers={'Content-Type': 'application/json; charset=gb2312','cookie':self.cookiestr,}
        payload={"pagerId":"$19b126ff$gridPType_pager1","queryParams":{"eshopId":"2605638400292508735","classTypeId":"","platFullname":"","RelationStatus":0,"isShowZeroQty":True,"isRepeatXcode":False,"StockStatus":3},"orders":None,"filter":None,"first":0,"count":20}
        
        #去页面数据,并放入列表
        resp=requests.post(url,data=json.dumps(payload),headers=headers)
        res=resp.text
        #print res
        '''
        result=re.compile(r"\\")
        z=result.sub('',res) 
        result=re.compile(r"/")
        z=result.sub('',res) 
        z=z.strip(" ")
        data=json.loads(z)
        print data
        '''
        itemsno=re.findall("itemCount\":(.*?)}",res)
        itemexist=int(itemsno[0])
        print "itemscount:"+str(itemexist)
        
        
        before=re.findall("row(.*)itemCount",res)
        itemlist=re.findall("\[\"(.*?)-1\],",before[0])
        #页面中每一行商品
        for data in itemlist:
            itemlis=re.compile("\"")
            resault=itemlis.sub('',data)
            iresault=re.findall("(.*?),",resault)
            id=iresault[11]                      
            
            #print itemlist
               
            #取接口数据
            f=open('E:\wei\sp.dat','r')
            token=f.read()
            print "token:"+token
                        
            params={"itemid":id}
            publics={"method":"vdian.item.get","access_token":token,"version":"1.0","format":"json"}
                        
            payload={"param":json.dumps(params),"public":json.dumps(publics)}
            url="http://api.vdian.com/api"
            apires=requests.post(url,data=payload)
            apidata=json.loads(apires.text)
            print apidata
            #是否有sku
            sku=apidata['result']['skus']
            #页面和接口数据进行比较
      
            
          
        
        
        
        
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
    
    
    