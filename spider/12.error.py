import urllib.request

# url = "https://blog.csdn.net/weixin_53072519/article/details/1308727101"
url = "https://www.auisdgui.com"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57X-Requested-With: XMLHttpRequest'}


try:
  request = urllib.request.Request(url =url ,headers =headers)

  response = urllib.request.urlopen(request)

  content = response.read().decode("utf-8")

  print(content)

except urllib.error.HTTPError:
     print("错误")

except urllib.error.URLError:
    print("肯定错误啊 ")