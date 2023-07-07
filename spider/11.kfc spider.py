import urllib.request
import urllib.parse


def create_request(page):
    base_url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname"

    data ={
        "cname": "韶关",
        "pid":"",
        "pageIndex": page,
        "pageSize": "10"
         }

    data = urllib.parse.urlencode(data).encode("utf-8")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57X-Requested-With: XMLHttpRequest'}
    request = urllib.request.Request(url=base_url, headers=headers,data = data)
    return request

def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode("utf-8")
    return content

def down_load(page,content):
    fp = open("kfc" + str(page) + ".json", "w", encoding="utf-8")
    fp.write(content)


if __name__ == "__main__":
    start_page = int(input("请输入页码"))
    end_page = int(input("最终页码"))

    for page in range(start_page,end_page+1):
        request = create_request(page)
        content = get_content(request)
        down_load(page, content)