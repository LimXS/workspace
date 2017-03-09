#*-* coding:UTF-8 *-*

import datetime
import xml.dom.minidom

import gevent.pool
import gevent.monkey

gevent.monkey.patch_all()

from common import browserClass
browser=browserClass.browser()



def newcookie():
    #central note
    while 1:
        try:
            driver=browser.startBrowser('chrome')
            browser.set_up(driver)
            #browser.set_up(driver)
            #driver.get("http://dba.wsgjp.com.cn/")
            dom = xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\frequentlyused\frelocation')
            module=browser.xmlRead(dom,'module',0)
            moduledetail=browser.xmlRead(dom,'moduledetail',1)

            browser.openModule2(driver,module,moduledetail)
            browser.delaytime(1)
            browser.refreshbutton(driver)
            browser.delaytime(1)
            cookies=browser.cookieSave(driver)
            browser.delaytime(1)
            #driver.close()

            f=open(r"D:\cookies\cennote.txt",'w')
            f.write(cookies)
            f.close()
            #driver.close()

            #check
            driver=browser.startBrowser('chrome')
            browser.set_up(driver)

            dom = xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\stock\stocklocation')

            modulename=browser.xmlRead(dom,"module",0)
            moduledetail=browser.xmlRead(dom,'moduledetail',1)

            browser.openModule2(driver,modulename,moduledetail)
            browser.delaytime(1)
            browser.refreshbutton(driver)
            browser.delaytime(1)
            cookies=browser.cookieSave(driver)
            browser.delaytime(1)
            #driver.close()

            f=open(r"D:\cookies\stocksave.txt",'w')
            f.write(cookies)
            f.close()
            #driver.close()

            #关闭
            driver=browser.startBrowser('chrome')
            browser.set_up(driver)

            dom = xml.dom.minidom.parse(r'C:\workspace\proxynufeeb.button\finance\financelocation')
            module=browser.xmlRead(dom,'module',0)
            moduledetail=browser.xmlRead(dom,'moduledetail',1)
            browser.openModule2(driver,module,moduledetail)
            browser.delaytime(1)
            driver.close()
            print "取cookie成功"
            break
        except:
            print "取cookie失败 重新取"
            pass

def f(salredata,salreurl,headers):
    '''
    fc=open(r"D:\cookies\stocksave.txt")
    nskcookie=fc.read()
    headers={'cookie':nskcookie,"Content-Type": "application/json"}
    salreurl="http://dba.wsgjp.com.cn/Beefun/Beefun.Bill.StockOrderBill.ajax/Save"
    '''
    pageorderdata=browser.requestpost(salreurl,salredata,headers,1)
    print pageorderdata

def f2(salredata):
    '''
    fc=open(r"D:\cookies\stocksave.txt")
    nskcookie=fc.read()
    headers={'cookie':nskcookie,"Content-Type": "application/json"}
    salreurl="http://dba.wsgjp.com.cn/Beefun/Beefun.Bill.StockOrderBill.ajax/Save"
    '''
    pageorderdata=browser.requestpost(salreurl,salredata,headers,1)
    print pageorderdata


def fun(num):
    today = datetime.date.today()
    #overday=today+datetime.timedelta(days=-6)

    today=today.strftime('%Y-%m-%d')
    getdatas=[]
    for a in range(0,num):
        #stockurlsave="http://dba.wsgjp.com.cn/Beefun/Beefun.Bill.StockOrderBill.ajax/Save"
        nskdata=(
        {"bill":{"date":"2017-01-04","draft":False,"displaynumber":"","number":"TJHD-20170104"+browser.getrandnumber()+str(a),"inputno":"2605637371041214558",
                 "inputfullname":"毕方","redword":False,"redold":False,"billtype":0,"ktypeid":"2605637371178862817","kfullname":"主仓库",
                 "btypetax":0,"todate":today,"efullname":"丁超","currencyid":0,"btypeid":"2605637371041213604",
                 "bfullname":"网店客户","etypeid":"869735145061843","summary":"","comment":"",
                 "details":[{"prop1":0,"prop1name":"","prop2":0,"prop2name":"","prop3":0,"prop3name":"","pic_url":"https://img.alicdn.com/bao/uploaded/i1/T1WlXHFlFgXXXXXXXX_!!0-item_pic.jpg",
                             "ptypeid":"870037142332159","pfullname":"得力803封箱器 胶带切割器打包切割器 金属封箱胶带打包切割","pname":"得力80","ptypecode":"803",
                             "brandname":"","temp_ucode":"803","temp_ucode_flag":True,"ptypeunit":"","unit":"1","unitrate":1,"ptypestandard":"","ptypetype":"",
                             "ptypearea":"","snenabled":0,"ptypeweight":0,"oneweight":0,"batchno":None,"producedate":None,"expirationdate":None,"position":None,
                             "pstatus":0,"comment":"","prop1_enabled":False,"prop2_enabled":False,"prop3_enabled":False,"fullbarcode":"","retailprice":28,
                             "ptypeweightall":0,"tax":0,"showstockqty":1000026.89,"assdpprice":325,"discount":1,"assqty":1,"price":325,"dpprice":325,"qty":1,
                             "dptotal":325,"asstpprice":325,"tpprice":325,"tptotal":325,"taxtotal":0,"assprice":325,"total":325,"mallfee":0,"urate0":"","urate1":"",
                             "urate2":""}],"isover":False,"../Selector/BTypeSelector.gspx":"00002","customerreceiver":None,"customerreceivermobile":None,
                 "customerreceiverphone":None,"customerreceiverzipcode":None,"customerreceiverprovince":None,"customerreceivercity":None,
                 "customerreceiverdistrict":None,"customerreceiveraddress":None,"deliveryinfoid":0,"deliveryinfotext":"","total":325,"ftypeid":0}}
            )
        getdatas.append(nskdata)

    return getdatas

def main():
    #newcookie()
    fc=open(r"D:\cookies\stocksave.txt")
    nskcookie=fc.read()
    senddatas=fun(1000)
    #print nskcookie
    global headers
    global salreurl
    headers={'cookie':nskcookie,"Content-Type": "application/json"}

    salreurl="http://dba.wsgjp.com.cn/Beefun/Beefun.Bill.StockOrderBill.ajax/Save"


    print "pool"
    pool = gevent.pool.Pool(300)
    data=pool.map(f2,senddatas)

    #print data


    '''

    print "no pool"
    jobs = [gevent.spawn(f, salreurl,headers,sendata) for sendata in senddatas]
    gevent.joinall(jobs)
    '''

if __name__ == '__main__':
  main()