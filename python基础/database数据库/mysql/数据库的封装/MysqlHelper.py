#coding=utf-8
from pymysql import *


class MysqlHelper:

    def __init__(self,host,port,db,user,password,charset):
        self.host = host
        self.port = port
        self.db = db
        self.user = user
        self.password = password
        self.charset = charset

    def open(self):
        try:
            self.conn = connect(host=self.host,port = self.port,db=self.db,user=self.user,password=self.password,charset=self.charset)
            self.cursor =self.conn.cursor()
        except Exception as e:
            print(e)
            print("打开数据库失败")


    def close(self):
        self.cursor.close()
        self.conn.close()

    def cud(self,sql):
         try:
            self.open()
            self.cursor.execute(sql)
            self.conn.commit()
            self.close()
            print("execute is ok")
         except Exception as  e:
             self.conn.rollback()
             print(e)

    def queryAll(self,sql,params):
         try:
             self.open()
             self.cursor.execute(sql,params)
             result = self.cursor.fetchall()
             self.close()
             return result
         except Exception as e:
             print(e)
             return None
