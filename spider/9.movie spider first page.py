import urllib.request
url = "https://movie.douban.com/j/chart/top_list?type=13&interval_id=100%3A90&action=&start=0&limit=20"

headers  = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57X-Requested-With: XMLHttpRequest'}

request = urllib.request.Request(url = url,headers = headers)

response = urllib.request.urlopen(request)
content = response.read().decode("utf-8")

fp = open("douban.json","w",encoding="utf-8")
fp.write(content)