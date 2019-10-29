from bs4 import BeautifulSoup as bs
from selenium import webdriver
import datetime

id_input = input("학번을 입력하세요 : ")
pw_input = input("비밀번호를 입력하세요 : ")

print("환경 설정 중...")
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")

browser = webdriver.Chrome('.\chromedriver_win32\chromedriver.exe', options=options)
browser.get("http://eclass2.hufs.ac.kr:8181/ilos/main/member/login_form.acl")

id = browser.find_element_by_id("usr_id")
id.send_keys(id_input)                     # 아이디

pw = browser.find_element_by_id("usr_pwd")
pw.send_keys(pw_input)                     # 비밀번호

login_bt=browser.find_element_by_class_name('btntype')
login_bt.click()
print("로그인 완료")



# 과제 가져오기

# 각 날짜 클릭
temp = datetime.datetime.now().day
result = []
print("과제 정보를 가져오고 있습니다. 잠시만 기다려 주세요.\n")

now_day = datetime.datetime.now().day
now_month = datetime.datetime.now().month

day_30 = [4, 6, 9, 11]
day_31 = [1, 3, 5, 7, 8, 10, 12]


for i in range(1, 15):
    now_div = browser.find_element_by_id(str(now_month) + '_' + str(now_day))
    now_div.click()
    main = browser.page_source
    parse = bs(main, 'html.parser')

    try:
        divs = parse.find('div', {'class': 'schedule_txt_view'})
        sorting = divs.findAll('div')
        for i in sorting:
            refer_text = i.find('div',{'class' : 'schedule-show-control'}).find("div").text
            if "과제" in refer_text or "개인" in refer_text:
                title = None
                if "과제" in refer_text:
                    title = "[과제]"
                else:
                    title = "[개인]"
                hw_tags = i.find('div', {"class" : "changeDetile schedule-Detail-Box"})
                striped_ = []
                hw_tag = hw_tags.text.splitlines()

                for i in hw_tag:
                    if len(i.strip()) == 0 or len(i) == 0:
                        pass
                    else:
                        striped_.append(i.strip())
                now = datetime.datetime.now()
                nowDatetime = now.strftime('%Y.%m.%d %H:%M:%S')
                due_date = None
                if '지각' in striped_[-1]:
                    due_date = striped_[-2][6:]
                elif "마감일" in striped_[-1] or "Due Date" in striped_[-1]:
                    due_date = striped_[-1][6:]
                else:
                    if len(str(now_day)) == 1:
                        due_date = nowDatetime[:7] + ".0" + str(now_day)
                    else:
                        due_date = nowDatetime[:7] + "." + str(now_day)
                    striped_.append("마감일 : " + due_date)

                if len(striped_) == 0 or nowDatetime > due_date:
                    del striped_
                else:
                    striped_.insert(0, title)
                    result.append(striped_)

    except:
        pass
    now_day += 1
    if now_month in day_30 and now_day > 30:
        now_day = 1
        now_month += 1
    elif now_month in day_31 and now_day > 31:
        now_day = 1
        now_month += 1

if len(result) == 0:
    print("과제가 없습니다.")
else:
    for i in result:
        for j in i:
            print(j)
        print()





# try:
#     for tr in range(1, 7):
#         for td in range(1, 8):
#             date_click = browser.find_element_by_xpath('//*[@id="schedule"]/div[2]/table/tbody/tr[' + str(tr) +']/td[' + str(td) + ']')
#             now_date = int(date_click.text)
#             if now_date != temp:
#                 continue
#             if now_date == temp:
#                 date_click.click()
#                 main_page = browser.page_source
#                 parse = bs(main_page, 'html.parser')
#
#                 try:
#                     divs = parse.find('div', {'class': 'schedule_txt_view'})
#                     sorting = divs.findAll('div')
#                     for i in sorting:
#                         refer_text = i.find('div',{'class' : 'schedule-show-control'}).find("div").text
#                         # print(refer_text)
#                         if "과제" in refer_text or "개인" in refer_text:
#                             title = None
#                             if "과제" in refer_text:
#                                 title = "[과제]"
#                             else:
#                                 title = "[개인]"
#                             hw_tags = i.find('div', {"class" : "changeDetile schedule-Detail-Box"})
#                             striped_ = []
#                             hw_tag = hw_tags.text.splitlines()
#
#                             for i in hw_tag:
#                                 if len(i.strip()) == 0 or len(i) == 0:
#                                     pass
#                                 else:
#                                     striped_.append(i.strip())
#
#                             now = datetime.datetime.now()
#                             nowDatetime = now.strftime('%Y.%m.%d %H:%M:%S')
#                             due_date = None
#                             if "마감일" in striped_[-1] or "Due Date" in striped_[-1]:
#                                 due_date = striped_[-1][6:]
#                             else:
#                                 if len(str(now_date)) == 1:
#                                     due_date = nowDatetime[:7] + ".0" + str(now_date)
#                                 else:
#                                     due_date = nowDatetime[:7] + "." + str(now_date)
#                                 striped_.append("마감일 : " + due_date)
#                             if len(striped_) == 0 or nowDatetime > due_date:
#                                 del striped_
#                             striped_.insert(0, title)
#                             result.append(striped_)
#
#                 except:
#                     pass
#             if now_date < temp:
#                 break
#             temp += 1
#
# except:
#     pass
#
# if len(result) == 0:
#     print("과제가 없습니다.")
# else:
#     for i in result:
#         for j in i:
#             print(j)
#         print()