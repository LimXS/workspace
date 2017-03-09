#*-* coding:UTF-8 *-*
import time
import unittest
import  xml.dom.minidom
import traceback

from common import browserClass
browser=browserClass.browser()

class notedraftTest(unittest.TestCase):
    u'''常用-单据草稿'''

    def setUp(self):
        browser.deleteandmkdir()
        f=open('C:\\workspace\\nufeeb.button\\data\\assertlog','w')
        f.write('')
        f.close()
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



    def testnoteDraft(self):
        u'''常用-单据草稿'''
        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        dom = xml.dom.minidom.parse(r'C:\workspace\nufeeb.button\frequentlyused\frelocation')
        module=browser.xmlRead(dom,'module',0)
        moduledetail=browser.xmlRead(dom,'moduledetail',0)


        try :
            #进入单据草稿页面
            browser.openModule2(self.driver,module,moduledetail)

            #页面id
            urlid="http://beefun.wsgjp.com/Beefun/Assistant/BusinessDraft.gspx"
            pageid=browser.halfid(urlid,header)

            copyanopen=pageid+browser.xmlRead(dom,'copyanopen',0)
            alternote=pageid+browser.xmlRead(dom,'alternote',0)
            delnote=pageid+browser.xmlRead(dom,'delnote',0)
            selnote=pageid+browser.xmlRead(dom,'selnote',0)
            basetype=browser.xmlRead(dom,'basetype',0)
            refrdragt=browser.xmlRead(dom,'refrdragt',0)

            #复制打开
            browser.findId(self.driver,copyanopen).click()
            time.sleep(1)
            browser.openModule2(self.driver,module,moduledetail)

            #修改单据
            browser.findId(self.driver,alternote).click()
            time.sleep(1)
            browser.openModule2(self.driver,module,moduledetail)

            #删除单据
            #取消
            browser.findId(self.driver,delnote).click()
            browser.accAlert(self.driver,0)
            #确定
            browser.findId(self.driver,delnote).click()
            browser.accAlert(self.driver,1)

            #刷新
            refresh=basetype+pageid+refrdragt
            #print refresh
            browser.findXpath(self.driver,refresh).click()

            #查询
            browser.findId(self.driver,selnote).click()

            #select id
            cookies=browser.cookieSave(self.driver)
            header3={'cookie':cookies,"Content-Type": "application/json"}
            selurl="http://beefun.wsgjp.com/Beefun/Assistant/BusinessDraftCondition.gspx"
            seltext=browser.requestget(selurl,header3)
            selid=browser.getdraftalterid(seltext)
            #self.selectid=selid
            #print selid
            #关闭查询窗口
            #time.sleep(1)
            selclose=selid+browser.xmlRead(dom,'selclose',0)
            browser.findId(self.driver,selclose).click()
            #time.sleep(1)
            browser.findId(self.driver,selnote).click()
            #print "close ok"

            #查询OK
            selok=selid+browser.xmlRead(dom,'selok',0)
            selnum=selid+browser.xmlRead(dom,'selnum',0)
            seltype=selid+browser.xmlRead(dom,'seltype',0)
            seloppeo=selid+browser.xmlRead(dom,'seloppeo',0)
            selsumm=selid+browser.xmlRead(dom,'selsumm',0)
            selbcom=selid+browser.xmlRead(dom,'selbcom',0)
            selhapeo=selid+browser.xmlRead(dom,'selhapeo',0)
            seloutcate=selid+browser.xmlRead(dom,'seloutcate',0)
            selincate=selid+browser.xmlRead(dom,'selincate',0)

            next=browser.xmlRead(dom,'typenext',0)
            topnext=browser.xmlRead(dom,'typetopnext',0)
            before=browser.xmlRead(dom,'typebe',0)
            topebefore=browser.xmlRead(dom,'typetopbe',0)

            #单据编号
            browser.findId(self.driver,selnum).click()
            browser.findId(self.driver,selnum).clear()
            browser.findId(self.driver,selnum).send_keys("note NO.")
            time.sleep(1)
            #browser.findId(self.driver,seltype).click()

            #单据类型
            browser.doubleclick(self.driver,seltype)
            typeurl="http://beefun.wsgjp.com/Beefun/Selector/VchTypeSelector.gspx?t=1&type=all&Add=False&Mode=Money&all=1"
            typeid=browser.halfid(typeurl,header3)
            #print typeid
            typeselok=typeid+browser.xmlRead(dom,'selbtn',0)
            typeselclose=typeid+browser.xmlRead(dom,'selclose',0)


            #下一页
            typenext=basetype+typeid+next
            #print typenext
            browser.findXpath(self.driver,typenext).click()
            #第一页
            typetopbe=basetype+typeid+topebefore
            browser.findXpath(self.driver,typetopbe).click()
            #上一页
            typebe=basetype+typeid+before
            browser.findXpath(self.driver,typebe).click()
            #最后一页
            typetopnext=basetype+typeid+topnext
            browser.findXpath(self.driver,typetopnext).click()

            #关闭
            browser.findId(self.driver,typeselclose).click()
            browser.doubleclick(self.driver,seltype)
            #选择，ok
            browser.findId(self.driver,typeselok).click()



            #制单人
            browser.doubleclick(self.driver,seloppeo)
            creaturl="http://beefun.wsgjp.com/Beefun/Selector/ETypeSelector.gspx?SelectClass=false&Add=False&Mode=Money&all=1"
            crpeoid=browser.halfid(creaturl,header3)
            #print crpeoid
            crpeoselok=crpeoid+browser.xmlRead(dom,'selbtn',0)
            crpeoselclose=crpeoid+browser.xmlRead(dom,'selclose',0)

            #关闭
            browser.findId(self.driver,crpeoselclose).click()
            browser.doubleclick(self.driver,seloppeo)
            #选择，ok
            browser.findId(self.driver,crpeoselok).click()

            #摘要
            browser.findId(self.driver,selsumm).click()
            browser.findId(self.driver,selsumm).clear()
            browser.findId(self.driver,selsumm).send_keys("summary")

            #往来单位
            browser.doubleclick(self.driver,selbcom)
            browser.delaytime(1)
            browser.pagechoice(self.driver)
            browser.exjscommin(self.driver,"关闭")
            browser.doubleclick(self.driver,selbcom)
            browser.exjscommin(self.driver,"查看单位基本信息")
            browser.exjscommin(self.driver,"关闭")
            browser.exjscommin(self.driver,"选中")






            #经手人
            browser.doubleclick(self.driver,selhapeo)
            papeourl="http://beefun.wsgjp.com/Beefun/Selector/ETypeSelector.gspx?SelectClass=false?Add=True&HideStoppedItem=false&ShowFreight=false&Bcategory=1"
            papeoid=browser.halfid(papeourl,header3)
            #print papeoid
            ppeoselok=papeoid+browser.xmlRead(dom,'selbtn',0)
            ppeoselclose=papeoid+browser.xmlRead(dom,'selclose',0)

            #关闭
            browser.findId(self.driver,ppeoselclose).click()
            browser.doubleclick(self.driver,selhapeo)
            #选择，ok
            browser.findId(self.driver,ppeoselok).click()


            #出库仓库
            browser.doubleclick(self.driver,seloutcate)
            ocateurl="http://beefun.wsgjp.com/Beefun/Selector/KTypeSelector.gspx?SelectClass=True&HideStoppedItem=false&FilterMode=fullname&FilterStr="
            ocateid=browser.halfid(ocateurl,header3)
            #print "ocateid....."
            #print ocateid
            ocateselok=ocateid+browser.xmlRead(dom,'selbtn',0)
            ocateselclose=ocateid+browser.xmlRead(dom,'selclose',0)

            #关闭
            #time.sleep(1)
            #print ocateselclose
            browser.findId(self.driver,ocateselclose).click()
            browser.doubleclick(self.driver,seloutcate)
            #选择，ok
            browser.findId(self.driver,ocateselok).click()



            #入库仓库
            browser.doubleclick(self.driver,selincate)
            incateurl="http://beefun.wsgjp.com/Beefun/Selector/KTypeSelector.gspx?SelectClass=True&HideStoppedItem=false&FilterMode=fullname&FilterStr="
            incateid=browser.halfid(incateurl,header3)
            #print incateid
            icateselok=incateid+browser.xmlRead(dom,'selbtn',0)
            icateselclose=incateid+browser.xmlRead(dom,'selclose',0)

            #关闭
            time.sleep(1)
            browser.findId(self.driver,icateselclose).click()
            browser.doubleclick(self.driver,selincate)
            #选择，ok
            browser.findId(self.driver,icateselok).click()

            #开始日期
            #browser.doubleclick(self.driver,selsttime)
            #结束日期
            #browser.doubleclick(self.driver,selendtime)
            #查询
            browser.findId(self.driver,selok).click()

            #退出
            browser.delaytime(1)
            browser.findId(self.driver,pageid+browser.xmlRead(dom,'selclose',0)).click()
            browser.delaytime(1)
            browser.openModule2(self.driver,module,moduledetail)
            browser.refreshbutton(self.driver)
            browser.delaytime(3)

            browser.pagechoice(self.driver)


            #打印
            #browser.findId(self.driver,printnote).click()
            #browser.accAlert(self.driver,1)
            #browser.accAlert(self.driver,1)



        except :
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            #print filename+u"常用-单据草稿.png"
            #browser.getpicture(self.driver,filename+u"notedraft.png")
            browser.getpicture(self.driver,filename+u"常用-单据草稿.png")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
