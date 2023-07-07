import urllib.request
import urllib.parse
url = 'https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6'

headers ={'User-Agent'
        : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.78'}
request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(url)
content = response.read().decode('utf-8')
print(content)