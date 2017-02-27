#*-* coding:UTF-8 *-*
import unittest
import  xml.dom.minidom
import traceback
import reportsClass
browser=reportsClass.instockclass()

class deppeobusinessTest(unittest.TestCase):
    u'''报表-部门职员业务分析-业务员业务统计'''

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


    def test_depPeobusiness(self):
        u'''报表-部门职员业务分析-业务员业务统计'''
        dom = xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\reports\reportslocation.xml')
        module=browser.xmlRead(dom,'module',0)
        moduledetail=browser.xmlRead(dom,'moduledetail',5)
        moduledd=browser.xmlRead(dom,'depadd',4)

        browser.openModule3(self.driver,module,moduledetail,moduledd)

        headers={'cookie':self.cookiestr,'Content-Type': 'text/plain; charset=gb2312'}

        try:
            browser.exjscommin(self.driver,"关闭")
            browser.openModule3(self.driver,module,moduledetail,moduledd)
            browser.exjscommin(self.driver,"确定")

            #计算提成金额
            browser.exjscommin(self.driver,"计算提成金额")
            browser.selectbycon(self.driver,"提成规则名称","2")
            browser.exjscommin(self.driver,"删除提成规则")
            browser.accAlert(self.driver,0)
            browser.exjscommin(self.driver,"删除提成规则")
            browser.accAlert(self.driver,1)
            browser.exjscommin(self.driver,"退出")
            browser.exjscommin(self.driver,"计算提成金额")
            browser.exjscommin(self.driver,"新增提成规则")
            browser.exjscommin(self.driver,"关闭")
            browser.exjscommin(self.driver,"新增提成规则")
            newrule="rule2_"+str(browser.getrandnumber())
            browser.elementvalue(self.driver,"input","tePercentageName",newrule)
            url="http://dba.wsgjp.com.cn/Beefun/BaseInfo/SetPercentage.gspx?percentagetype=default"
            id=browser.getalertid(url,headers)
            xpath1=browser.xmlRead(dom,'depxpath1',0)
            xpath2=browser.xmlRead(dom,'depxpath2',0)
            moneyxpath=xpath1+id+xpath2+'2]'
            ratexpath=xpath1+id+xpath2+'3]'
            browser.delaytime(1)
            #print moneyxpath,ratexpath
            browser.findXpath(self.driver,moneyxpath).click()
            browser.findId(self.driver,id+"gridsale_begin_factor").send_keys('10')
            browser.findXpath(self.driver,ratexpath).click()
            browser.findId(self.driver,id+"gridsale_result_value").send_keys('1')
            #print id
            browser.exjscommin(self.driver,"保存")
            browser.accAlert(self.driver,1)
            browser.inputid(self.driver,"edFilterMode","销售金额")
            browser.exjscommin(self.driver,"选中")
            browser.exjscommin(self.driver,"退出")

            #筛选职员
            browser.exjscommin(self.driver,"筛选职员")
            browser.exjscommin(self.driver,"退出")
            browser.exjscommin(self.driver,"筛选职员")
            browser.elementvalue(self.driver,"input","edFullname","001")
            browser.exjscommin(self.driver,"确定")
            browser.exjscommin(self.driver,"筛选职员")
            browser.elementvalue(self.driver,"input","edUsercode","001")
            browser.exjscommin(self.driver,"确定")

            #刷新
            browser.refreshbutton(self.driver)

            browser.exjscommin(self.driver,"退出")
            browser.openModule3(self.driver,module,moduledetail,moduledd)


        except:
            print traceback.format_exc()
            filename=browser.xmlRead(dom,'filename',0)
            browser.delaytime(1)
            browser.getpicture(self.driver,filename+u"报表-部门职员业务分析-业务员业务统计.png")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()