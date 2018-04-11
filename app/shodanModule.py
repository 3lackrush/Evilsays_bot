#!/usr/bin/env python
# coding:utf-8
__author__ = 'Kios <root@mkernel.com>'
__desc__ = 'Telegram Bot: Evilsays_bot | shodan module'

from config.config import shodan_api_key
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import shodan 

class BotShodan:

    def __init__(self):
        self.api = shodan.Shodan(shodan_api_key)

    def searchByService(self, service):
        try:
            results = self.api.search(service)
            returnResult = {}
            tempIpList = []
            for result in results['matches']:
                tempIpList.append(result['ip_str'])
            returnResult['total'] = results['total']
            returnResult['ip'] = tempIpList
            return returnResult, "success"
        except shodan.APIError, e:
            return e, "failed"

    def searchByHost(self, host):
        try:
            host = self.api.host(host)
            returnResult = {}
            returnResult['ip'] = host['ip_str']
            returnResult['org'] = host.get('org', 'n/a')
            returnResult['os'] = host.get('os', 'n/a')
            
            serviceTemp = []
            for item in host['data']:
                serviceTemp.append("""
                            Port: %s
                            Banner: %s
                """ % (item['port'], item['data']))
            returnResult['service'] = serviceTemp
            return returnResult, "success"
        except shodan.APIError, e:
            return e, "failed"
         