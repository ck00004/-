not_found = 0
global i
global mid
global nid
global aid
global not_found
while nid <= mid:
    if not_found==0:
        not_found = 1
        username = '051916747627'
        passwd = '320481'
        cmd_str = "rasdial" + " " + "宽带连接" + " " + username + " " + passwd
        not_found = os.system(cmd_str)
        i = 0
    else:
        if mysqldb == 0:
            upsql1 = pymysql.Connect(host='115.159.42.53',port=3306,user='azxc',passwd='ww19970901ww',db='bilibili',charset='utf8') #连接到mysql服务器
            cursor1 = upsql1.cursor() #创建游标
            mysqldb = 1
        while i <= 199:
            aid = nid
            payload = {'mid':aid}
            nid+=1 
            sqldate = mysql123(payload)
            sqlstr = 'INSERT INTO user (mid, name, sex, face, coins, regtime, spacesta, birthday, place, description,article, fans, friend, attention, sign, attentions, level, exp,viptype,vipstatus)VALUES ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")'
            cursor1.execute(sqlstr % sqldate)
            upsql1.commit()
            i = i + 1
            cmd_del = 'rasdial'+' '+'宽带连接'+' '+'/disconnect'
            os.system(cmd_del)
            not_found = 0
        else:
            not_found = 0