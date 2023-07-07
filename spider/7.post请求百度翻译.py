import urllib.request
import urllib.parse
import json
url = 'https://fanyi.baidu.com/sug'
headers ={'User-Agent'
        : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.78'}
data = {'kw':'spider'}
#post请求的参数必须使用编码
data = urllib.parse.urlencode(data).encode('utf-8')
request = urllib.request.Request(url=url,data=data,headers=headers)

response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(type(content))
obj = json.loads(content)
print(obj)