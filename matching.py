# -*- coding: <encoding name> -*- 
import pymysql

conn=pymysql.connect('localhost','root','password')
conn.select_db('logger')
cur=conn.cursor()
cur.execute("select ip, request_url,status_code from  logger_watcher_2021_05_03_09;")
print("==========开始匹配============")
while 1:
    res=cur.fetchone()
    if res is None:
        break
    print (res[2],res[0],res[1])
cur.close()
conn.commit()
conn.close()
