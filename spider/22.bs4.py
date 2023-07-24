from bs4 import BeautifulSoup

soup = BeautifulSoup(open('22.bs4.html',encoding='utf-8'),'lxml')

# #找到是第一个符合条件的数据
# print(soup.a)
# #返回的是标签的属性和属性值
# print(soup.a.attrs)

# find
# 返回的是第一个条件的数据,也可以根据附加条件找到对应的标签对象
# print(soup.find('a', title ="a2"))

# find_all 返回所有的a标签
# print(soup.find_all('a'))
# find_all 获取多个标签
# print(soup.find_all(['a','span']))
# 找前几个的数据
# print(soup.find_all('li',limit=2))

# select返回的是一个列表 并且会返回多个数据
# print(soup.select('a'))

# 可以通过.代表class 我们把这种操作叫做类选择器
# print(soup.select('.a1'))
# 可以通过#代表id
# print(soup.select('#l1'))
# 找到li标签中有id的标签
# print(soup.select('li[id]'))
# 找到li标签中id为l2的标签
# print(soup.select('li[id="l2"]'))

# 层级选择器
# 后代选择器
# 找到的师div下面的li
# print(soup.select('div li'))
# 子代选择器
# print(soup.select('div > ul > li'))

# 找到a标签和li标签的所有的对象
# print(soup.select('a,li'))

# 节点信息
# 获取节点内容get_text()
# obj = soup.select('#d1')[0]
# print(obj.get_text())

# 节点的属性
# obj = soup.select('#p1')[0]
# name是标签的名字
# print(obj.name)
# 将属性值作为一个字典返回
# print(obj.attrs)

# 获取节点的属性
# obj = soup.select('#p1')[0]
# print(obj.attrs.get('class'))