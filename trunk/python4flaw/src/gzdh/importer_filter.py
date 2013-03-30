# -*- coding:utf-8 -*-

import MySQLdb, re, filesearch
import time
import datetime

def saveFilter(date, key, value):
    
#    print date
#    print key
#    print value
    
    db = MySQLdb.connect(host="localhost", user="root", passwd="chengyaoan", db="gzdh")
    cur = db.cursor()
    
    #execute an sql query
    cur.execute('select * from applog_filter where time = %s and name = %s ', (date, db.escape_string(key)))
    one = cur.fetchone()
    
    if one is None:
        cur.execute("""insert into applog_filter(time,name,count) values(%s,%s,%s)""", (date, key, value))
    else:
        cur.execute("""update applog_filter set count = %s
        where time = %s and name = %s """,
          (value, date, key))
    
    cur.close ()
    db.commit()
    db.close()


def readAppLog(filename):
    
    FILTER_PATTERN = re.compile(r'4444444444444444444444==value=(.*)')
    
    table = {}
    filereg = re.compile(r'\d{4}-\d{2}-\d{2}')
    fs = filereg.findall(filename)
    
    reg = re.compile(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}')
    
    linecount = 0
    
    for line in open(filename):
        aline = line.strip()
        #[INFO ] 2012-12-06 16:49:21 [com.client.common.ServiceUse][600] =======电子渠道全球通选号调用boss=============
        
        linecount += 1
        if linecount % 1000 == 0:
            print 'line count:', linecount
        
        times = re.findall(reg, aline)
        if len(times) == 0:
            continue
    
        m = FILTER_PATTERN.search(aline)
        if m is None:
            continue
        else:
            key = m.groups()[0]
            if table.has_key(key):
                table[key] = table[key] + 1
            else:
                table[key] = 1
            
        
    for current in table:
        counts = table[current]
        print counts, current 
        saveFilter(fs[0], current, counts)
        
        



if __name__ == '__main__':
    
