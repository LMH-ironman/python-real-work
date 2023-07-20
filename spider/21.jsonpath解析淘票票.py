import urllib.request
import json
import jsonpath
url = 'https://dianying.taobao.com/cityAction.json?city=110100&_ksTS=1689863980933_19&jsoncallback=jsonp20&action=cityAction&n_s=new&event_submit_doLocate=true'

headers = {
'Accept':'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
'Accept-Language':'zh-CN,zh;q=0.9',
'Cookie':'_samesite_flag_=true; cookie2=1ef75c476f91010b087c064a98d2c0a9; t=694bee70c86f3e2d11b359740a56c9a5; _tb_token_=be30edfbede7; v=0; cna=ozNAHb/JlHkCAXzwCbkSqFs+; xlly_s=1; tb_city=110100; tb_cityName="sbG+qQ=="; isg=BNXVBC0AHa2EGjnRgbY57Obr5NGP0onkLVpOkVd6I8ybrvagHyMVtJkveLIYqaGc; l=fBM3saK4N3yQvyk5BO5ahurza779eIRf11PzaNbMiIEGa1-dTFsoONC15eSX7dtjgTCX7etrip0J_dUD89UdNxDDBevjisVsXxvtaQtJe; tfstk=cNPFBOOGa6CekYURDfcz7BTMAhodaNNuG93-KGldEwBMbGMK0sAJ2VD8tkEy73Dh.',
'Referer':'https://dianying.taobao.com/index.htm?spm=a1z21.3046609.city.1.468a112apvjp5O&n_s=new&city=110100',
'Sec-Ch-Ua':'"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
'Sec-Ch-Ua-Mobile':'?0',
'Sec-Ch-Ua-Platform':'"Windows"',
'Sec-Fetch-Dest':'empty',
'Sec-Fetch-Mode':'cors',
'Sec-Fetch-Site':'same-origin',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
'X-Requested-With':'XMLHttpRequest'

}


request = urllib.request.Request(url = url ,headers = headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

content = content.split('(')[1].split(')')[0]

with open('21.jsonpath解析淘票票.json','w',encoding='utf-8') as f:
    f.write(content)

obj = json.load( open('21.jsonpath解析淘票票.json', 'r', encoding='utf-8'))

citylist =  jsonpath.jsonpath(obj,'$..name')

print(citylist[0])
