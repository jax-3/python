import requests
import re
def getHtmlText(url):
    headers={
             'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3861.400 QQBrowser/10.7.4313.400'
            }
    try:
        r=requests.get(uel,headers=headers)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return"异常1"
def parsePage(html):
    try:
        plt=re.findall(r'<em>￥</em><i>(.*)</i>',html)
        return plt
    except:
        print("异常2")
def printGoodsList(ilt):
    tplt="{:8}\t{:8}"
    print(tplt.format("序号","价格"))
    count=0
    for i in ilt:
        count+=1
        print(tplt.format(count,i[0]))
def main():
    url='https://search.jd.com/Search?keyword=书包&qrst=1&stock=1&page=3&s=56&click=0'
    ##infoList=[]
    try:
        html=getHtmlText(url)
        plt=parsePage(html)
    except:
           print("异常3")
    printGoodsList(plt)
    
main()
            
            
            
