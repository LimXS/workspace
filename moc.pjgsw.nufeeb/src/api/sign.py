# -*- coding: utf-8 -*-
import requests
import json
import re
import time
import hashlib
import threading
import MySQLdb

lock=threading.Lock()

a=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
m2 = hashlib.md5()
src="testapp_keytesterp_appkeycustomerIdstub-cust-codeformatxmlmethodtaobao.qimen.itemlack.reportsign_methodmd5timestamp2015-04-26 00:00:07v2.0bodytest"
m2.update(src)
print m2.hexdigest()


strs="https://img3.doubanio.com/view/movie_poster_cover/ipst/public/p2332503406.jpg"
res=re.findall("c/(.*?)$",strs)
print  '.'.join(res)

lis={u"你",u"我"}
for a in lis:
    print a

conn=MySQLdb.connect(host="172.16.0.96",user="website",passwd="test@2011",db="test",port=4036)
cur=conn.cursor()
cur.execute('select * from dlysale')
cur.close()