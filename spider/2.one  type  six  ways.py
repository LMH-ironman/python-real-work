import urllib.request

url = 'https://www.baidu.com/s?wd='

#类型
#print(type(response))

#获取一句
#content = response.readlines()
#print(content)

#返回状态码
#print(response.getcode())

#获取url地址
#print(response.geturl())

#获取是一个状态信息
#print(response.getheaders())

#综上，一个类型  HTTPRsponse
#六个方法 read readline readlines getcode  geturl  getheaders

import urllib.parse
name = urllib.parse.quote('周杰伦'
                )
url = url + name
print(url)