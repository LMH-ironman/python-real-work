import json
import jsonpath

obj = json.load(open('D:\python real  work\spider\jsonpath.json', 'r', encoding='utf-8'))

# list = jsonpath.jsonpath(obj,'$.store.book[*].author')
# print(list)

# list = jsonpath.jsonpath(obj,'$..author')
# print(list)

# tag_list = jsonpath.jsonpath(obj,'$.store.*')
# print(tag_list)

# price_list = jsonpath.jsonpath(obj,'$.store..price')
# print(price_list)

# book = jsonpath.jsonpath(obj , '$..book[(@.length-1)]')
# print(book)

# book = jsonpath.jsonpath(obj , '$..book[:2]')
# print(book)

# book = jsonpath.jsonpath(obj , '$..book[?(@.isbn)]')
# print(book)

book = jsonpath.jsonpath(obj , '$..book[?(@.price>10)]')
print(book)