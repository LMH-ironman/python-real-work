import random
import urllib.request
#代理池
proxies_pool = [
                {"http":"222.74.73.202:42055"},
                {"http":"111.3.102.207:30001"},
                {"http":"61.216.185.88:60808"},
                {"http":"223.241.118.26:1133"}
                ]

proxies = random.choice(proxies_pool)


url = "https://www.baidu.com/s?wd=ip"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57X-Requested-With: XMLHttpRequest'}

request = urllib.request.Request(url=url,headers=headers)

handler =urllib.request.ProxyHandler(proxies=proxies)
opener = urllib.request.build_opener(handler)
response = opener.open(request)

content = response.read().decode("utf-8")

with open("daili2.html","w",encoding="utf-8") as  fp:
    fp.write(content)
