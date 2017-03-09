#*-* coding:UTF-8 *-*
import time
import unittest
import  xml.dom.minidom
import traceback
import requests
import re
import json
from selenium.webdriver.common.action_chains import ActionChains
from common import browserClass
browser=browserClass.browser()

class lssaleTest(unittest.TestCase):
    u'''批零-零售开单'''

    def setUp(self):
        self.driver=browser.startBrowser('chrome')
        browser.set_up(self.driver)
        cookie = [item["name"] + "=" + item["value"] for item in self.driver.get_cookies()]
        #print cookie
        self.cookiestr = ';'.join(item for item in cookie)
        time.sleep(2)
        pass


    def tearDown(self):
        print "test over"
        #self.driver.close()
        pass



    def assernote(self,num1,num2,note,noteok,flag):
        try:
            self.assertEqual(num1,num2,msg=note)
            print noteok
        except AssertionError,msg:
            print msg
            print flag
            print num1
            print num2


    def testLssale(self):
        u'''批零-零售开单'''

        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        header2={'cookie':self.cookiestr,"Content-Type": "application/x-www-form-urlencoded"}

        #stamp=browser.gettimestamp()

        dom = xml.dom.minidom.parse(r'C:\workspace\moc.pjgsw.nufeeb\src\data\salecreatedata')
        modulename=browser.xmlRead(self.driver,dom,"module",5)
        moduledetail=browser.xmlRead(self.driver,dom,'moduledetail',5)

        browser.openModule2(self.driver,modulename,moduledetail)

        #选择商品
        '''
        lsitem=browser.xmlRead(self.driver,dom,'lsitem',0)
        lsiteminput=browser.xmlRead(self.driver,dom,'lsiteminput',0)
        lsitemok=browser.xmlRead(self.driver,dom,'lsitemok',0)

        #browser.setheader(self.driver,lsitem,lsiteminput,lsitemok)

        time.sleep(1)
        browser.findXpath(self.driver,lsitem).click()
        time.sleep(2)
        browser.findXpath(self.driver,lsiteminput).click()
        browser.findXpath(self.driver,lsitemok).click()
        '''
        #选择套餐
        lstaocan=browser.xmlRead(self.driver,dom,'lstaocan',0)
        lstaocaninput=browser.xmlRead(self.driver,dom,'lstaocaninput',0)
        lstaonum=browser.xmlRead(self.driver,dom,'lstaonum',0)
        lstaonumok=browser.xmlRead(self.driver,dom,'lstaonumok',0)
        lstaocanok=browser.xmlRead(self.driver,dom,'lstaocanok',0)

        #browser.setheader(self.driver,lsitem,lsiteminput,lsitemok)

        time.sleep(2)
        browser.findXpath(self.driver,lstaocan).click()
        time.sleep(1)
        browser.findXpath(self.driver,lstaocaninput).click()
        browser.findXpath(self.driver,lstaocanok).click()
        browser.findXpath(self.driver,lstaonum).send_keys("2")
        browser.findXpath(self.driver,lstaonumok).click()


        #选择会员
        lsvip=browser.xmlRead(self.driver,dom,'lsvip',0)
        lsvipinput=browser.xmlRead(self.driver,dom,'lsvipinput',0)
        lsvipok=browser.xmlRead(self.driver,dom,'lsvipok',0)

        #browser.setheader(self.driver,lsitem,lsiteminput,lsitemok)

        time.sleep(1)
        browser.findXpath(self.driver,lsvip).click()
        time.sleep(1)
        browser.findXpath(self.driver,lsvipinput).click()
        browser.findXpath(self.driver,lsvipok).click()

        #结算
        lscount=browser.xmlRead(self.driver,dom,'lscount',0)
        time.sleep(1)
        browser.findXpath(self.driver,lscount).click()

        #结算编号
        #print vchcode
        counturl="http://beefun.wsgjp.com/Beefun/Bill/Retail/RetailSaveHint.gspx?VCHTYPE=12&vipMemberId=869974051907919&vchcode=0"
        counttext=requests.get(url=counturl,headers=header)
        #print counttext.text
        countid=re.findall("id=\"(.*?)bankAccountEnabled\"",counttext.text)
        countid=countid[0]
        #print countid

        #整单优惠
        dismoney=browser.xmlRead(self.driver,dom,'dismoney',0)
        browser.findId(self.driver,countid+dismoney).clear()
        browser.findId(self.driver,countid+dismoney).send_keys("1.8")

        #实收金额
        getmoney=browser.xmlRead(self.driver,dom,'getmoney',0)
        browser.findId(self.driver,countid+getmoney).clear()
        browser.findId(self.driver,countid+getmoney).send_keys("300.25")

        #积分抵扣
        socreex=browser.xmlRead(self.driver,dom,'socreex',0)
        browser.findId(self.driver,countid+socreex).clear()
        browser.findId(self.driver,countid+socreex).send_keys("3")

        #储值消费
        chargecost=browser.xmlRead(self.driver,dom,'chargecost',0)
        browser.findId(self.driver,countid+chargecost).clear()
        browser.findId(self.driver,countid+chargecost).send_keys("18")

        #结算完成
        countok=browser.xmlRead(self.driver,dom,'countok',0)
        browser.findId(self.driver,countid+countok).click()

    def testLssalere(self):
        u'''批零-零售开单(这张单据要整单退货)'''

        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        header2={'cookie':self.cookiestr,"Content-Type": "application/x-www-form-urlencoded"}

        #stamp=browser.gettimestamp()

        dom = xml.dom.minidom.parse(r'C:\workspace\moc.pjgsw.nufeeb\src\data\salecreatedata')
        modulename=browser.xmlRead(self.driver,dom,"module",5)
        moduledetail=browser.xmlRead(self.driver,dom,'moduledetail',5)

        browser.openModule2(self.driver,modulename,moduledetail)


        lsnumber=browser.xmlRead(self.driver,dom,'lsnumber',0)
        lspeople=browser.xmlRead(self.driver,dom,'lspeople',0)
        lsdepartment=browser.xmlRead(self.driver,dom,'lsdepartment',0)
        lscompany=browser.xmlRead(self.driver,dom,'lscompany',0)
        lscate=browser.xmlRead(self.driver,dom,'lscate',0)
        lstime=browser.xmlRead(self.driver,dom,'lstime',0)

        #编号
        browser.exjsgettext(self.driver,lsnumber,"w","a+")
        #营业员（经手人）
        browser.exjsgettext(self.driver,lspeople,"a+","a+")
        #部门
        browser.exjsgettext(self.driver,lsdepartment,"a+","a+")
        #购买单位
        browser.exjsgettext(self.driver,lscate,"a+","a+")
        #门店（仓库）
        browser.exjsgettext(self.driver,lscompany,"a+","a+")
        #录单时间
        browser.writebyattr(self.driver,lstime,"title","a+","a+","")


        #选择商品

        lsitem=browser.xmlRead(self.driver,dom,'lsitem2',0)
        lsiteminput=browser.xmlRead(self.driver,dom,'lsiteminput2',0)
        lsiteminput2=browser.xmlRead(self.driver,dom,'lsiteminput',0)
        lsitemok=browser.xmlRead(self.driver,dom,'lsitemok2',0)

        #browser.setheader(self.driver,lsitem,lsiteminput,lsitemok)

        time.sleep(1)
        browser.findXpath(self.driver,lsitem).click()
        time.sleep(2)
        browser.findXpath(self.driver,lsiteminput).click()
        browser.findXpath(self.driver,lsiteminput2).click()
        time.sleep(2)
        lsitemcode=browser.xmlRead(self.driver,dom,'lsitemcode',0)
        lsitemname=browser.xmlRead(self.driver,dom,'lsitemname',0)
        code=browser.findXpath(self.driver,lsitemcode).text
        name=browser.findXpath(self.driver,lsitemname).text
        browser.writebyattr(self.driver,lsitemcode,"","a+","a+",1)
        browser.writebyattr(self.driver,lsitemname,"","a+","a+",1)

        lsitemcode2=browser.xmlRead(self.driver,dom,'lsitemcode2',0)
        lsitemname2=browser.xmlRead(self.driver,dom,'lsitemname2',0)
        code2=browser.findXpath(self.driver,lsitemcode2).text
        name2=browser.findXpath(self.driver,lsitemname2).text
        browser.writebyattr(self.driver,lsitemcode2,"","a+","a+",1)
        browser.writebyattr(self.driver,lsitemname2,"","a+","a+",1)
        browser.findXpath(self.driver,lsitemok).click()

        itemcodelis=[]
        itemnamelist=[]
        itemcodelis.append(code)
        itemcodelis.append(code2)
        itemnamelist.append(name)
        itemnamelist.append(name2)
        '''

        #选择套餐
        lstaocan=browser.xmlRead(self.driver,dom,'lstaocan',0)
        lstaocaninput=browser.xmlRead(self.driver,dom,'taocan2',0)
        lstaonum=browser.xmlRead(self.driver,dom,'lstaonum',0)
        lstaonumok=browser.xmlRead(self.driver,dom,'lstaonumok',0)
        lstaocanok=browser.xmlRead(self.driver,dom,'lstaocanok',0)

        #browser.setheader(self.driver,lsitem,lsiteminput,lsitemok)

        time.sleep(1)
        browser.findXpath(self.driver,lstaocan).click()
        time.sleep(1)
        browser.findXpath(self.driver,lstaocaninput).click()
        browser.findXpath(self.driver,lstaocanok).click()
        browser.findXpath(self.driver,lstaonum).send_keys("2")
        browser.findXpath(self.driver,lstaonumok).click()
        '''

        #选择会员
        lsvip=browser.xmlRead(self.driver,dom,'lsvip',0)
        lsvipinput=browser.xmlRead(self.driver,dom,'lsvipinput',1)
        lsvipok=browser.xmlRead(self.driver,dom,'lsvipok',0)

        #browser.setheader(self.driver,lsitem,lsiteminput,lsitemok)

        time.sleep(2)
        browser.findXpath(self.driver,lsvip).click()
        time.sleep(1)
        browser.findXpath(self.driver,lsvipinput).click()
        browser.findXpath(self.driver,lsvipok).click()


        #商品信息

        n=2
        cdismoney=0
        cdpmoney=0
        cnum=0
        for k in range(0,2):
            k+=1
            lssetinfo=browser.xmlRead(self.driver,dom,'lssetinfo',0)
            lssetinfo=lssetinfo+str(k)+"]/td["
            print u"第"+str(k)+u"行商品明细:"+str(itemnamelist[k-1])
            #商品编号
            itemcodexpath=lssetinfo+str(n)+"]/div"
            #print itemcodexpath
            itemcode=browser.findXpath(self.driver,itemcodexpath).text
            self.assernote(str(itemcode),str(itemcodelis[k-1]),u"商品编号不相同（页面和选择商品信息）","note itemcode ok",u"商品编号")

            #商品名称
            itemnamexpath=lssetinfo+str(n+1)+"]/div"
            itemname=browser.findXpath(self.driver,itemnamexpath).text

            self.assernote(str(itemname),str(itemnamelist[k-1]),u"商品名称不相同（页面和选择商品信息）","note itemname ok",u"商品名称")

            #数量
            itemnumsxpath=lssetinfo+str(n+12)+"]/div"
            #time.sleep(1)
            #定位到要双击的元素
            nums =browser.findXpath(self.driver,itemnumsxpath)
            #对定位到的元素执行鼠标双击操作
            ActionChains(self.driver).double_click(nums).perform()
            lsnumbersend=browser.xmlRead(self.driver,dom,'lsnumbersend',0)
            lsnumsendok=browser.xmlRead(self.driver,dom,'lsnumsendok',0)
            browser.findXpath(self.driver,lsnumbersend).send_keys(str(k+1))
            browser.findXpath(self.driver,lsnumsendok).click()
            browser.writebyattr(self.driver,itemnumsxpath,"","a+","a+",1)

            itemnumscompare=browser.findXpath(self.driver,itemnumsxpath).text
            self.assernote(str(itemnumscompare),str(k+1),u"数量不相同（页面和录入信息）","note item numbers ok",u"数量")
            cnum+=float(itemnumscompare)

            #单价
            itemdppricexpath=lssetinfo+str(n+14)+"]/div"
            priceself=browser.findXpath(self.driver,itemdppricexpath)
            ActionChains(self.driver).double_click(priceself).perform()
            lspricesend=browser.xmlRead(self.driver,dom,'lspricesend',0)
            lspriceok=browser.xmlRead(self.driver,dom,'lspriceok',0)
            browser.findXpath(self.driver,lspricesend).send_keys(str(k+11))
            browser.findXpath(self.driver,lspriceok).click()
            browser.writebyattr(self.driver,itemdppricexpath,"","a+","a+",1)

            itempricscompare=browser.findXpath(self.driver,itemdppricexpath).text
            self.assernote(str(itempricscompare),str(k+11),u"单价不相同（页面和录入信息）","note item price ok",u"单价")

            #金额
            itemmoneyxpath=lssetinfo+str(n+15)+"]/div"
            browser.writebyattr(self.driver,itemmoneyxpath,"","a+","a+",1)

            itemmoncompare=float(browser.findXpath(self.driver,itemmoneyxpath).text)
            self.assernote(str(itemmoncompare),str(float(itempricscompare)*float(itemnumscompare)),u"金额不相同（页面和计算）","note item money ok",u"金额")
            cdpmoney+=itemmoncompare
            #折扣
            itemdiscountxpath=lssetinfo+str(n+16)+"]/div"
            browser.writebyattr(self.driver,itemdiscountxpath,"","a+","a+",1)
            dis=browser.findXpath(self.driver,itemdiscountxpath).text
            self.assernote(str(dis),"0.85",u"折扣不相同（页面和会员信息）","note discount ok","折扣")


             #折后单价
            itemdispricexpath=lssetinfo+str(n+17)+"]/div"
            browser.writebyattr(self.driver,itemdispricexpath,"","a+","a+",1)
            dispricecom=browser.findXpath(self.driver,itemdispricexpath).text
            self.assernote(str(dispricecom),str(float(itempricscompare)*float(dis)),u"折后单价不相同（页面和计算）","note discount price ok",u"折后单价")

            #折后金额
            itemdismonxpath=lssetinfo+str(n+18)+"]/div"
            browser.writebyattr(self.driver,itemdismonxpath,"","a+","a+",1)
            dismoncom=browser.findXpath(self.driver,itemdismonxpath).text
            self.assernote(str(dismoncom),str(float(itemmoncompare)*float(dis)),u"折后金额不相同（页面和计算）","note discount money ok",u"折后金额")
            cdismoney+=float(dismoncom)

        #表单
        lsnums=browser.xmlRead(self.driver,dom,'lsnums',0)
        lsdpmoney=browser.xmlRead(self.driver,dom,'lsdpmoney',0)
        lsmoney=browser.xmlRead(self.driver,dom,'lsmoney',0)
        adzero=browser.xmlRead(self.driver,dom,'adzero',0)
        lsvipinfo=browser.xmlRead(self.driver,dom,'lsvipinfo',0)

        print u"商品合计数据验证....."
        #数量
        browser.writebyattr(self.driver,lsnums,"","a+","a+","")
        self.assernote(str(float(browser.findId(self.driver,lsnums).text)),str(cnum),u"数量不相同（页面和计算）","note sum num ok",u"数量")

        #折前金额
        browser.writebyattr(self.driver,lsdpmoney,"","a+","a+","")
        self.assernote(str(float(browser.findId(self.driver,lsdpmoney).text)),str(cdpmoney),u"折前金额不相同（页面和计算）","note sum discount before money ok",u"折前金额")

        #金额
        self.assernote(str(float(browser.findId(self.driver,lsmoney).text)),str(cdismoney),u"金额不相同（页面和计算）","note sum discount money ok",u"金额")
        browser.writebyattr(self.driver,lsmoney,"","a+","a+","")
        #抹零
        browser.writebyattr(self.driver,adzero,"","a+","a+","")
        #会员信息
        browser.writebyattr(self.driver,lsvipinfo,"","a+","a+","")


        #结算
        lscount=browser.xmlRead(self.driver,dom,'lscount',0)
        time.sleep(1)
        browser.findXpath(self.driver,lscount).click()

        #结算编号
        #print vchcode
        counturl="http://beefun.wsgjp.com/Beefun/Bill/Retail/RetailSaveHint.gspx?VCHTYPE=12&vipMemberId=870069546699788&vchcode=0"
        counttext=requests.get(url=counturl,headers=header)
        #print counttext.text
        countid=re.findall("id=\"(.*?)bankAccountEnabled\"",counttext.text)
        countid=countid[0]
        #print countid

        #整单优惠
        dismoney=browser.xmlRead(self.driver,dom,'dismoney',1)
        browser.findId(self.driver,countid+dismoney).clear()
        browser.findId(self.driver,countid+dismoney).send_keys("1.8")

        #实收金额
        getmoney=browser.xmlRead(self.driver,dom,'getmoney',1)
        browser.findId(self.driver,countid+getmoney).clear()
        browser.findId(self.driver,countid+getmoney).send_keys("110.02")

        #赠送积分
        givescore=browser.xmlRead(self.driver,dom,'givescore',1)
        scotetext=browser.findId(self.driver,countid+givescore).text
        #browser.findId(self.driver,countid+givescore).send_keys("19")

        #积分抵扣
        socreex=browser.xmlRead(self.driver,dom,'socreex',0)
        browser.findId(self.driver,countid+socreex).clear()
        browser.findId(self.driver,countid+socreex).send_keys("9")

        #储值消费
        chargecost=browser.xmlRead(self.driver,dom,'chargecost',0)
        browser.findId(self.driver,countid+chargecost).clear()
        browser.findId(self.driver,countid+chargecost).send_keys("19")



        #找零
        returnmoney=browser.xmlRead(self.driver,dom,'returnmoney',1)
        browser.findId(self.driver,countid+returnmoney).click()
        remoney=browser.findId(self.driver,countid+returnmoney).text
        self.assernote(str(remoney),str(78.17),u"找零不相同（页面和计算）","note return money ok",u"找零")


        #结算完成
        countok=browser.xmlRead(self.driver,dom,'countok',1)
        browser.findId(self.driver,countid+countok).click()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()