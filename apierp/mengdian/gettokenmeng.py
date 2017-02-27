#*-* coding:UTF-8 *-*
import MySQLdb
def getmengToken():
    conn= MySQLdb.connect(host='172.16.0.96',user='website',passwd='test@2011',db='beefun',port = 4306)
    cur = conn.cursor()
    aa=cur.execute("SELECT token FROM eshop WHERE FullName='peter.yang0019@weimob.com'")
    print aa
    row=cur.fetchone()
    print row[0]
    info = cur.fetchmany(aa)
    '''
    print cur.fetchone()
    print cur.scroll(0,'absolute')

    for i in info:
        print i
    '''
    cur.close()
    conn.commit()
    conn.close()
    token= row[0]
    return token
getmengToken()