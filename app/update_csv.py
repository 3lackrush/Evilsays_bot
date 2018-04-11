#!/usr/bin/env python
# coding:utf-8
__author__ = 'Kios <root@mkernel.com>'
__desc__ = 'Telegram Bot: Evilsays_bot | update csv file'
__link__ = 'http://cve.mitre.org/data/downloads/index.html'

import requests
from config.config import update_check_url, update_download_url
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from lxml import html
from db import CVESQL

class Updator(object):

    def __init__(self):
        self.url = update_check_url
        self.downloadLink = update_download_url

    def getUpdateDate(self):
        r = requests.get(self.url)
        html_data = r.content
        html_tree = html.fromstring(html_data)
        result = html_tree.xpath('//*[@id="CenterPane"]/div[1]')
        data = (result[0].text.split(":")[1]).split("\n")[1]
        return data

    def checkUpdated(self):
        try:
            cve_web_data = self.getUpdateDate()
            obj = CVESQL()
            sql = "SELECT * from cve_update"
            args = ()
            res = obj.getbysql(sql, args)
            db_date = res[0][0]
            if db_date != cve_web_data:
                return False
            else:
                return True
        except Exception as e:
            return False

    def downloadNewCsv(self):
        r = requests.get(self.downloadLink, stream=True)
        with open('./data/newCsv.csv', 'wb') as fd:
            for chunk in r.iter_content(chunk_size = 1024*100):
                fd.write(chunk)
        fd.close()

if __name__ == '__main__':
    obj = Updator()
    print obj.getUpdateDate()
    #print obj.checkUpdated()
    #obj.downloadNewCsv()
