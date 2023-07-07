import urllib.request
import urllib.parse

base_url = 'https://www.baidu.com/s?'
data  = {
    'wd':'周杰伦',
    'sex':'男'
}
newdata = urllib.parse.urlencode(data)
print(newdata)
url = base_url+newdata
headers ={'User-Agent'
        : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.78'}
request = urllib.request.Request(url=url,headers=headers)

response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)