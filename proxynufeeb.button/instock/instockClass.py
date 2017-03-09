#*-* coding:UTF-8 *-*
from common import browserClass

class instockclass(browserClass.browser):
    def __init__(self):

        pass

    #查询条件
    def selcon(self,driver,*c):
        self.exjscommin(driver,"查询条件")
        #关闭
        self.exjscommin(driver,"关闭")
        self.exjscommin(driver,"查询条件")
        #确定
        self.exjscommin(driver,"确定")

        #库存商品
        self.exjscommin(driver,"查询条件")
        self.excutejs(driver,c[0])
        self.doubleclick(driver,c[1])
        #-翻页
        self.delaytime(2)
        self.pagechoice(driver)
        #-关闭
        self.exjscommin(driver,"关闭")
        self.doubleclick(driver,c[1])
        #-选中
        self.exjscommin(driver,"选中")
        self.exjscommin(driver,"关闭")
        self.exjscommin(driver,"查询条件")
        self.excutejs(driver,c[0])
        self.doubleclick(driver,c[1])
        self.exjscommin(driver,"选中")
        self.exjscommin(driver,"确定")
        #选择一类
        self.exjscommin(driver,"查询条件")
        self.excutejs(driver,c[0])
        self.doubleclick(driver,c[1])
        self.exjscommin(driver,"选择一类")
        self.exjscommin(driver,"关闭")
        self.exjscommin(driver,"查询条件")
        self.excutejs(driver,c[0])
        self.doubleclick(driver,c[1])
        self.exjscommin(driver,"选择一类")
        self.exjscommin(driver,"确定")

    #明细账本
    def detailaccbook(self,driver,id):
        self.findId(driver,id).click()
        #关闭
        self.exjscommin(driver,"关闭")
        self.findId(driver,id).click()

        #选中
        self.exjscommin(driver,"选中")
        self.exjscommin(driver,"关闭")
        self.findId(driver,id).click()
        self.exjscommin(driver,"选中")
        self.exjscommin(driver,"确定")
        self.pagechoice(driver)
        self.exjscommin(driver,"查看单据")
        self.exjscommin(driver,"退出")
        self.exjscommin(driver,"退出")
        self.findId(driver,id).click()
        #全部
        self.exjscommin(driver,"全部")
        self.exjscommin(driver,"关闭")
        self.findId(driver,id).click()
        self.exjscommin(driver,"全部")
        self.exjscommin(driver,"确定")
        self.pagechoice(driver)
        self.exjscommin(driver,"查看单据")
        self.exjscommin(driver,"退出")
        self.exjscommin(driver,"退出")

    #查询条件 选中选择一类
    def selcondition(self,driver,dblid,*c):
        self.doubleclick(driver,dblid)
        self.pagechoice(driver)
        if len(c)>0:
            self.exjscommin(driver,"查看单位基本信息")
            self.exjscommin(driver,"关闭")
        self.exjscommin(driver,"关闭")
        self.doubleclick(driver,dblid)
        self.exjscommin(driver,"选中")
        self.doubleclick(driver,dblid)
        self.exjscommin(driver,"选择一类")





