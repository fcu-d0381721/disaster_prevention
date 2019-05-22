import pandas as pd
from lxml import etree
import requests
temp = []


def main():
    result = requests.get("https://www.gov.taipei/ActivityTheme3.aspx?n=9EBB37CB9D211D44&sms=33891424602B0C38#")
    result.encoding = 'utf-8'
    parseTable(result)


def parseTable(result):
    root = etree.fromstring(result.content, etree.HTMLParser())
    row = root.xpath("//div[@class='group base-content']//div[@class='table']/@id")
    print(row)

if __name__ == "__main__":
    main()