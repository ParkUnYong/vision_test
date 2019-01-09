########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Content-Type': 'application/json', ## 제이슨 쓰니까 제이슨임 아니면 바꿔줘야함.
    'Ocp-Apim-Subscription-Key': '{12e457e85bb8497d88333dae3fb8d759}', ## 에저 클라우드에서 이걸 지원해줘서 쓰는것.
}

params = urllib.parse.urlencode({
    # Request parameters
    'visualFeatures': 'Description', ## 디스크립션만 쓸거니까 수정 정확히는 설명서에  visualFeatures 옵션들에 가면 옵션에 대한 설명이 있음.
    ##'details': '{string}',
    'language': 'en',
})

try:
    conn = http.client.HTTPSConnection('koreacentral.api.cognitive.microsoft.com/')
    ## 생성한 컴퓨터 비전의 엔드포인트를 복붙 http는 지우고 
    conn.request("POST", "/vision/v1.0/analyze?%s" 
        % params, {'url':'https://imgnews.pstatic.net/image/139/2019/01/09/0002102547_001_20190109151125138.jpg?type=w647'}, headers)   
        ## 이미지 주소를 복사해서 붙여 넣기.
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()

##except Exception as e:
  ##  print("[Errno {0}] {1}".format(e.errno, e.strerro 