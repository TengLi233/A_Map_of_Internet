from bs4 import BeautifulSoup
import requests
import time
import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')
base_url = "http://www.cidr-report.org/as2.0/autnums.html"
file = '/home/teng/BGP_Data/ASes.csv'


def getHtmlTest(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return " ERROR. "

def storeData(file, text):
    f = open(file, 'w')
    f.write(text)

def get_content(url):
    contents = []
    htmltext = getHtmlTest(url)
    soup = BeautifulSoup(htmltext, "lxml")
    liTags = soup.find_all('a')

    for li in liTags:
        hl = str(li)
        m = re.match(r'([0-9a-zA-Z\<\/\-\?\;\=\"\'\.\>\& ]+)([a-zA-Z]{2}[0-9]+)([ </a>]+)', hl)
        print m.group(2)

def main():
    get_content(base_url)
main()