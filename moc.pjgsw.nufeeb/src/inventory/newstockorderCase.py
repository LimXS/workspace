#*-* coding:UTF-8 *-*
import time
import unittest
import  xml.dom.minidom
import traceback
from common import browserClass
browser=browserClass.browser()

class newstockTest(unittest.TestCase):
    u'''新增订货订单'''

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
        self.driver.close()
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

    def testnewStock(self):
        u'''新增订货订单'''
        dom = xml.dom.minidom.parse(r'C:\workspace\moc.pjgsw.nufeeb\src\data\basedata')

        module='moudle'
        modulename=browser.xmlRead(self.driver,dom,module,0)
        moduledetail=browser.xmlRead(self.driver,dom,'page',0)

        browser.openModule2(self.driver,modulename,moduledetail)

        #编号
        time.sleep(2)
        stockorderid=browser.xmlRead(self.driver,dom,'stockorderid',0)
        js="var code=document.getElementById('"+stockorderid+"').value;"+stockorderid+".setAttribute('value',code);"
        self.driver.execute_script(js)
        id=browser.findId(self.driver,stockorderid).get_attribute("value")
        #print id
        browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata','w',0,id)
        browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata','a+',0,'\n')


        #录单日期
        time.sleep(2)
        ordertime=browser.xmlRead(self.driver,dom,'ordertime',0)
        js="var code=document.getElementById('"+ordertime+"').value;"+ordertime+".setAttribute('value',code);"
        self.driver.execute_script(js)
        ordertime=browser.findId(self.driver,ordertime).get_attribute("value")
        browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata','a+',0,ordertime)
        browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata','a+',0,'\n')

        #供货单位
        try:
            xpath=browser.xmlRead(self.driver,dom,'stockcompany',0)
            browser.findXpath(self.driver,xpath).click()
            #self.driver.implicitly_wait(10)
            comsec=browser.xmlRead(self.driver,dom,'companysec',0)
            browser.findXpath(self.driver,comsec).click()

            choice=browser.xmlRead(self.driver,dom,'choicecompany',0)
            browser.findXpath(self.driver,choice).click()
            print u"设置供货单位成功"
        except:
            print u"设置供货单位失败"
            print(traceback.format_exc())
            #js='document.getElementById("$eb57a3e$edBType").style.color="blue";'
            #self.driver.execute_script(js)

        companypath=browser.xmlRead(self.driver,dom,'company',0)
        time.sleep(2)
        js="var code=document.getElementById('"+companypath+"').value;"+companypath+".setAttribute('value',code);"
        self.driver.execute_script(js)
        company=browser.findId(self.driver,companypath).get_attribute("value")
        #print company
        try:
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata','a+',0,company)
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata','a+',0,'\n')
        except:
            print u"设置供货单位checkdata失败"
            print(traceback.format_exc())


        #经手人
        try:
            handle=browser.xmlRead(self.driver,dom,'handlepeople',0)
            browser.findXpath(self.driver,handle).click()

            peoplesec=browser.xmlRead(self.driver,dom,'peoplesec',0)
            browser.findXpath(self.driver,peoplesec).click()

            choicepeople=browser.xmlRead(self.driver,dom,'choicepeople',0)
            browser.findXpath(self.driver,choicepeople).click()
            print u"设置经手人成功"
        except:
            print u"设置经手人失败"
            print(traceback.format_exc())
        time.sleep(2)
        people=browser.xmlRead(self.driver,dom,'people',0)
        js="var code=document.getElementById('"+people+"').value;"+people+".setAttribute('value',code);"
        self.driver.execute_script(js)
        people=browser.findId(self.driver,people).get_attribute("value")
        #print people
        try:
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata','a+',0,people)
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata','a+',0,'\n')
        except:
            print u"设置经手人checkdata失败"
            print(traceback.format_exc())



        #日期
        time.sleep(2)
        ordate=browser.xmlRead(self.driver,dom,'ordate',0)
        js="var code=document.getElementById('"+ordate+"').value;"+ordate+".setAttribute('value',code);"
        self.driver.execute_script(js)
        ordate=browser.findId(self.driver,ordate).get_attribute("value")
        #print ordate
        try:
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata','a+',0,ordate)
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata','a+',0,'\n')
        except:
            print u"设置交货日期checkdata失败"
            print(traceback.format_exc())

        try:
            #收货仓库
            repertory=browser.xmlRead(self.driver,dom,'repertory',0)
            browser.findXpath(self.driver,repertory).click()

            repertorysec=browser.xmlRead(self.driver,dom,'repertorysec',0)
            browser.findXpath(self.driver,repertorysec).click()

            choicerepertory=browser.xmlRead(self.driver,dom,'choicerepertory',0)
            browser.findXpath(self.driver,choicerepertory).click()
            print u"设置收货仓库成功"
        except:
            print u"设置收货仓库失败"
            print(traceback.format_exc())

        time.sleep(2)
        whichre=browser.xmlRead(self.driver,dom,'whichre',0)
        js="var code=document.getElementById('"+whichre+"').value;"+whichre+".setAttribute('value',code);"
        self.driver.execute_script(js)
        whichre=browser.findId(self.driver,whichre).get_attribute("value")
        #print whichre
        try:
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata','a+',0,whichre)
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata','a+',0,'\n')
        except:
            print u"设置收货仓库checkdata失败"
            print(traceback.format_exc())

        #摘要
        try:
            sumnote=u'我是摘要abcde.233333333333333'
            summary=browser.xmlRead(self.driver,dom,'summary',0)
            browser.findXpath(self.driver,summary).send_keys(sumnote)
            print u"设置摘要成功"
        except:
            print u"设置摘要失败"
            print(traceback.format_exc())

        time.sleep(2)
        summaryid=browser.xmlRead(self.driver,dom,'summaryid',0)
        js="var code=document.getElementById('"+summaryid+"').value;"+summaryid+".setAttribute('value',code);"
        self.driver.execute_script(js)
        summarynote=browser.findId(self.driver,summaryid).get_attribute("value")
        #print summarynote
        if summarynote!=sumnote:
            print u"输入摘要和显示的摘要不一致"
        try:
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata','a+',0,summarynote)
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata','a+',0,'\n')
        except:
            print u"写入摘要checkdata失败"
            print(traceback.format_exc())


        #附加说明
        try:
            comnote=u'我是附加说明abcde.233333333333333'
            comment=browser.xmlRead(self.driver,dom,'comment',0)
            browser.findXpath(self.driver,comment).send_keys(comnote)
            print u"设置附加说明成功"
        except:
            print u"设置附加说明失败"
            print(traceback.format_exc())
        time.sleep(2)
        commentid=browser.xmlRead(self.driver,dom,'commentid',0)
        js="var code=document.getElementById('"+commentid+"').value;"+commentid+".setAttribute('value',code);"
        self.driver.execute_script(js)
        commentnote=browser.findId(self.driver,commentid).get_attribute("value")
        #print commentnote
        if commentnote!=comnote:
            print u"输入附加说明和显示的摘要不一致"
        try:
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata','a+',0,commentnote)
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata','a+',0,'\n')
        except:
            print u"写入附加说明checkdata失败"
            print(traceback.format_exc())


        #录入单据
        #名字
        try:
            itemname=browser.xmlRead(self.driver,dom,'itemname',0)
            browser.findXpath(self.driver,itemname).click()

            item=browser.xmlRead(self.driver,dom,'item',0)
            browser.findXpath(self.driver,item).click()
            time.sleep(2)
            inputfirst=browser.xmlRead(self.driver,dom,'inputfirst',0)
            browser.findXpath(self.driver,inputfirst).click()
            infirstchoice=browser.xmlRead(self.driver,dom,'infirstchoice',0)
            browser.findXpath(self.driver,infirstchoice).click()
            print u"设置单据1名字成功"

        except:
            print u"录入单据1名字失败"
            print(traceback.format_exc())

        try:
            getname1=browser.xmlRead(self.driver,dom,'getitemname1',0)
            name1=browser.findXpath(self.driver,getname1).text
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata','a+',0,name1)
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata','a+',0,'\n')
        except:
            print u"录入单据名字checkdata1失败"
            print(traceback.format_exc())
        time.sleep(2)

        try:
            inputsecound=browser.xmlRead(self.driver,dom,'inputsecound',0)
            browser.findXpath(self.driver,inputsecound).click()
            insecoundchoice=browser.xmlRead(self.driver,dom,'insecoundchoice',0)
            browser.findXpath(self.driver,insecoundchoice).click()
            print u"设置单据2名字成功"
        except:
            print u"录入单据名字2失败"
            print(traceback.format_exc())
        try:
            getname2=browser.xmlRead(self.driver,dom,'getitemname2',0)
            name2=browser.findXpath(self.driver,getname2).text
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata','a+',0,name2)
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata','a+',0,'\n')
        except:
            print u"录入单据名字checkdata2失败"
            print(traceback.format_exc())



        #数量
        try:
            num=[]
            numfirst=browser.xmlRead(self.driver,dom,'numfirst',0)
            inputnum=browser.xmlRead(self.driver,dom,'inputnum',0)
            browser.findXpath(self.driver,numfirst).click()
            browser.findXpath(self.driver,inputnum).send_keys("777")
            print u"设置数量1成功"
            time.sleep(1)

            numsecound=browser.xmlRead(self.driver,dom,'numsecound',0)
            browser.findXpath(self.driver,numsecound).click()
            browser.findXpath(self.driver,inputnum).send_keys("888")
            time.sleep(1)
            print u"设置数量2成功"
        except:
            print u"录入单据数量失败"
            print(traceback.format_exc())



        num1=browser.xmlRead(self.driver,dom,'num1',0)
        numq1=browser.findXpath(self.driver,num1).text

        browser.findXpath(self.driver,comment).click()

        if numq1!='777':
            print u"输入数量和显示数量不一致"
        try:
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata','a+',0,numq1)
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata','a+',0,'\n')
            num.append(numq1)
        except:
            print u"录入单据数量checkdata1失败"
            print(traceback.format_exc())

        browser.findXpath(self.driver,comment).click()
        num2=browser.xmlRead(self.driver,dom,'num2',0)
        numq=browser.findXpath(self.driver,num2).text


        if numq!='888':
            print u"输入数量和显示数量不一致"
        try:
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata','a+',0,numq)
            browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata','a+',0,'\n')
            num.append(numq)
        except:
            print u"录入单据数量checkdata2失败"
            print(traceback.format_exc())



        #折前单价
        try:
            sigle=[]
            pricefirst=browser.xmlRead(self.driver,dom,"pricefirst",0)
            pricesecound=browser.xmlRead(self.driver,dom,'pricesecound',0)
            price=browser.xmlRead(self.driver,dom,'price',0)
            for n in range(1,5):
                pricexpath=pricefirst+str(n)+pricesecound
                time.sleep(2)
                browser.findXpath(self.driver,pricexpath).click()
                try:
                    browser.findXpath(self.driver,price).send_keys("20.25")
                    print u"设置折前单价"+str(n)+u"成功"

                except:
                    break

        except:
            print u"录入单据折前单价失败"
            print(traceback.format_exc())

        browser.findXpath(self.driver,comment).click()

        price1=browser.xmlRead(self.driver,dom,'price1',0)
        pr1=browser.findXpath(self.driver,price1).text
        sigle.append(pr1)

        price2=browser.xmlRead(self.driver,dom,'price2',0)
        pr2=browser.findXpath(self.driver,price2).text
        sigle.append(pr2)
        for a in range(len(sigle)):
            if sigle[a]!='20.25':
                print u"第"+str(a)+u"个商品输入折前单价和显示折前单价不一致"
            else:
                print u"折前单价"+str(a)+u"价正确"

        try:
            for b in range(len(sigle)):
                browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata','a+',0,str(sigle[b]))
                browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata','a+',0,'\n')
        except:
            print u"录入单据折前单价checkdata失败"
            print(traceback.format_exc())

        #折扣
        try:
            browser.findXpath(self.driver,comment).click()
            discount=browser.xmlRead(self.driver,dom,'discount',0)
            dissend=browser.xmlRead(self.driver,dom,'dissend',0)
            browser.findXpath(self.driver,discount).click()
            browser.findXpath(self.driver,dissend).send_keys("0.85")
        except:
            print u"录入单据折扣失败"
            print(traceback.format_exc())

        #税率
        try:
            browser.findXpath(self.driver,comment).click()
            tax=browser.xmlRead(self.driver,dom,'tax',0)
            taxsend=browser.xmlRead(self.driver,dom,'taxsend',0)
            browser.findXpath(self.driver,tax).click()
            time.sleep(2)
            browser.findXpath(self.driver,taxsend).send_keys("12.25")
        except:
            print u"录入税率折扣失败"
            print(traceback.format_exc())


        #商品编号
        itemno1=browser.xmlRead("aa",dom,'itmeno1',0)
        itemno2=browser.xmlRead("aa",dom,'itemno2',0)
        itemcode=[]
        for k in range(len(sigle)):
            codexpath=itemno1+str(k+1)+itemno2
            code=browser.findXpath(self.driver,codexpath).text
            try:
                browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata','a+',0,code)
                browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata','a+',0,'\n')
                itemcode.append(code)
            except:
                print u"录入商品编号checkdata失败"
                print(traceback.format_exc())


        #折前金额

        totalmoney1=browser.xmlRead(self.driver,dom,"totalmoney1",0)
        totalmoney2=browser.xmlRead(self.driver,dom,'totalmoney2',0)
        #print "money..........................................."
        #print sigle
        #print num
        for m in range(1,3):
            xpath=totalmoney1+str(m)+totalmoney2
            money=float(browser.findXpath(self.driver,xpath).text)
            pagemoney=float(sigle[m-1])*int(num[m-1])
            if str(money)!=str(pagemoney):
                print u"折前金额"+str(m)+u"错误"
                print money
                print pagemoney
            else:
                print u"折前金额"+str(m)+u"正确"
            try:
               browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata','a+',0,str(money))
               browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata','a+',0,'\n')
            except:
                print u"录入金额checkdata失败"
                print(traceback.format_exc())

        browser.findXpath(self.driver,comment).click()
        #单价
        dissiglexpath=browser.xmlRead(self.driver,dom,"dissigle",0)
        dissigle=float(browser.findXpath(self.driver,dissiglexpath).text)
        pagetemp=17.2125
        self.assernote(dissigle,pagetemp,u"单价不相同",u"单价相同",u"单价")
        try:
               browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata','a+',0,str(dissigle))
               browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata','a+',0,'\n')
        except:
            print u"录入单价checkdata失败"
            print(traceback.format_exc())

        #金额
        dismoneyxpath=browser.xmlRead(self.driver,dom,"dismoney",0)
        dismoney=float(browser.findXpath(self.driver,dismoneyxpath).text)
        pagetemp=13374.11
        self.assernote(dismoney,pagetemp,u"金额不相同",u"金额相同",u"金额")
        try:
               browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata','a+',0,str(dismoney))
               browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata','a+',0,'\n')
        except:
            print u"录入金额checkdata失败"
            print(traceback.format_exc())

        #税额
        taxtotalxpath=browser.xmlRead(self.driver,dom,"taxtotal",0)
        taxtotal=float(browser.findXpath(self.driver,taxtotalxpath).text)
        pagetemp=1638.33
        self.assernote(taxtotal,pagetemp,u"税额不相同","税额相同","税额")
        try:
               browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata','a+',0,str(taxtotal))
               browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata','a+',0,'\n')
        except:
            print u"录入税额checkdata失败"
            print(traceback.format_exc())

        #税后单价
        taxsiglexpath=browser.xmlRead(self.driver,dom,"taxsigle",0)
        taxsigle=float(browser.findXpath(self.driver,taxsiglexpath).text)
        pagetemp=19.321
        self.assernote(taxsigle,pagetemp,u"税后单价不相同",u"税后单价相同",u"税后单价")
        try:
               browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata','a+',0,str(taxsigle))
               browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata','a+',0,'\n')
        except:
            print u"录入税后单价checkdata失败"
            print(traceback.format_exc())

        #税后金额
        taxmoneyxpath=browser.xmlRead(self.driver,dom,"taxmoney",0)
        taxmoney=float(browser.findXpath(self.driver,taxmoneyxpath).text)
        pagetemp=15012.44
        self.assernote(taxmoney,pagetemp,u"税后金额不相同",u"税后金额相同",u"税后金额")
        try:
               browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata','a+',0,str(taxmoney))
               browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata','a+',0,'\n')
        except:
            print u"录入税后金额checkdata失败"
            print(traceback.format_exc())

        #折扣税率
        try:
               browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata','a+',0,str(0.85))
               browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata','a+',0,'\n')
               browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata','a+',0,str(1))
               browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata','a+',0,'\n')
               browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata','a+',0,str(12.25))
               browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata','a+',0,'\n')
               browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata','a+',0,str(0))
               browser.handleFile(self.driver,r'C:\workspace\moc.pjgsw.nufeeb\src\data\checkdata','a+',0,'\n')
        except:
            print u"录入税后金额checkdata失败"
            print(traceback.format_exc())

        #保存或退出单据
        try:
           saveorexit=browser.xmlRead(self.driver,dom,"saveorexit",0)
           browser.findXpath(self.driver,saveorexit).click()
        except:
            print u"保存或退出单据报错"
            print(traceback.format_exc())

        #进行保存
        try:
            save=browser.xmlRead(self.driver,dom,"save",0)
            browser.findXpath(self.driver,save).click()
        except:
            print u"保存单据报错"
            print(traceback.format_exc())



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()