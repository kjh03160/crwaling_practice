import urllib.request
import bs4

url = "https://www.naver.com"
html = urllib.request.urlopen(url)

bsOjt = bs4.BeautifulSoup(html, "html.parser")

menu_list = bsOjt.find("ul", {"class" : "an_l"})
li_list = menu_list.findAll("li") # 안에 있는 모든 li 찾음 > 리스트형 반환

for li in li_list:
    a_tag = li.find("a")
    span_tag = a_tag.find("span", {"class" : "an_txt"})
    text = span_tag.text
    print(text)
# print(menu_list)