#    FILTER_PATTERN = re.compile(r'4444444444444444444444==value=(.*)')
#    str = '[INFO ] 2013-01-10 11:00:30 [com.client.representation.struts.CharsFilter][53] 4444444444444444444444==value=Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; @FhlL5FQjC/B4Ki.tO8}Ddr2>suii2<*q-OHj)'
#    str = '[INFO ] 2013-01-10 18:06:22 [com.client.representation.struts.CharsFilter][53] 4444444444444444444444==value=WT-FPC=id=21d428fef24e02214941357109960343:lv=1357812436671:ss=1357811736796:fs=1357109960343:pv_Num=11:vt_Num=14; ProductsViewHistory=%7B%22VO%22%3A%5B%7B%22bizCode%22%3A%22GOTONE_BENDI_SUIT_88%22%2C%22bizName%22%3A%2288%E5%85%83%E5%85%A8%E7%90%83%E9%80%9A%E6%9C%AC%E5%9C%B0%E5%A5%97%E9%A4%90%22%2C%22url%22%3A%22%2Fcommodity%2Foptions%2Fdetail%2FGOTONE_BENDI_SUIT_88.shtml%22%2C%22icon%22%3A%22%2Fupfile%2Fimages%2Fv2012_cms%2Fproducts%2FGOTONE_BENDI_SUIT_88-icon.jpg%3Fver%3D20120907172945%22%7D%2C%7B%22bizCode%22%3A%22GOTONE_NEW_ZF_SUIT%22%2C%22bizName%22%3A%22%E6%96%B0%E5%85%A8%E7%90%83%E9%80%9A%E5%95%86%E6%97%85%E3%80%81%E4%B8%8A%E7%BD%91%E5%A5%97%E9%A4%90%E3%80%81%E6%9C%AC%E5%9C%B0%E5%A5%97%E9%A4%90%22%2C%22url%22%3A%22%2Fcommodity%2Foptions%2Fdetail%2FGOTONE_NEW_ZF_SUIT.shtml%22%2C%22icon%22%3A%22%2Fupfile%2Fimages%2Fv2012_cms%2Fproducts%2FGOTONE_NEW_ZF_SUIT-icon.jpg%3Fver%3D20111202065548%22%7D%2C%7B%22bizCode%22%3A%22PushEmail%22%2C%22bizName%22%3A%22139%E9%82%AE%E7%AE%B1%E6%89%8B%E6%9C%BA%E5%AE%A2%E6%88%B7%E7%AB%AF%22%2C%22url%22%3A%22%2Fcommodity%2Foptions%2Fdetail%2FPushEmail.shtml%22%2C%22icon%22%3A%22%2Fupfile%2Fimages%2Fv2012_cms%2Fproducts%2FPushEmail-icon.jpg%3Fver%3D20120727184134%22%7D%2C%7B%22bizCode%22%3A%22GPRS_FUNCTION_10%22%2C%22bizName%22%3A%22GPRS%E5%A5%97%E9%A4%90%22%2C%22url%22%3A%22%2Fcommodity%2Foptions%2Fdetail%2FGPRS_FUNCTION_10.shtml%22%2C%22icon%22%3A%22%2Fupfile%2Fimages%2Fv2012_cms%2Fproducts%2FGPRS_FUNCTION_10-icon.jpg%3Fver%3D20111202051437%22%7D%2C%7B%22bizCode%22%3A%22GOTONE_BENDI_SUIT_128%22%2C%22bizName%22%3A%22128%E5%85%83%E5%85%A8%E7%90%83%E9%80%9A%E6%9C%AC%E5%9C%B0%E5%A5%97%E9%A4%90%22%2C%22url%22%3A%22%2Fcommodity%2Foptions%2Fdetail%2FGOTONE_BENDI_SUIT_128.shtml%22%2C%22icon%22%3A%22%2Fupfile%2Fimages%2Fv2012_cms%2Fproducts%2FGOTONE_BENDI_SUIT_128-icon.jpg%3Fver%3D20120907173116%22%7D%2C%7B%22bizCode%22%3A%22BENDITAOCAN%22%2C%22bizName%22%3A%22%E6%9C%AC%E5%9C%B0%E5%A5%97%E9%A4%90%22%2C%22url%22%3A%22%2Fcommodity%2Foptions%2Fdetail%2FBENDITAOCAN.shtml%22%2C%22icon%22%3A%22%2Fupfile%2Fimages%2Fv2012_cms%2Fproducts%2FBENDITAOCAN-icon.jpg%3Fver%3D20121016152927%22%7D%2C%7B%22bizCode%22%3A%22GOTONE_BENDI_SUIT_58%22%2C%22bizName%22%3A%2258%E5%85%83%E5%85%A8%E7%90%83%E9%80%9A%E6%9C%AC%E5%9C%B0%E5%A5%97%E9%A4%90%22%2C%22url%22%3A%22%2Fcommodity%2Foptions%2Fdetail%2FGOTONE_BENDI_SUIT_58.shtml%22%2C%22icon%22%3A%22%2Fupfile%2Fimages%2Fv2012_cms%2Fproducts%2FGOTONE_BENDI_SUIT_58-icon.jpg%3Fver%3D20120907173027%22%7D%5D%7D; _t_y_t_b_ip=211.136.253.230; history_phone=PHONE-20121023152242551-44473786%23PHONE-20120210191059830-66531008%23PHONE-20120627090552465-39653729%23PHONE-20120824112506084-11901698%23PHONE-20120627093309180-95545302%23PHONE-20121207095744982-17912584%23PHONE-20121207100431086-23003856%23PHONE-20120823090509563-99810754%23PHONE-20120531165923070-85945134%23PHONE-20121205085554786-68218518%23%23%23PHONE-20121009090536877-59003435%23PHONE-20121023150001120-51673053%23PHONE-20120627100253893-67022074%23PHONE-20111008160709699-60742564%23%23%23%23PHONE-20120808100549512-17021012%23PHONE-20120808094232626-52671075; _a_h_b_c=GZ; JSESSIONID=0000fQu3x9n5WrT0qdorA76vusp:15io2i4og; isopenOnline=0; NGWEBJSESSIONID=0000LBeL7mKp0zj3vlv0GLrOU3S:167e8sdps; mobileip=1; WT_FPC=id=26ec761cf431ddd91961356947919750:lv=1357812436718:ss=1357810750343; CmProvid=gd; __utma=96969631.1585333593.1353738431.1353738431.1355560571.2; __utmz=96969631.1355560571.2.2.utmcsr=g.10086.cn|utmccn=(referral)|utmcmd=referral|utmcct=/g/500230544000/700022091000.html; MM_VERSION=WWW; mobileNo1=b4e5a2d525ff3761ac52cd6a58a671e11243ea4e@@826e466e891b60f4c6ae6cce2cba6ffc750f90f7@@1354606849164; _ca_tk=xss5wzdowsqt3h5vzvwshewlsvjvxc0o; stat_hist=sms.feixin.10086.cn'
#    m = FILTER_PATTERN.search(str)
#    print m
#    print m.groups()[0]

