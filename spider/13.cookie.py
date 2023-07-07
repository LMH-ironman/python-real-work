import urllib.request

url = "https://weibo.com/u/1669879400"

headers = {
#cookie包含着登录信息
'Cookie' :  'SINAGLOBAL=699079924511.9094.1662288355814; UOR=,,cn.bing.com; XSRF-TOKEN=dX9pB2q46QxU93A_vGI0Uaek; _s_tentry=weibo.com; Apache=3302665952620.2915.1688740098234; ULV=1688740098242:15:4:4:3302665952620.2915.1688740098234:1688474632398; PC_TOKEN=652f6035d8; SSOLoginState=1688740413; SCF=AhEWJrzV3aFz3KD2vBDxpwubtgm4m2kLWJQ2q8YmXfg7AxyZPw28Wi0WSC91PmbImXtZWZHGkLi2r9XlYR6DE9Q.; SUB=_2A25JrFJtDeRhGeFG71QW-CbNwj2IHXVq2MSlrDV8PUNbmtANLXHGkW9NeWagmzowBfbpfL6eL1m9dH35vSeEkvc3; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFOkmkFUi2pw9i5kG4ESdsf5JpX5KzhUgL.FoMRShqN1hnp1K22dJLoIpnLxKqL1-2L1KMLxKqLBonLBK8kSoq4eoBt; ALF=1720276412; WBPSESS=Dt2hbAUaXfkVprjyrAZT_IMLNbl0iEnnvAUTjpMTi5ad6VRdE0A20Qaw2DIkwOne-o6dQUJlUhPQYt--B2ijhENCrragNTOsqZY2a17Wth5mpVtvJtiXU4ivhdoScfiTU_6iONwebPmgSGpOOjLWD5TzBbWOL3dRb59XYEGyO7N0RcdGGhb8MHgOxIYhkihKB8IjQ7_KcfJgSHLRgQilDQ==',
'Referer':'https://s.weibo.com/',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57X-Requested-With: XMLHttpRequest',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
}

request = urllib.request.Request(url =url,headers = headers)
response = urllib.request.urlopen(request)
content = response.read().decode("utf-8")

with open("weibo 主页.html","w",encoding ="utf-8")  as fp:
    fp.write(content)