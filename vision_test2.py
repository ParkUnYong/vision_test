import requests
import json


params = {
                'visualFeatures': 'Description',
                'language': 'en'
         }

##https://[location].api.cognitive.microsoft.com/vision/v1.0/analyze[?visualFeatures][&details][&language]
## 이런식으로 옵션 넣어줘야함. 비주얼 퓨처로 
headers = {
    # Request headers
    'Content-Type': 'application/json', ## 제이슨 쓰니까 제이슨임 아니면 바꿔줘야함.
    'Ocp-Apim-Subscription-Key': '12e457e85bb8497d88333dae3fb8d759', ## 에저 클라우드에서 이걸 지원해줘서 쓰는것.
}

data = {
    'url':'http://image.chosun.com/sitedata/image/201804/25/2018042502074_0.jpg'
}

res = requests.post('https://koreacentral.api.cognitive.microsoft.com/vision/v1.0/analyze',
                        params= params, headers=headers, json =data)


res_dic = json.loads(res.text)

#print(res_dic['description'])  디스크립션만
#print(res_dic['description']['captions']) 디스크립션안에 캡션만
#print(res_dic['description']['captions'][0]) 리스트형 파일이니 0번째만
print(res_dic['description']['captions'][0]['text'])  ##그안에 텍스트만.

 