#    saveFilter('2013-01-01', 'WT-FPC=id=21d428fef24e02214941357109960343:lv=1357812436671:ss=1357811736796:fs=1357109960343:pv_Num=11:vt_Num=14; ProductsViewHistory=%7B%22VO%22%3A%5B%7B%22bizCode%22%3A%22GOTONE_BENDI_SUIT_88%22%2C%22bizName%22%3A%2288%E5%85%83%E5%85%A8%E7%90%83%E9%80%9A%E6%9C%AC%E5%9C%B0%E5%A5%97%E9%A4%90%22%2C%22url%22%3A%22%2Fcommodity%2Foptions%2Fdetail%2FGOTONE_BENDI_SUIT_88.shtml%22%2C%22icon%22%3A%22%2Fupfile%2Fimages%2Fv2012_cms%2Fproducts%2FGOTONE_BENDI_SUIT_88-icon.jpg%3Fver%3D20120907172945%22%7D%2C%7B%22bizCode%22%3A%22GOTONE_NEW_ZF_SUIT%22%2C%22bizName%22%3A%22%E6%96%B0%E5%85%A8%E7%90%83%E9%80%9A%E5%95%86%E6%97%85%E3%80%81%E4%B8%8A%E7%BD%91%E5%A5%97%E9%A4%90%E3%80%81%E6%9C%AC%E5%9C%B0%E5%A5%97%E9%A4%90%22%2C%22url%22%3A%22%2Fcommodity%2Foptions%2Fdetail%2FGOTONE_NEW_ZF_SUIT.shtml%22%2C%22icon%22%3A%22%2Fupfile%2Fimages%2Fv2012_cms%2Fproducts%2FGOTONE_NEW_ZF_SUIT-icon.jpg%3Fver%3D20111202065548%22%7D%2C%7B%22bizCode%22%3A%22PushEmail%22%2C%22bizName%22%3A%22139%E9%82%AE%E7%AE%B1%E6%89%8B%E6%9C%BA%E5%AE%A2%E6%88%B7%E7%AB%AF%22%2C%22url%22%3A%22%2Fcommodity%2Foptions%2Fdetail%2FPushEmail.shtml%22%2C%22icon%22%3A%22%2Fupfile%2Fimages%2Fv2012_cms%2Fproducts%2FPushEmail-icon.jpg%3Fver%3D20120727184134%22%7D%2C%7B%22bizCode%22%3A%22GPRS_FUNCTION_10%22%2C%22bizName%22%3A%22GPRS%E5%A5%97%E9%A4%90%22%2C%22url%22%3A%22%2Fcommodity%2Foptions%2Fdetail%2FGPRS_FUNCTION_10.shtml%22%2C%22icon%22%3A%22%2Fupfile%2Fimages%2Fv2012_cms%2Fproducts%2FGPRS_FUNCTION_10-icon.jpg%3Fver%3D20111202051437%22%7D%2C%7B%22bizCode%22%3A%22GOTONE_BENDI_SUIT_128%22%2C%22bizName%22%3A%22128%E5%85%83%E5%85%A8%E7%90%83%E9%80%9A%E6%9C%AC%E5%9C%B0%E5%A5%97%E9%A4%90%22%2C%22url%22%3A%22%2Fcommodity%2Foptions%2Fdetail%2FGOTONE_BENDI_SUIT_128.shtml%22%2C%22icon%22%3A%22%2Fupfile%2Fimages%2Fv2012_cms%2Fproducts%2FGOTONE_BENDI_SUIT_128-icon.jpg%3Fver%3D20120907173116%22%7D%2C%7B%22bizCode%22%3A%22BENDITAOCAN%22%2C%22bizName%22%3A%22%E6%9C%AC%E5%9C%B0%E5%A5%97%E9%A4%90%22%2C%22url%22%3A%22%2Fcommodity%2Foptions%2Fdetail%2FBENDITAOCAN.shtml%22%2C%22icon%22%3A%22%2Fupfile%2Fimages%2Fv2012_cms%2Fproducts%2FBENDITAOCAN-icon.jpg%3Fver%3D20121016152927%22%7D%2C%7B%22bizCode%22%3A%22GOTONE_BENDI_SUIT_58%22%2C%22bizName%22%3A%2258%E5%85%83%E5%85%A8%E7%90%83%E9%80%9A%E6%9C%AC%E5%9C%B0%E5%A5%97%E9%A4%90%22%2C%22url%22%3A%22%2Fcommodity%2Foptions%2Fdetail%2FGOTONE_BENDI_SUIT_58.shtml%22%2C%22icon%22%3A%22%2Fupfile%2Fimages%2Fv2012_cms%2Fproducts%2FGOTONE_BENDI_SUIT_58-icon.jpg%3Fver%3D20120907173027%22%7D%5D%7D; _t_y_t_b_ip=211.136.253.230; history_phone=PHONE-20121023152242551-44473786%23PHONE-20120210191059830-66531008%23PHONE-20120627090552465-39653729%23PHONE-20120824112506084-11901698%23PHONE-20120627093309180-95545302%23PHONE-20121207095744982-17912584%23PHONE-20121207100431086-23003856%23PHONE-20120823090509563-99810754%23PHONE-20120531165923070-85945134%23PHONE-20121205085554786-68218518%23%23%23PHONE-20121009090536877-59003435%23PHONE-20121023150001120-51673053%23PHONE-20120627100253893-67022074%23PHONE-20111008160709699-60742564%23%23%23%23PHONE-20120808100549512-17021012%23PHONE-20120808094232626-52671075; _a_h_b_c=GZ; JSESSIONID=0000fQu3x9n5WrT0qdorA76vusp:15io2i4og; isopenOnline=0; NGWEBJSESSIONID=0000LBeL7mKp0zj3vlv0GLrOU3S:167e8sdps; mobileip=1; WT_FPC=id=26ec761cf431ddd91961356947919750:lv=1357812436718:ss=1357810750343; CmProvid=gd; __utma=96969631.1585333593.1353738431.1353738431.1355560571.2; __utmz=96969631.1355560571.2.2.utmcsr=g.10086.cn|utmccn=(referral)|utmcmd=referral|utmcct=/g/500230544000/700022091000.html; MM_VERSION=WWW; mobileNo1=b4e5a2d525ff3761ac52cd6a58a671e11243ea4e@@826e466e891b60f4c6ae6cce2cba6ffc750f90f7@@1354606849164; _ca_tk=xss5wzdowsqt3h5vzvwshewlsvjvxc0o; stat_hist=sms.feixin.10086.cn', 23)
#    saveFilter('2013-01-10', 'http://m.baidu.com/bd_page_type=1/pu=usm%402%2Csz%401321%5F2003%2Cta%40utouch%5F1%5F6.0%5F1%5F8.4/uid=97AED28F342F1CF7C035134CD30D9A9F/t=wap/w=0_10_%E4%B8%AD%E5%9B%BD%E7%A7%BB%E5%8A%A8%E5%B9%BF%E5%B7%9E/ssid=0/from=2001a/l=0/tc?pn=15&m=0&src=gd%2E10086%2Ecn%2Fgzdh', 100)
    
    FILE_TYPE_FWDHLOG = re.compile(r'fwdh_logs')
    
    files = filesearch.search("*", 'F:/fwdhlogs/')
    for f in files:
        if FILE_TYPE_FWDHLOG.search(f) is not None:
            readAppLog(f)
