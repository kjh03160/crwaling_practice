from selenium import webdriver
from time import sleep

def ticket(start, tic_num):

    driver = webdriver.Chrome('.\chromedriver_win32\chromedriver')
    driver.get('https://ticket.interpark.com/Gate/TPLogin.asp?CPage=B&MN=Y&tid1=main_gnb&tid2=right_top&tid3=login&tid4=login')
    driver.switch_to.frame(0)
    driver.find_element_by_name('userId').send_keys('')
    driver.find_element_by_name('userPwd').send_keys('')
    driver.find_element_by_xpath('//*[@id="btn_login"]').click()

    driver.get(start)
    driver.switch_to.frame('ifrCalendar')
    driver.find_element_by_xpath('//*[@id="CellPlayDate2"]/a').click()
    driver.switch_to.default_content()
    driver.find_element_by_xpath('/html/body/div[9]/div[2]/div[3]/div/div[2]/div/div[2]/div[5]/a').click()
    print(driver.title)
    sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    print(driver.title)
    sleep(1)
    driver.find_element_by_xpath('//*[@id="LargeNextBtnImage"]').click()
    sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    driver.switch_to.frame('ifrmSeat')
    driver.switch_to.frame('ifrmSeatDetail')

    count = 0
    for i in range(100):
        try:
            if driver.find_element_by_xpath('//*[@id="TmgsTable"]/tbody/tr/td/img[' + str(i) + ']'):
                for j in range(i, 100, 2):
                    driver.find_element_by_xpath('//*[@id="TmgsTable"]/tbody/tr/td/img[' + str(j) + ']').click()
                    count += 1
                    if count == tic_num+1:
                        break
                if count == tic_num+1:
                    break
        except:
            pass
    driver.switch_to.default_content()
    driver.switch_to.frame('ifrmSeat')
    driver.find_element_by_xpath('//*[@id="NextStepImage"]').click()

start = 'http://ticket.interpark.com/Ticket/Goods/GoodsInfo.asp?GoodsCode=18015454#'
ticket(start, 2)