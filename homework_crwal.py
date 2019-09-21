from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time

browser = webdriver.Chrome('.\chromedriver_win32\chromedriver.exe')
browser.get("http://eclass2.hufs.ac.kr:8181/ilos/main/member/login_form.acl")

id = browser.find_element_by_id("usr_id")
id.send_keys("201600786")

pw = browser.find_element_by_id("usr_pwd")
pw.send_keys("hwaitaeng1")

login_bt=browser.find_element_by_class_name('btntype')
login_bt.click()

main_page = browser.page_source

parse = bs(main_page, 'html.parser')

# 과제 가져오기

# 각 날짜 클릭
# tds = parse.findAll("td", {"class" : ""})
temp = 0
# for tr in range(1, 6):
#     for td in range(1, 8):
        # date_click = browser.find_element_by_xpath('//*[@id="schedule"]/div[2]/table/tbody/tr[' + str(tr) +']/td[' + str(td) + ']')
        # now_date = int(date_click.text)
        #
        # if now_date < temp:
        #     break
        # temp = now_date
        # date_click.click()
        # time.sleep(10)

browser.execute_script("getMainSchedule('','2019-9-6');")
time.sleep(3)
date_click = browser.find_element_by_xpath('//*[@id="schedule"]/div[2]/table/tbody/tr[1]/td[6]')
time.sleep(3)
date_click.click()
time.sleep(3)
divs = parse.find('div',{'class' : 'schedule-show-control'})


print(divs)


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




