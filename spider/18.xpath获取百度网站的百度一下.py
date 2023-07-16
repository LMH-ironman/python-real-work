import urllib.request
from lxml import etree
url = "https://www.baidu.com/"


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57X-Requested-With: XMLHttpRequest'
}

request = urllib.request.Request(url = url , headers = headers)
response = urllib.request.urlopen(request)
content = response.read().decode("utf-8")

tree = etree.HTML(content)
##xpath是一个列表类型的数据
result = tree.xpath('//input[@id="su"]/@value')[0]
print(result)