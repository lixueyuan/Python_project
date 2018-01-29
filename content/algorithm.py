import urllib.parse
import urllib
import json
import urllib.request
data_info={}
data_info['type']='AUTO'
data_info['doctype']='json'
data_info['xmlVersion']='1.6'
data_info['ue']='UTF-8'
data_info['typoResult']='true'
data_info=urllib.parse.urlencode(data_info).encode('utf-8')

for x in range(0,195):
    url='http://capi.douyucdn.cn/api/v1/getVerticalRoom?aid=ios&client_sys=ios&limit=20&offset='+str(x)
    print(data_info)
    requ=urllib.request.Request(url,data_info)
    requ.add_header('Referer','http://capi.douyucdn.cn')
    requ.add_header('User-Agent','DYZB/2.271 (iphone; iOS 9.3.2; Scale/3.00)')
    response=urllib.request.urlopen(requ)
    print(response)
    html=response.read().decode('utf-8')
    dictionary=json.loads(html)
    data_arr=dictionary["data"]
    for i in range(0,19):
        name=data_arr[i]["nickname"]
        img_url=data_arr[i]["vertical_src"]
        print(type(img_url))
        respon_tem=urllib.request.urlopen(img_url)
        anchor_img=respon_tem.read()
        with open('../photos/'+name+'.jpg','wb') as f:
            f.write(anchor_img)
