#*-* coding:UTF-8 *-*
import time
import re
import datetime
import unittest
import  xml.dom.minidom
import traceback
import requests
import json
from common import browserClass
browser=browserClass.browser()

class iteminfoTest(unittest.TestCase):
    u'''商品-商品信息'''

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



    def testitemInfo(self):
        u'''商品-商品信息'''
        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        dom = xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\itemmodule\itemlocation')
        modulename=browser.xmlRead(dom,"module",0)
        moduledetail=browser.xmlRead(dom,'moduledetail',0)

        browser.openModule2(self.driver,modulename,moduledetail)
        cookies=browser.cookieSave(self.driver)
        header3={'cookie':cookies,"Content-Type": "application/json"}
        header4={'cookie':cookies,"Content-Type": "application/x-www-form-urlencoded"}

        #页面id
        pageurl=browser.xmlRead(dom,"iteminfourl",0)
        pageid=browser.halfid(pageurl,header)
        #print pageid

        button=browser.xmlRead(dom,"button",0)
        btnexit=browser.xmlRead(dom,"btnexit",0)
        selok=browser.xmlRead(dom,"selok",0)
        selbtn=browser.xmlRead(dom,"selbtn",0)


        try:
            #刷新
            browser.refreshbutton(self.driver)

            #翻页
            browser.pagechoice(self.driver)

            #快速查询
            js="$(\"input[id$=edFilterStr]\").val('a1x');$(\"div[id$=btnFilter]\").click()"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)

            #定位
            js="$(\"input[id$=nodenames]\").val('classify')"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.exjscommin(self.driver,"定位")

            #编辑分类
            js="$(\"button[id$=btnTreeEdit]\").click()"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.excutejs(self.driver,js)

            #退出
            browser.exjscommin(self.driver,"退出")
            browser.openModule2(self.driver,modulename,moduledetail)

            #空白新增
            browser.exjscommin(self.driver,"空白新增")
            browser.exjscommin(self.driver,"关闭")
            browser.exjscommin(self.driver,"空白新增")
            browser.skupagesalman(self.driver)
            nums=browser.getrandnumber(2)
            js1="$(\"input[id$=edFullName]\").last().val('newitem"+str(nums[0])+"');$(\"input[id$=edUserCode]\").last().val('"+str(nums[0])+"')"
            js2="$(\"input[id$=edFullName]\").last().val('newitem"+str(nums[1])+"');$(\"input[id$=edUserCode]\").last().val('"+str(nums[1])+"')"
            browser.delaytime(1)
            browser.excutejs(self.driver,js1)
            browser.exjscommin(self.driver,"保存并新增")
            browser.excutejs(self.driver,js2)
            browser.exjscommin(self.driver,"保存并关闭")


            #编辑删除，蓝字

            for a in nums:
                js="$(\"div[class=GridBodyCellText]:contains('"+str(a)+"')\").last().attr(\"id\",\"itid"+str(a)+"\")"
                browser.delaytime(1)
                browser.excutejs(self.driver,js)
                browser.findId(self.driver,"itid"+str(a)).click()
                #-编辑
                js="$(\"a[class=GridDynamicButtonHorz]:contains('编辑')\").eq(1).attr(\"id\",\"editid\")"
                browser.delaytime(1)
                browser.excutejs(self.driver,js)
                browser.findId(self.driver,"editid").click()
                browser.skupagesalman(self.driver)
                browser.exjscommin(self.driver,"关闭")
                browser.findId(self.driver,"editid").click()
                browser.exjscommin(self.driver,"保存并关闭")
                #删除
                #browser.findId(self.driver,"itid"+str(a)).click()
                js="$(\"a[class=GridDynamicButtonHorz]:contains('删除')\").eq(1).attr(\"id\",\"delid\")"
                browser.delaytime(1)
                browser.excutejs(self.driver,js)
                browser.findId(self.driver,"delid").click()
                browser.accAlert(self.driver,0)
                browser.findId(self.driver,"delid").click()
                browser.accAlert(self.driver,1)


            #复制新增 删除
            js="$(\"div[class=GridBodyCellText]:contains('331菊花有商品编码')\").last().attr(\"id\",\"dpdelid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.findId(self.driver,"dpdelid").click()
            browser.exjscommin(self.driver,"复制新增")
            browser.exjscommin(self.driver,"关闭")
            browser.exjscommin(self.driver,"复制新增")
            browser.exjscommin(self.driver,"保存并新增")
            browser.exjscommin(self.driver,"保存并关闭")
            for k in range(2):
                js="$(\"div[class=GridBodyCellText]:contains('331菊花有商品编码')\").last().attr(\"id\",\"cpitid"+str(k)+"\")"
                browser.delaytime(1)
                browser.excutejs(self.driver,js)
                browser.findId(self.driver,"cpitid"+str(k)).click()
                browser.exjscommin(self.driver,"删除")
                browser.accAlert(self.driver,1)

            #导入
            browser.exjscommin(self.driver,"导入")
            browser.exjscommin(self.driver,"导入文件")
            browser.accAlert(self.driver,1)
            browser.exjscommin(self.driver,"关闭")

            #批量修改
            browser.exjscommin(self.driver,"批量修改")
            browser.exjscommin(self.driver,"关闭")
            browser.exjscommin(self.driver,"批量修改")
            browser.skupagesalman(self.driver,1)
            browser.exjscommin(self.driver,"保存并关闭")

            #搬移
            moveurl="http://dba.wsgjp.com.cn/Beefun/BaseInfo2/PTypeMoveTo.gspx"
            movetext=browser.requestget(moveurl,header3)
            moveid=browser.getdraftalterid(movetext,1)
            moveid=moveid[:10]
            #print moveid

            time.sleep(1)
            btnMoveTo=browser.xmlRead(dom,"btnMoveTo",0)
            pmovebtn=pageid+btnMoveTo
            #print pmovebtn
            browser.findId(self.driver,pmovebtn).click()

            #退出
            movcancel=moveid+btnexit

            movetop=moveid+browser.xmlRead(dom,"movetop",0)
            browser.findId(self.driver,movetop).click()

            #搬移至分类
            moveclassify=moveid+browser.xmlRead(dom,"moveclassify",0)
            browser.findId(self.driver,moveclassify).click()

            mcdeclbtn=moveid+browser.xmlRead(dom,"edTarget",0)
            browser.doubleclick(self.driver,mcdeclbtn)

            mvclurl="http://dba.wsgjp.com.cn/Beefun/Selector/PTypeClassSelector.gspx?HideStoppedItem=true"
            mvcltext=browser.requestget(mvclurl,header3)
            mvclid=browser.getdraftalterid(mvcltext,1)
            mvclid=mvclid[:10]
            #print mvclid
            #关闭
            browser.exjscommin(self.driver,"关闭")
            browser.doubleclick(self.driver,mcdeclbtn)
            #确定
            btnSelectClass=browser.xmlRead(dom,"btnSelectClass",0)
            browser.findId(self.driver,mvclid+btnSelectClass).click()

            #搬移至商品
            moveitem=moveid+browser.xmlRead(dom,"moveitem",0)
            browser.findId(self.driver,moveitem).click()
            mcdeitbtn=moveid+browser.xmlRead(dom,"edPtype",0)
            browser.doubleclick(self.driver,mcdeitbtn)

            mviturl="http://dba.wsgjp.com.cn/Beefun/Selector/PTypeSelector.gspx?HideStoppedItem=true"
            mvittext=browser.requestget(mviturl,header3)
            mvitid=browser.getdraftalterid(mvittext,1)
            mvitid=mvitid[:10]
            #print mvitid

            #关闭
            browser.exjscommin(self.driver,"关闭")
            browser.doubleclick(self.driver,mcdeitbtn)

            #确定
            time.sleep(1)
            browser.findId(self.driver,mvitid+selbtn).click()

            #商品搬移选择框退出
            browser.findId(self.driver,movcancel).click()
            browser.findId(self.driver,pmovebtn).click()
            #time.sleep(5)

            #确定
            moveensure=moveid+selok
            browser.findId(self.driver,moveensure).click()
            browser.accAlert(self.driver,1)
            browser.findId(self.driver,movcancel).click()

            #print u"搬移ok....."

            #停用
            js="$(\"div[class=GridBodyCellText]:contains('测试雨伞')\").last().attr(\"id\",\"stopid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.findId(self.driver,"stopid").click()
            stopitem=browser.xmlRead(dom,"stopitem",0)
            pstopitem=pageid+stopitem
            browser.findId(self.driver,pstopitem).click()
            browser.delaytime(1)
            browser.findId(self.driver,pstopitem).click()
           # print u"停用ok....."

            #往来单位商品编号设置
            comcode=pageid+button+str(1)
            browser.findId(self.driver,comcode).click()
            browser.exjscommin(self.driver,"关闭")
            browser.findId(self.driver,comcode).click()
            js="$(\"input[id$=edBType]\").last().attr(\"id\",\"comid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.buycompanysel(self.driver,"comid")
            browser.exjscommin(self.driver,"确定")
            browser.delaytime(1)
            browser.pagechoice(self.driver)
            browser.exjscommin(self.driver,"设置编号")
            browser.exjscommin(self.driver,"关闭")
            browser.exjscommin(self.driver,"设置编号")
            browser.exjscommin(self.driver,"确定")

            browser.exjscommin(self.driver,"复制到")
            browser.pagechoice(self.driver)
            browser.exjscommin(self.driver,"查看单位基本信息")
            browser.exjscommin(self.driver,"关闭")
            browser.exjscommin(self.driver,"关闭")
            browser.exjscommin(self.driver,"复制到")
            browser.exjscommin(self.driver,"添加")
            browser.exjscommin(self.driver,"保存并新增")
            browser.accAlert(self.driver,1)
            browser.exjscommin(self.driver,"保存并关闭")
            browser.accAlert(self.driver,1)
            browser.exjscommin(self.driver,"关闭")
            browser.exjscommin(self.driver,"选中")
            browser.exjscommin(self.driver,"确定")

            js="$(\"div[class=GridBodyCellText]:contains('测试商品有编码不包邮')\").attr(\"id\",\"cpiditem\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.findId(self.driver,"cpiditem").click()
            browser.exjscommin(self.driver,"复制到")
            js="$(\"div[class=GridBodyCellText]:contains('t5123')\").last().attr(\"id\",\"cpcomid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.findId(self.driver,"cpcomid").click()
            browser.exjscommin(self.driver,"选中")
            browser.accAlert(self.driver,1)

            browser.pagechoice(self.driver)

            browser.exjscommin(self.driver,"退出")


            #print u"往来单位商品编号设置OK...."


            #商品下载与对应
            itemdown=browser.xmlRead(dom,"itemdown",0)
            pitemdown=pageid+itemdown
            browser.findId(self.driver,pitemdown).click()

            browser.openModule2(self.driver,modulename,moduledetail)

        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            #print filename+u"常用-单据草稿.png"
            #browser.getpicture(self.driver,filename+u"notedraft.png")
            browser.getpicture(self.driver,filename+u"商品-商品信息.png")








if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
