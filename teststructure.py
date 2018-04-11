from app.searchCVE import searchByCVE
from app.shodanModule import BotShodan

if __name__ == '__main__':
    # cve = "cve-1999-1010"
    # res = searchByCVE(cve)
    # print len(res), type(res), res

    obj = BotShodan()
    # result, status = obj.searchByService('apache')
    # print result
    result, status = obj.searchByHost('207.246.103.184')
    print result, status