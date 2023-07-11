import urllib.request

url = "http://www.baidu.com"

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57X-Requested-With: XMLHttpRequest'
}

request = urllib.request.Request(url=url,headers=headers)

handler = urllib.request.HTTPHandler()

opener = urllib.request.build_opener(handler)

response = opener.open(request)

content = response.read().decode("utf-8")

print(content)