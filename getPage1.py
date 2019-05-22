import pandas as pd
from lxml import etree
import requests
temp = []
def main():
    for i in range(1):
        result = requests.get("https://www.arena.taipei/News.aspx?n=4A7BFF61FA074F0F&sms=F9A95D3F5A5C2C68&page=%s&PageSize=20" %str(i))
        result.encoding = 'utf-8'
        row = parseTable(result)
        print(row)
def parseTable(result):
    root = etree.fromstring(result.content, etree.HTMLParser())
    row = root.xpath("//td[@class='CCMS_jGridView_td_Class_1']/span/a/text()")
    temp = []
    for i in row:
        if '2018/' in str(i):
            temp.append(str(i))
    return temp


    # return row


if __name__ == "__main__":
    main()