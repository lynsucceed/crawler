#python  Web Crawler
import requests
import bs4
from bs4 import BeautifulSoup

def getHTMLText(url):
    try:
        r = requests.get(url,timeout = 30)     #获取网页
        r.raise_for_status()                   #获取异常信息
        r.encoding = r.apparent_encoding       #编码转换
        return r.text
    except:
        return ""

def printHTMLScript(html):
    soup = BeautifulSoup(html,"html.parser")
    print(soup.prettify())

def findHTMLScript(html,tag):
    soup = BeautifulSoup(html,"html.parser")
    print(soup.find_all(tag))



def main():
    url = input("请输入要抓取的网址URL:\n")
    html=getHTMLText(url)
    printHTMLScript(html)
    tag= input("请输入要抓取的Html标签:\n")
    findHTMLScript(html,tag)

main()
    
  
