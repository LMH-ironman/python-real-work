import urllib.request
from lxml import etree


# url1 = "https://699pic.com/zhuanti/xiariyongzhuangmeinv.html"
# url2 = "https://699pic.com/zhuanti/xiariyongzhuangmeinv-2/"

def create_request(page):
    if (page == 1):
        url = "https://699pic.com/zhuanti/xiariyongzhuangmeinv.html"
    else:
        url = "https://699pic.com/zhuanti/xiariyongzhuangmeinv-" + str(page) + "/"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57X-Requested-With: XMLHttpRequest'}

    request = urllib.request.Request(url=url, headers=headers)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def down_load(content):
    # urllib.request.urlretrieve()
    tree = etree.HTML(content)
    name_list = tree.xpath('//div[@class="photo-tag"]//a/@title')
    src_list = tree.xpath('//li[@class="list"]//a/img/@data-original')

    for i in range(len(src_list)):
        name = name_list[i]
        src = src_list[i]
        url = 'https:' + src
        urllib.request.urlretrieve(url=url, filename='D:\python real  work\swimming img/' + name + '.jpg')


if __name__ == '__main__':
    start_page = int(input('请输入起始页码'))
    end_page = int(input('请输入结束页码'))

    for page in range(start_page, end_page + 1):
        request = create_request(page)
        content = get_content(request)
        down_load(content)
