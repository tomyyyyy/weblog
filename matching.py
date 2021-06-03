import pymysql
import re

conn=pymysql.connect('localhost','root','password')
conn.select_db('logger')
cur=conn.cursor()
table_name = 'logger_watcher_2021_05_03_09'

with open("urlinfo.txt","w") as f:
    cur.execute("select ip, request_url,status_code,ua from " + table_name + ";")
    print("====================UA信息开始匹配==================")
    while 1:
        res=cur.fetchone()
        if res is None:
            break
        if re.search("baidu|sougou|google|谷歌|360|",res[3], re.IGNORECASE) != None:
            print (res[2],res[0],res[1])
            f.write(res[2],res[0],res[1])


    cur.execute("select ip, request_url,status_code,request_method from   " + table_name + ";")
    print("====================请求方式开始匹配==================")
    while 1:
        res=cur.fetchone()
        if res is None:
            break
        if re.search("GET|POST",res[3], re.IGNORECASE) == None:
            print (res[2],res[0],res[1],res[3])
             f.write(res[2],res[0],res[1],res[3])

    cur.execute("select ip, request_url,status_code from  " + table_name + ";")
    print("====================sql注入开始匹配==================")
    while 1:
        res=cur.fetchone()
        if res is None:
            break
        if re.search("\{*.*?\}|>|<|\||information_schema|select",res[1], re.IGNORECASE) != None:
            print (res[2],res[0],res[1])
             f.write(res[2],res[0],res[1])

cur.close()
conn.commit()
conn.close()

