from  lxml import etree

##本地文件   etree.parse
##服务器响应的数据 response.read().decode("utf-8")  etree.HTML()


tree  = etree.parse("D:\\python real  work\\spider\\17.xpath.html")
#查找ul下面的li
li_list =  tree.xpath("//ul/li")

#查找所有id的属性的li标签
#text()获取标签中的内容
li_list1 =  tree.xpath("//ul/li[@id]/text()")

##找到idl1的li标签
li_list2 =  tree.xpath('//ul/li[@id= "l1"]/text()')

##找到idl1的li标签的class的属性值
li_list3 = tree.xpath('//ul/li[@id= "l1"]/@class')

##模糊查询，查询id中包含l的li标签
li_list4 = tree.xpath('//ul/li[contains(@id,"l")]/text()')

##查询id的值以l开头的li标签
li_list5 = tree.xpath('//ul/li[starts-with(@id,"c")]/text()')

##查询id为l1和class为c1的
li_list6 = tree.xpath('//ul/li[@id = "l1" and @class = "c1"]/text()')

##或运算
li_list7 = tree.xpath('//ul/li[@id = "l1" ]/text()|  //ul/li[@id = "l2" ]/text()')
# print(li_list,li_list1)
# print(len(li_list),len(li_list1))
# print(li_list2)
# # print(len(li_list2))
# print(li_list3)
# print(len(li_list3))
# print(li_list4)
# print(len(li_list4))
# print(li_list5)
# print(len(li_list5))
# print(li_list6)
# print(len(li_list6))
print(li_list7)
print(len(li_list7))