import urllib.request
from bs4 import BeautifulSoup
import time

class Stock:

    def __init__(self, company_code):
        url = "https://finance.naver.com/item/main.nhn?code=" + company_code
        html = urllib.request.urlopen(url)
        self.bs_obj = BeautifulSoup(html, "html.parser")


    def get_name(self):

        # 주식 이름
        name_tag = self.bs_obj.find("div", {"class" : "wrap_company"})
        name = name_tag.find("a").text
        return name

    def get_close(self):
        # bs_obj = self.bs_obj(company_code)
        # 종가
        close = self.bs_obj.find("td", {"class" : "first"})
        no_close = close.find("span", {"class" : "blind"}).text
        return no_close

    def get_now(self):
        # bs_obj = self.bs_obj(company_code)
        # 현재가
        no_today = self.bs_obj.find("p", {"class" : "no_today"})
        blind = no_today.find("span", {"class" : "blind"})
        return blind.text

    def get_high(self):
        # bs_obj = self.bs_obj(company_code)
        # 고가
        high = self.bs_obj.findAll("td")[1]
        high_price = high.find("span", {"class" : "blind"}).text
        return high_price

    def get_cmprice(self):
        # bs_obj = self.bs_obj(company_code)
        # 시가
        price = self.bs_obj.findAll("tr")[1]
        price_ = price.find("td", {"class" : "first"})
        price__= price_.find("span", {"class" : "blind"}).text
        return price__

    def get_low(self):
        # bs_obj = self.bs_obj(company_code)
        # 저가
        low = self.bs_obj.findAll("tr")[1].findAll("td")[1]
        low_price = low.find("span", {"class" : "blind"}).text
        # lowest = low_price.find("span", {"class" : ""})
        return low_price

    def get_rate(self):
        # bs_obj = self.bs_obj(company_code)
        # 등락률
        try:
            list1 = self.bs_obj.findAll("em", {"class" : "no_down"})
            rate_list = list1[2].findAll("span")
            text_list = []
            for text in rate_list:
                text_list.append(text.text)
            result = str(text_list[0]) + str(text_list[1]) + text_list[-1]
        except:
            list1 = self.bs_obj.findAll("em", {"class": "no_up"})
            rate_list = list1[2].findAll("span")
            text_list = []
            for text in rate_list:
                text_list.append(text.text)
            result = str(text_list[0]) + str(text_list[1]) + text_list[-1]
        return result
        # return {"종목" : name, "현재가" : blind.text , "종가" : no_close, "고가" : high_price, "시가" : price__, "저가" : low_price}


request_list = list(input("검색할 종목의 번호를 적어주세요 (띄어쓰기로 구분) : ").split())
set_time = int(input("몇 초마다 갱신하시겠습니까? "))

while True:
    for company_code in request_list:
        member = Stock(company_code)
    # company_code = "078070"
        print("종목: %s\n 현재가 : %s(%s) 종가 : %s\n 시가 : %s 고가 : %s 저가 : %s\n"
              % (member.get_name(), member.get_now(), member.get_rate(),
              member.get_close(), member.get_cmprice(), member.get_high(), member.get_low()))
    time.sleep(set_time)


# 068270 005930