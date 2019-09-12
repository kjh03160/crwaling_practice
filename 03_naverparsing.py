import urllib.request
import bs4

url = "https://www.naver.com"
html = urllib.request.urlopen(url)

bsObj = bs4.BeautifulSoup(html, "html.parser")
top_right_content = bsObj.find("div", {"class" : "area_links"})

first_a = top_right_content.find("a")

print(first_a.text)
# print(bsObj)