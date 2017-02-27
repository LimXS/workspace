#*-* coding:UTF-8 *-*
from common import browserClass

class instockclass(browserClass.browser):
    def __init__(self):

        pass

    #查询条件 商品
    def selconitem(self,driver,id):
        self.doubleclick(driver,id)
        self.pagechoice(driver)
        self.exjscommin(driver,"关闭")
        self.doubleclick(driver,id)
        self.exjscommin(driver,"选中")
        self.doubleclick(driver,id)
        self.exjscommin(driver,"选择一类")

    #查询条件 单位
    def selcompany(self,driver,id,*c):
        self.doubleclick(driver,id)
        if len(c)>0:
            self.exjscommin(driver,"进入下级")
        self.exjscommin(driver,"查看单位基本信息")
        self.exjscommin(driver,"关闭")
        if len(c)>0:
            self.exjscommin(driver,"返回上级")
        self.pagechoice(driver)
        self.exjscommin(driver,"关闭")
        self.doubleclick(driver,id)
        self.exjscommin(driver,"选中")
        if len(c)>0:
            self.exjscommin(driver,"选中")
        self.doubleclick(driver,id)
        self.exjscommin(driver,"选择一类")
        
        
    #查询条件
    def selothersavecon(self,driver):
        self.exjscommin(driver,"查询条件")
        self.exjscommin(driver,"关闭")
        self.exjscommin(driver,"查询条件")
        self.exjscommin(driver,"另存为")
        self.exjscommin(driver,"取消")
        self.exjscommin(driver,"另存为")
        js="$(\"input[id$=txtconfigname]\").last().val('solution"+str(self.getrandnumber())+"')"
        self.delaytime(1)
        self.excutejs(driver,js)
        self.exjscommin(driver,"确定")
        self.exjscommin(driver,"删除")

    #查询条件all
    def selcomcaitpeo(self,driver,*c):
        js="$(\"input[id$=edEType]\").last().attr(\"id\",\"peoid\");$(\"input[id$=edKType]\").last().attr(\"id\",\"cateid\")"
        js2="$(\"input[id$=edPType]\").last().attr(\"id\",\"itemid\");$(\"input[id$=edBType]\").last().attr(\"id\",\"comid\")"
        self.delaytime(1)
        self.excutejs(driver,js)
        self.excutejs(driver,js2)

        if len(c)==0:
            #-商品
            self.selconitem(driver,"itemid")

        #-往来单位
        self.selcompany(driver,"comid")

        #-内部职员
        self.passpeoplesel(driver,"peoid")

        #-仓库
        self.passpeoplesel(driver,"cateid")

        self.exjscommin(driver,"确定")

    def catclslall(self,driver,id,*c):
        self.doubleclick(driver,id)
        self.exjscommin(driver,"关闭")
        self.doubleclick(driver,id)
        self.exjscommin(driver,"选中")
        if len(c)==0:
            self.doubleclick(driver,id)
            self.exjscommin(driver,"全部")

    #明细账本
    def detailacc(self,driver):
        self.exjscommin(driver,"明细账本")
        self.exjscommin(driver,"查看单据")
        self.exjscommin(driver,"退出")
        self.pagechoice(driver)
        self.selectbycon(driver,"商品名称","cx")
        self.exjscommin(driver,"退出")

    #最近一周
    def weeklylast(self,driver):
        js="$(\"input[id$=edDateScope]\").last().attr(\"id\",\"seltimeid\")"
        self.delaytime(1)
        self.excutejs(driver,js)
        self.doubleclick(driver,"seltimeid")
        js="$(\"div:contains('最近一周')\").last().attr(\"id\",\"weekid\")"
        self.delaytime(1)
        self.excutejs(driver,js)
        self.findId(driver,"weekid").click()
        self.exjscommin(driver,"查询")

    #套餐查询条件
    def selpackage(self,driver):
        self.exjscommin(driver,"查询条件")
        self.exjscommin(driver,"关闭")
        self.exjscommin(driver,"查询条件")
        js="$(\"input[id$=edEType]\").last().attr(\"id\",\"peoid\");$(\"input[id$=edKType]\").last().attr(\"id\",\"cateid\")"
        js2="$(\"input[id$=edCombo]\").last().attr(\"id\",\"packageid\");$(\"input[id$=edBType]\").last().attr(\"id\",\"comid\")"
        self.delaytime(1)
        self.excutejs(driver,js)
        self.excutejs(driver,js2)

        #套餐
        self.doubleclick(driver,"packageid")
        self.exjscommin(driver,"关闭")
        self.doubleclick(driver,"packageid")
        self.exjscommin(driver,"添加")
        self.exjscommin(driver,"保存",1)
        self.exjscommin(driver,"确定")
        self.exjscommin(driver,"保存并继续")
        self.exjscommin(driver,"确定")
        self.exjscommin(driver,"退出")
        self.exjscommin(driver,"选中")

        #往来单位
        self.selcompany(driver,"comid")

        #-内部职员
        self.passpeoplesel(driver,"peoid")

        #-仓库
        self.passpeoplesel(driver,"cateid")

        self.exjscommin(driver,"确定")













