import urllib.request
import bs4

url = "https://news.naver.com"
html = urllib.request.urlopen(url)

bsOjt = bs4.BeautifulSoup(html,"html.parser")
healine_news = bsOjt.find("ul", {"class" : "hdline_article_list"})
titles = healine_news.findAll("div", {'class' : "hdline_article_tit"})

today_news_titles = []
for div in titles:
    a_tag = div.find("a")
    title_text = a_tag.text.strip()
    today_news_titles.append(title_text)

for i in today_news_titles:
    print("오늘의 기사는 " + i)
