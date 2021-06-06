import pymysql
import configparser
import re

conn=pymysql.connect('localhost','root','password')
conn.select_db('logger')
cur=conn.cursor()
table_name = 'logger_watcher_2021_05_03_09'
cf = configparser.ConfigParser()
cf.read(r"config.ini")
ua_rule = cf.get("rule","ua_rule")
method_rule = cf.get("rule","method_rule")
sql_rule = cf.get("rule","sql_rule")

with open("urlinfo.txt","w") as f:
    cur.execute("select ip, request_url,status_code,ua from " + table_name + ";")
    print("====================UA信息开始匹配==================")
    while 1:
        res=cur.fetchone()
        if res is None:
            break
        if re.search(ua_rule,res[3], re.IGNORECASE):
            info = [res[2],res[0],res[1]]
            f.write(str(info)+"\n")


    cur.execute("select ip, request_url,status_code,request_method from   " + table_name + ";")
    print("====================请求方式开始匹配==================")
    while 1:
        res=cur.fetchone()
        if res is None:
            break
        if re.search(method_rule,res[3], re.IGNORECASE) == None:
            print (res[2],res[0],res[1],res[3])
            info = [res[2],res[0],res[1],res[3]]
            f.write(str(info)+"\n")

    cur.execute("select ip, request_url,status_code from  " + table_name + ";")
    print("====================sql注入开始匹配==================")
    while 1:
        res=cur.fetchone()
        if res is None:
            break
        if re.search(sql_rule,res[1], re.IGNORECASE):
            print (res[2],res[0],res[1])
            info = [res[2],res[0],res[1]]
            f.write(str(info)+"\n")

cur.close()
conn.commit()
conn.close()

