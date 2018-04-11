#!/usr/bin/env python
# coding:utf-8
__author__ = 'Kios <root@mkernel.com>'
__desc__ = 'Telegram Bot: Evilsays_bot | CVE data parse'

import csv
from db import CVESQL

dbclass = CVESQL()
sql = "INSERT INTO `cve`.`cve_details`(`name`, `status`, `description`, `references`, `phase`, `votes`, `comments`) VALUES (%s, %s, %s, %s, %s, %s, %s);"

with open('./data/newCsv.csv', 'rb') as csvfile:
    data = csv.reader(csvfile)
    for i in range(10):
        data.next()
    for item in data:
        try:
            cve_number = item[0]
            status = item[1]
            description = item[2]
            reference = "\n".join([each.strip() for each in item[3].split("|")])
            phase = item[4]
            votes = item[5]
            comments = " ".join([each.strip() for each in item[6].split("|")])
            args = (cve_number, status, description, reference, phase, votes, comments,)

            dbclass.insertbysql(sql, args)
        except Exception as e:
            print "[*] Error encountered! >>>" , str(e)
