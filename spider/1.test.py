# 使用urllib来获取百度首页的源码
import urllib.request
#定义一个url  就是你要访问的地址
url = 'http://www.baidu.com'
#模拟浏览器向服务器发送
response = urllib.request.urlopen(url)
#采集数据
content = response.read().decode('utf-8')
#打印
print(content)