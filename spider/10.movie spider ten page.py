import urllib.request
import urllib.parse

def create_request(page):
    base_url  =   "https://movie.douban.com/j/chart/top_list?type=13&interval_id=100%3A90&action=&"
    data = {"start":  (page - 1) *20,
            "limit":   20}

    data = urllib.parse.urlencode(data)
    url = base_url + data
    print(url)
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57X-Requested-With: XMLHttpRequest'}
    request = urllib.request.Request(url=url,headers=headers)
    return request

def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode("utf-8")
    return content

def down_load(page,content):
    fp = open("doubanpage" + str(page) + ".json", "w", encoding="utf-8")
    fp.write(content)


if __name__ == "__main__":
   start_page = int(input("起始页码"))
   end_page = int(input("结束页码"))

   for page  in range(start_page,end_page+1):
        request = create_request(page)
        content = get_content(request)
        down_load(page,content)