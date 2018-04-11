import csv
import time
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

with open("allitems.csv", 'rb') as csvfile:
    data = csv.reader(csvfile)
    for i in range(10):
        data.next()
    for each in data:
        print each
        time.sleep(3)
