from bs4 import BeautifulSoup as bs
from selenium import webdriver
import datetime

browser = webdriver.Chrome('.\chromedriver_win32\chromedriver.exe')
browser.get("http://eclass2.hufs.ac.kr:8181/ilos/main/member/login_form.acl")

id = browser.find_element_by_id("usr_id")
id.send_keys("201600786")

pw = browser.find_element_by_id("usr_pwd")
pw.send_keys("")

login_bt=browser.find_element_by_class_name('btntype')
login_bt.click()



# 과제 가져오기

# 각 날짜 클릭
temp = 1
for tr in range(1, 6):
    for td in range(1, 8):
        date_click = browser.find_element_by_xpath('//*[@id="schedule"]/div[2]/table/tbody/tr[' + str(tr) +']/td[' + str(td) + ']')
        now_date = int(date_click.text)
        if now_date != temp:
            continue
        if now_date == temp:
            date_click.click()
            # time.sleep(1)
            main_page = browser.page_source
            parse = bs(main_page, 'html.parser')
            divs = parse.find('div', {'class': 'schedule_txt_view'})
            try:
                hw_tags = divs.findAll('a')
                hw_tag = None
                for i in hw_tags:
                    hw_tag = (i.text.splitlines())
                if hw_tag == None:
                    del hw_tag
                else:               # 과목, 제목, 마감일 자르기 해야됨
                    pass

                # text_list = []
                # div_text = divs.find('div').text.splitlines()
                # for i in div_text:
                #     if "[과제]" in text_list or i.strip() =="[과제]":
                #          text_list.append(i.strip())
                # if len(text_list) == 0:
                #     del text_list
                #
                # now = datetime.datetime.now()
                # nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
                # print(text_list)
            except:
                pass

        if now_date < temp:
            break
        temp += 1

# month = "9"
# date_list = []
# for i in range(1, 32):
#     date_list.append(month + "_" + str(i))

# hw_list = []
# for i in date_list:
#     find_div = parse.find("td", {"class" : "getMainSchedule(''," + i + ")"})
#     print(find_div)




# hw_list = parse.findAll("div", {"class" : "schedule-show-control"})
# print(hw_list)




