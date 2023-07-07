import urllib.request
import urllib.parse
import json

url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'

headers  ={'Accept': '*/*',
#Accept-Encoding: gzip, deflate, br
'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
'Acs-Token': '1677574807371_1677593179455_5mL/ntoBEHwaGmWEBe6HMOmtKt5V44fZybyNYyEXcmFuDIMZQ5A9gSYyUk86Fx8Rbgo+ndi9NbVv7ExchqgPGuS8EHAo61MxdSX/I6oW0KtNfXlW0hlpeSUgIR9cJPKBGgfYQYUi0Ympy9TvhOZRaUhBd7eJqLgWiRg1xWjI+86003HRfxLxv/eUcL+e0rhGCvx6vvQSjxFSIwByEGTAVW/jbcDLhYKFSox6GN1Kvk71ZRGItKOi/zrGJtfPkWnBTzfD0Ua1Dnl2UFfbhTqPs8CipiUd58VSmFTiHrJcepBbTkZx3Xa943AQpZMRB6ccGMhK76EWPa7UgIZXqcKBjw==',
'Connection': 'keep-alive',
'Content-Length': '135',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Cookie': 'BIDUPSID=43866FD6A8AEA77B1BD59B401F413539; PSTM=1658469988; BAIDUID=43866FD6A8AEA77BAE2AB08FAEA1AB46:SL=0:NR=10:FG=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; MCITY=-233%3A; BAIDUID_BFESS=43866FD6A8AEA77BAE2AB08FAEA1AB46:SL=0:NR=10:FG=1; BA_HECTOR=a02420202004al2ga58g809u1hvpeep1l; ZFY=E8GE1BdDvbXi6aDCZ8HaRVH6qHyKwqKpzj7nqWPUc6c:C; APPGUIDE_10_0_2=1; BDRCVFR[-BxzrOzUsTb]=mk3SLVN4HKm; BDRCVFR[S4-dAuiWMmn]=diI5f__t7DsfjDdnj0LPjDYg19xuAT; delPer=0; PSINO=5; ariaDefaultTheme=undefined; RT="z=1&dm=baidu.com&si=8ec12683-c883-442c-ab63-9763bb440ac5&ss=leo9y4im&sl=1&tt=1ws&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=2ow&nu=mux7b7en&cl=12aq&ul=ny61&hd=ny6e"; H_PS_PSSID=26350; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1677510320,1677593009; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1677593161; ab_sr=1.0.1_Y2JkYjE2OWVjMjU4Yzk4NjBiZjIwZDFjZDJiNDAxNWVlNjk4NTI1MzNjZjdhZDRiN2M3ZTJjZDcyOWJkOTAwNzIyMmEwOTIxMGZkNjRjNTExYjg0ZWNkOTA5NDYwNTI2MTg0NDBjNzZlOWZiNzg5ZGMxYTgyNjRiNzc0ZWNmMGQxY2YwZjI1ODA0MTYyODRkMzNlY2ZmOTgwN2U0NDY0Nw==',
'Host': 'fanyi.baidu.com',
'Origin':' https://fanyi.baidu.com',
'Referer': 'https://fanyi.baidu.com/',
'sec-ch-ua':' "Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': 'Windows',
'Sec-Fetch-Dest': 'empty',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Site': 'same-origin',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57X-Requested-With: XMLHttpRequest'
                                }

data ={'from': 'en',
'to': 'zh',
'query': 'love',
'transtype': 'realtime',
'simple_means_flag': '3',
'sign': '198772.518981',
'token': '75deef303cf00666e4f929dfad9ab279',
'domain': 'common',}
#post编码且用urlencode
data = urllib.parse.urlencode(data).encode('utf-8')
#请求对象定制
request =urllib.request.Request(url=url,data=data,headers=headers)
response = urllib.request.urlopen(request)
#获取响应的数据
content =response.read().decode('utf-8')

obj = json.loads(content)
print(obj)
