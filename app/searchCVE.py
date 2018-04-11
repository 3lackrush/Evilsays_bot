#!/usr/bin/env python
# coding:utf-8
__author__ = 'Kios <root@mkernel.com>'
__desc__ = 'Telegram Bot: Evilsays_bot | seaching cve Module'

from db import CVESQL

def searchByCVE(cve_number):
    obj1 = CVESQL()
    sql = "SELECT * from `cve`.`cve_details` where `name`=%s"
    args = (cve_number.upper(),)
    res = obj1.getbysql(sql, args)
    return res

if __name__ == '__main__':
    cve = "cve-1999-1010"
    res = searchByCVE(cve)
    print len(res), type(res), res
