import requests
from urllib.parse import quote

def call(keyword, start) :
    encText = quote(keyword)
    url = "https://openapi.naver.com/v1/search/blog?query=" + keyword  # json 결과
    result = requests.get(urlparse(url).geturl(),
                          headers={"X-Naver-Client-Id": "", "X-Naver-Client-Secret": ""})
