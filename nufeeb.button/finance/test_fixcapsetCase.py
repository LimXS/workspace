#*-* coding:UTF-8 *-*
import unittest
import  xml.dom.minidom
import traceback
from common import browserClass
import random
browser=browserClass.browser()

class fixcapsetTest(unittest.TestCase):
    u'''财务-固定资产-固定资产设置'''

    def setUp(self):
        self.driver=browser.startBrowser('chrome')
        browser.set_up(self.driver)
        cookie = [item["name"] + "=" + item["value"] for item in self.driver.get_cookies()]
        #print cookie
        self.cookiestr = ';'.join(item for item in cookie)

        browser.delaytime(1)
        pass


    def tearDown(self):
        print "test over"
        self.driver.close()
        pass


    def test_fixcapSet(self):
        u'''财务-固定资产-固定资产设置'''
        header={'cookie':self.cookiestr,"Content-Type": "application/json"}
        dom = xml.dom.minidom.parse(r'C:\workspace\nufeeb.button\finance\financelocation')
        module=browser.xmlRead(dom,'module',0)
        moduledetail=browser.xmlRead(dom,'moduledetail',9)
        moduledd=browser.xmlRead(dom,'moduledd',9)

        browser.openModule3(self.driver,module,moduledetail,moduledd)

        #页面id
        #pageurl=browser.xmlRead(dom,"fixcapsaleurl",0)
        #pageid=browser.getalertid(pageurl,header)

        try:
            #复制新增
            browser.delaytime(1)
            browser.exjscommin(self.driver,"复制新增")
            browser.exjscommin(self.driver,"关闭")
            browser.exjscommin(self.driver,"复制新增")
            deno=browser.getrandnumber()
            js="$(\"input[id$=edFullName]\").val($(\"input[id$=edFullName]\").val()+'"+str(deno)+"')"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.exjscommin(self.driver,"保存")
            browser.exjscommin(self.driver,"关闭")

            #删除
            js="$(\"div[class=GridBodyCellText]:contains('"+deno+"')\").last().attr(\"id\",\"delid\")"
            #print deno
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.findId(self.driver,"delid").click()
            browser.exjscommin(self.driver,"删除")
            browser.accAlert(self.driver,1)

            #明细账本
            js="$(\"div[class=GridBodyCellText]:contains('gdzcj')\").first().attr(\"id\",\"setdetialid\")"
            browser.delaytime(2)
            browser.excutejs(self.driver,js)
            browser.delaytime(1)
            browser.findId(self.driver,"setdetialid").click()
            browser.exjscommin(self.driver,"明细账本",1)
            browser.exjscommin(self.driver,"关闭")
            browser.exjscommin(self.driver,"明细账本",1)
            browser.exjscommin(self.driver,"确定")
            browser.pagechoice(self.driver)
            browser.exjscommin(self.driver,"查看凭证")
            browser.exjscommin(self.driver,"退出")
            browser.exjscommin(self.driver,"退出")

            #空白新增
            browser.exjscommin(self.driver,"空白新增")
            fixclass=["计算机","打印机","显示器","空调","办公桌椅","固定电话","饮水机"]
            fixnamenew="固定资产_"+random.choice(fixclass)+str(browser.getrandnumber())
            js="$(\"input[id$=edFullName]\").val(\""+fixnamenew+"\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.exjscommin(self.driver,"保存")
            browser.exjscommin(self.driver,"关闭")

            #修改
            browser.exjscommin(self.driver,"修改")
            browser.exjscommin(self.driver,"关闭")
            browser.exjscommin(self.driver,"修改")
            browser.exjscommin(self.driver,"保存")




            #修改期初金额
            browser.exjscommin(self.driver,"修改期初金额")
            browser.exjscommin(self.driver,"退出")
            browser.exjscommin(self.driver,"修改期初金额")
            js="$(\"input[id$=ednumber]\").val('1000')"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.exjscommin(self.driver,"确定")


            #搬移
            js="$(\"div[class=GridBodyCellText]:contains('"+fixnamenew+"')\").first().attr(\"id\",\"makeid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.findId(self.driver,"makeid").click()
            browser.exjscommin(self.driver,"搬移")
            browser.exjscommin(self.driver,"关闭")
            browser.exjscommin(self.driver,"搬移")
            #搬移至分类
            js="$(\"input[id$=radTarget]\").click()"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            js="$(\"input[id$=edTarget]\").last().attr(\"id\",\"classid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.doubleclick(self.driver,"classid")
            browser.exjscommin(self.driver,"关闭")
            browser.doubleclick(self.driver,"classid")
            js="$(\"div[class=GridBodyCellText]:contains('classtest')\").last().attr(\"id\",\"classid2\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.findId(self.driver,"classid2").click()
            browser.exjscommin(self.driver,"选中")

            #搬移到固定资产
            js="$(\"input[id$=radAtype]\").click()"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            js="$(\"input[id$=edAtype]\").last().attr(\"id\",\"moveid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.doubleclick(self.driver,"moveid")
            browser.exjscommin(self.driver,"关闭")
            browser.doubleclick(self.driver,"moveid")
            js="$(\"div[class=GridBodyCellText]:contains('classtest')\").last().attr(\"id\",\"seleid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.findId(self.driver,"seleid").click()
            browser.exjscommin(self.driver,"进入下级")
            browser.exjscommin(self.driver,"返回上级")
            browser.excutejs(self.driver,js)
            browser.delaytime(1)
            browser.findId(self.driver,"seleid").click()
            browser.exjscommin(self.driver,"选中")
            js="$(\"div[class=GridBodyCellText]:contains('固定资产')\").last().attr(\"id\",\"seleid2\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.findId(self.driver,"seleid2").click()
            browser.exjscommin(self.driver,"选中")

            browser.exjscommin(self.driver,"确定")

            #删除
            js="$(\"div[class=TreeNodeText]:contains('classtest')\").click()"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            js="$(\"div[class=GridBodyCellText]:contains('"+fixnamenew+"')\").last().attr(\"id\",\"delid\")"
            browser.delaytime(1)
            browser.excutejs(self.driver,js)
            browser.findId(self.driver,"delid").click()
            browser.exjscommin(self.driver,"删除")
            browser.accAlert(self.driver,0)
            browser.exjscommin(self.driver,"删除")
            browser.accAlert(self.driver,1)

            #退出
            browser.exjscommin(self.driver,"退出")
            browser.openModule3(self.driver,module,moduledetail,moduledd)

        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            #print filename+u"常用-单据草稿.png"
            #browser.getpicture(self.driver,filename+u"notedraft.png")
            browser.getpicture(self.driver,filename+u"财务-固定资产-固定资产设置.png")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
