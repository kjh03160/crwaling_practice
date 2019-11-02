from bs4 import BeautifulSoup as bs
from selenium import webdriver
import datetime

import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 900)

        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(50,200,400,650))
        self.listWidget.setObjectName("textBrowser")

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(190, 10, 300, 16))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(190, 80, 300, 16))
        self.label_2.setObjectName("label_2")

        self.startButton = QtWidgets.QPushButton(Dialog)
        self.startButton.setGeometry(QtCore.QRect(160, 150, 190, 23))
        self.startButton.setObjectName("startButton")

        self.lineEdit_ID = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_ID.setGeometry(QtCore.QRect(160, 30, 190, 30))
        self.lineEdit_ID.setObjectName("lineEdit_ID")

        self.lineEdit_PW = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_PW.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_PW.setGeometry(QtCore.QRect(160, 100, 190, 30))
        self.lineEdit_PW.setObjectName("lineEdit_PW")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # startButton 클릭시 autoExcute 함수 수행
        self.startButton.clicked.connect(self.autoExcute)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Login"))
        self.label.setText(_translate("Dialog", "학번(Student Num)"))
        self.label_2.setText(_translate("Dialog", "비밀번호(Password)"))
        self.startButton.setText(_translate("Dialog", "시작"))

    def autoExcute(self):

        id_input = self.lineEdit_ID.text()
        pw_input = self.lineEdit_PW.text()

        # self.listWidget.addItem('환경 설정 중...\n')
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument(
            "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")

        browser = webdriver.Chrome('.\chromedriver_win32\chromedriver.exe', options=options)
        browser.get("http://eclass2.hufs.ac.kr:8181/ilos/main/member/login_form.acl")

        id = browser.find_element_by_id("usr_id")
        id.send_keys(id_input)  # 아이디

        pw = browser.find_element_by_id("usr_pwd")
        pw.send_keys(pw_input)  # 비밀번호

        login_bt = browser.find_element_by_class_name('btntype')
        login_bt.click()
        # self.listWidget.addItem('로그인 완료\n')

        # 과제 가져오기

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
                    refer_text = i.find('div', {'class': 'schedule-show-control'}).find("div").text
                    if "과제" in refer_text or "개인" in refer_text:
                        title = None
                        if "과제" in refer_text:
                            title = "[과제]"
                        else:
                            title = "[개인]"
                        hw_tags = i.find('div', {"class": "changeDetile schedule-Detail-Box"})
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

        # listWidget에 로그인 성공 표시

        if len(result) == 0:
            self.listWidget.addItem('과제가 없습니다.')
        else:
            for i in result:
                for j in i:
                    self.listWidget.addItem(j)
                self.listWidget.addItem('\n')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
