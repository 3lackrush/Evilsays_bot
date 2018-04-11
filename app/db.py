#!/usr/bin/env python
# coding:utf-8
__author__ = 'Kios <root@mkernel.com>'
__desc__ = 'Telegram Bot: Evilsays_bot | db module'

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import MySQLdb
from config.config import *
from DBUtils.PooledDB import PooledDB

class CVESQL:

    def __init__(self):
        self.host = mysql_host
        self.port = mysql_port
        self.username = mysql_username
        self.password = mysql_password
        self.dbname = mysql_db
        self.chrset = mysql_chrset
        self.conn = PooledDB(MySQLdb, host=self.host, user=self.username, passwd=self.password, db=self.dbname,port=int(self.port), charset=self.chrset).connection()

    def getbysql(self, sql, args):
        '''
                Get by sql
                :param sql:
                :param param:
                :return:
                '''
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, args)
            res = cursor.fetchall()
            cursor.close()
            return res
        except Exception as e:
            print e
            return "None"
        finally:
            cursor.close()


    def insertbysql(self, sql, args):
        '''
        :param sql:
        :param args:
        :return:
        '''

        try:
            cursor = self.conn.cursor()
            #import pdb;pdb.set_trace()
            cursor.execute(sql, args)
            print "Inserting data >>>", args
            self.conn.commit()
        except Exception as e:
            print "Error encountered >>> ", e
        finally:
            cursor.close()


    def __del__(self):
        self.conn.close()

if __name__ == '__main__':
    dbclass = CVESQL()
    sql = "SELECT VERSION()"
    args = ()
    print dbclass.getbysql(sql, args)