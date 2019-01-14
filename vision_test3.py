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
    'url':'https://t1.daumcdn.net/cfile/tistory/22392D3D530B64400B'
    ## 이미지 부분임.
}

res = requests.post('https://koreacentral.api.cognitive.microsoft.com/vision/v1.0/analyze',
                        params= params, headers=headers, json =data)


res_dict = json.loads(res.text)
subscribed_text = res_dict['description']['captions'][0]['text']


params = {
                'api-version': '3.0',
                'language': 'en',
                'to' : 'ko'
         }

##https://[location].api.cognitive.microsoft.com/vision/v1.0/analyze[?visualFeatures][&details][&language]
## 이런식으로 옵션 넣어줘야함. 비주얼 퓨처로 
headers = {
    # Request headers
    'Content-Type': 'application/json', ## 제이슨 쓰니까 제이슨임 아니면 바꿔줘야함.
    'Ocp-Apim-Subscription-Key': 'f8e5d5a65bae409fbe0651bb01d01b87', ## 에저 클라우드에서 이걸 지원해줘서 쓰는것.
}

data = [{
    'text' : subscribed_text
}]

res = requests.post('https://api.cognitive.microsofttranslator.com/translate',
                        params= params, headers=headers, json =data)

res_dict = json.loads(res.text)
result = res_dict[0]['translations'][0]['text']

print(result)

##res_dic = json.loads(res.text)



#print(res_dic['description'])  디스크립션만
#print(res_dic['description']['captions']) 디스크립션안에 캡션만
#print(res_dic['description']['captions'][0]) 리스트형 파일이니 0번째만
##print(res_dic['description']['captions'][0]['text'])  ##그안에 텍스트만.
