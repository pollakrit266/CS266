from operator import truediv
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui, QtCore
from panel import Ui_MainWindow
import os
from datetime import date
import calendar
import sqlite3
from pygame import mixer
import webbrowser


# importing all files  from tkinter
from tkinter import * 
from tkinter.ttk import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfile


#completed
date_full = str(date.today()).split('-')
date_name = 'date'+date_full[0]+date_full[1]+date_full[2]

conn = sqlite3.connect('todo.db')
c = conn.cursor()
c.execute(f'''CREATE TABLE IF NOT EXISTS {date_name}(
            task text,
            number integer,
            status integer
         )''')
conn.commit()

page_time = 0
number_task = int()
number = 0
checkalams = 5
stopSongs = False
stopSongcheck = 0

changtime = False
changtimecheck = 0
timecount = 0
time_min = 0
time_hour = 0


mixer.init()
mixer.music.load('alarms/alarm1.mp3')    ######################################################ไฟล์เสียงเริ่มต้น

class Root(QMainWindow):

    def __init__(self):  ############กำหนด class
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow() #ui_window
        self.ui.setupUi(self)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.show()

        self.set_task()

        timer = QTimer(self)
        timer.timeout.connect(self.timer)
        timer.start(1000)

        #self.ui.cs1.setPlaceholderText("Add a Task(ใส่งานใจ)")
        self.ui.addtask.setPlaceholderText("Add a Task(ใส่งาน)")
        self.ui.addtask_3.setPlaceholderText("Add a Task(ใส่งาน)")

        # set username and profile
        self.ui.nameuser.setText(os.getlogin())
        self.ui.profile.setText(str(os.getlogin())[0])
        self.ui.nameuser2.setText(os.getlogin())
        self.ui.profile2.setText(str(os.getlogin())[0])
        self.ui.nameuser2_2.setText(os.getlogin())
        self.ui.profile2_2.setText(str(os.getlogin())[0])
        self.ui.nameuser2_3.setText(os.getlogin())
        self.ui.profile2_3.setText(str(os.getlogin())[0])
        self.ui.nameuser5.setText(os.getlogin())
        self.ui.profile5.setText(str(os.getlogin())[0])

        self.ui.submit.clicked.connect(self.submit)
        self.ui.submit_2.clicked.connect(self.submit2)

        # timer เซ็ตเวลา
        self.ui.timer1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.set_timer))
        self.ui.timer1.clicked.connect(self.page_clock)  

        self.ui.timerd1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.set_timer))
        self.ui.timerd1.clicked.connect(self.page_clock_day)  #เชื่อมไปที่ self.page_clock

        self.ui.timer2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.set_timer))
        self.ui.timer2.clicked.connect(self.page_clock)

        self.ui.timerd2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.set_timer))
        self.ui.timerd2.clicked.connect(self.page_clock_day)  #เชื่อมไปที่ self.page_clock

        self.ui.timer3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.set_timer))
        self.ui.timer3.clicked.connect(self.page_clock)

        self.ui.timerd3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.set_timer))
        self.ui.timerd3.clicked.connect(self.page_clock_day)  #เชื่อมไปที่ self.page_clock

        self.ui.timer4.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.set_timer))
        self.ui.timer4.clicked.connect(self.page_clock)

        self.ui.timerd4.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.set_timer))
        self.ui.timerd4.clicked.connect(self.page_clock_day)  #เชื่อมไปที่ self.page_clock

        self.ui.timer5.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.set_timer))
        self.ui.timer5.clicked.connect(self.page_clock)

        self.ui.timerd5.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.set_timer))
        self.ui.timerd5.clicked.connect(self.page_clock_day)  #เชื่อมไปที่ self.page_clock


        self.ui.timer6.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.set_timer))
        self.ui.timer6.clicked.connect(self.page_clock)

        self.ui.timerd6.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.set_timer))
        self.ui.timerd6.clicked.connect(self.page_clock_day)  #เชื่อมไปที่ self.page_clock
        
        self.ui.timer7.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.set_timer))
        self.ui.timer7.clicked.connect(self.page_clock)

        self.ui.timerd7.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.set_timer))
        self.ui.timerd7.clicked.connect(self.page_clock_day)  #เชื่อมไปที่ self.page_clock

        self.ui.timer8.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.set_timer))
        self.ui.timer8.clicked.connect(self.page_clock)

        self.ui.timerd8.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.set_timer))
        self.ui.timerd8.clicked.connect(self.page_clock_day)  #เชื่อมไปที่ self.page_clock

        self.ui.cancel_time.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.day_task))
        self.ui.cancel_time.clicked.connect(self.page_clock_cancel)    #link ไปปุ่มกดที่กดเเล้วจะยกเลิกเเละกับไปหน้าหลักเเละรีเซตค่าตั้งเวลาใหม่
        self.ui.sub_time.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.day_task))   #########################
        self.ui.sub_time.clicked.connect(self.set_clock)                                                      ######################### ส่งข้อมูลไปset_clock
        self.ui.ok_clock.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.day_task))   #########################
        self.ui.ok_clock.clicked.connect(self.stop_clock)                                                    #########################

        # pages
        self.ui.comp1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.completed))
        self.ui.comp1.clicked.connect(self.page_clock)
        self.ui.comp2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.completed))
        self.ui.comp2.clicked.connect(self.page_clock)
        self.ui.comp4.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.completed))
        self.ui.comp4.clicked.connect(self.page_clock)
        self.ui.comp5.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.completed))
        self.ui.comp5.clicked.connect(self.page_clock)

        self.ui.my_day3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.day_task))
        self.ui.my_day3.clicked.connect(self.page_clock_cancel)
        self.ui.my_day4.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.day_task))
        self.ui.my_day4.clicked.connect(self.page_clock_cancel)
        self.ui.my_day5.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.day_task))
        self.ui.my_day5.clicked.connect(self.page_clock_cancel)

        self.ui.calender1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.calender))
        self.ui.calender1.clicked.connect(self.page_clock)
        self.ui.calender2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.calender))
        self.ui.calender2.clicked.connect(self.page_clock)
        self.ui.calender3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.calender))
        self.ui.calender3.clicked.connect(self.page_clock)
        self.ui.calender5.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.calender))
        self.ui.calender5.clicked.connect(self.page_clock)

        self.ui.about1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.about))
        self.ui.about1.clicked.connect(self.page_clock)
        self.ui.about2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.about))
        self.ui.about2.clicked.connect(self.page_clock)
        self.ui.about3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.about))
        self.ui.about3.clicked.connect(self.page_clock)
        self.ui.about4.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.about))
        self.ui.about4.clicked.connect(self.page_clock)

        self.ui.search_cal.clicked.connect(self.calender_search)

        # del task
        self.ui.delete1.clicked.connect(self.remove_task1)
        self.ui.delete2.clicked.connect(self.remove_task2)
        self.ui.delete3.clicked.connect(self.remove_task3)
        self.ui.delete4.clicked.connect(self.remove_task4)
        self.ui.delete5.clicked.connect(self.remove_task5)
        self.ui.delete6.clicked.connect(self.remove_task6)
        self.ui.delete7.clicked.connect(self.remove_task7)
        self.ui.delete8.clicked.connect(self.remove_task8)

        # Completed task
        self.ui.sub1.clicked.connect(self.sub_task1)
        self.ui.sub2.clicked.connect(self.sub_task2)
        self.ui.sub3.clicked.connect(self.sub_task3)
        self.ui.sub4.clicked.connect(self.sub_task4)
        self.ui.sub5.clicked.connect(self.sub_task5)
        self.ui.sub6.clicked.connect(self.sub_task6)
        self.ui.sub7.clicked.connect(self.sub_task7)
        self.ui.sub8.clicked.connect(self.sub_task8)

        self.ui.date_cal.setPlaceholderText("Enter date : ปี/เดือน/วัน") #เปลี่ยนเวลา ###########################################################################

        # link contact
        self.ui.contactme.clicked.connect(self.file_save)  ###################save ไฟล์เสียง####################################################################
        

        self.ui.Radio1.clicked.connect(self.file_open)     ###################open ไฟล์เสียง####################################################################


        self.ui.Radio2.clicked.connect(self.music_off)     ###################เปิด/ปิดเสียงเเจ้งเตีอน####################################################################

        self.ui.settingtime.clicked.connect(self.chang_t)     ###################เปิด/ปิดเสียงเเจ้งเตีอน####################################################################

        #self.ui.cs1.clicked.connect(self.file_save) ########################################################################################################################

    def mousePressEvent(self, evt):
        self.oldPos = evt.globalPos()

    def mouseMoveEvent(self, evt):

        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def submit(self):
        global number_task
        text = self.ui.addtask.text()
        self.ui.addtask.clear()
        print("onclick")
        if len(text) == 0:
            self.ui.addtask.setPlaceholderText("Please type a Task")
        else:
            number_task += 1
            self.add_task(number_task, text)

    def submit2(self):
        global number_task
        text = self.ui.addtask_3.text()
        self.ui.addtask_3.clear()
        if len(text) == 0:
            self.ui.addtask_3.setPlaceholderText("Please type a Task")
        else:
            number_task += 1
            self.add_task(number_task, text)

    def add_task(self, num, txt):
        global c
        global conn
        global date_name

        if num <= 8:
            new_data = ("""INSERT INTO {}(task, number, status) VALUES ('{}',{}, {});""".format(date_name, str(txt), int(num), 0))
            c.execute(new_data)
            conn.commit()
        self.set_task()

    def set_task(self):
        global number
        global date_name
        global page_time
        number = 0
        tasks = c.execute(f'SELECT * FROM {date_name}')
        for temp in tasks:
            if temp[2] == 0:
                number += 1

        if number == 0 and page_time != 1:
            self.ui.stackedWidget.setCurrentWidget(self.ui.day)

        count = 0
        tasks = c.execute(f'SELECT * FROM {date_name}')
        for row in tasks:
            if int(row[2]) == 0:
                count += 1
                txt = row[0]
                if count == 1:
                    if page_time != 1:
                        self.ui.stackedWidget.setCurrentWidget(self.ui.day_task)
                    self.ui.task1.show()
                    self.ui.task1.setText(txt)
                    self.ui.sub1.show()
                    self.ui.delete1.show()
                    self.ui.timer1.show()
                    self.ui.timerd1.show()
                if count == 2:
                    self.ui.task2.show()
                    self.ui.task2.setText(txt)
                    self.ui.sub2.show()
                    self.ui.delete2.show()
                    self.ui.timer2.show()
                    self.ui.timerd2.show()
                if count == 3:
                    self.ui.task3.show()
                    self.ui.task3.setText(txt)
                    self.ui.sub3.show()
                    self.ui.delete3.show()
                    self.ui.timer3.show()
                    self.ui.timerd3.show()
                if count == 4:
                    self.ui.task4.show()
                    self.ui.task4.setText(txt)
                    self.ui.sub4.show()
                    self.ui.delete4.show()
                    self.ui.timer4.show()
                    self.ui.timerd4.show()
                if count == 5:
                    self.ui.task5.show()
                    self.ui.task5.setText(txt)
                    self.ui.sub5.show()
                    self.ui.delete5.show()
                    self.ui.timer5.show()
                    self.ui.timerd5.show()
                if count == 6:
                    self.ui.task6.show()
                    self.ui.task6.setText(txt)
                    self.ui.sub6.show()
                    self.ui.delete6.show()
                    self.ui.timer6.show()
                    self.ui.timerd6.show()
                if count == 7:
                    self.ui.task7.show()
                    self.ui.task7.setText(txt)
                    self.ui.sub7.show()
                    self.ui.delete7.show()
                    self.ui.timer7.show()
                    self.ui.timerd7.show()
                if count == 8:
                    self.ui.task8.show()
                    self.ui.task8.setText(txt)
                    self.ui.sub8.show()
                    self.ui.delete8.show()
                    self.ui.timer8.show()
                    self.ui.timerd8.show()

    def set_completed(self):
        global date_name
        count = 0
        tasks = c.execute(f'SELECT * FROM {date_name}')
        for row in tasks:
            if int(row[2]) == 1:
                count += 1
                txt = row[0]
                if count == 1:
                    self.ui.com1.show()
                    self.ui.com1.setText(txt)
                if count == 2:
                    self.ui.com2.show()
                    self.ui.com2.setText(txt)
                if count == 3:
                    self.ui.com3.show()
                    self.ui.com3.setText(txt)
                if count == 4:
                    self.ui.com4.show()
                    self.ui.com4.setText(txt)
                if count == 5:
                    self.ui.com5.show()
                    self.ui.com5.setText(txt)
                if count == 6:
                    self.ui.com6.show()
                    self.ui.com6.setText(txt)
                if count == 7:
                    self.ui.com7.show()
                    self.ui.com7.setText(txt)
                if count == 8:
                    self.ui.com8.show()
                    self.ui.com8.setText(txt)

    def remove_task1(self):
        global c
        global conn
        global number
        global date_name
        task = self.ui.task1.text()
        c.execute(f'DELETE FROM {date_name} WHERE task = "{task}"')
        conn.commit()
        self.remover(number)
        self.set_task()

    def remove_task2(self):
        global c
        global conn
        global number
        global date_name
        task = self.ui.task2.text()
        c.execute(f'DELETE FROM {date_name} WHERE task = "{task}"')
        conn.commit()
        self.remover(number)
        self.set_task()

    def remove_task3(self):
        global c
        global conn
        global number
        global date_name
        task = self.ui.task3.text()
        c.execute(f'DELETE FROM {date_name} WHERE task = "{task}"')
        conn.commit()
        self.remover(number)
        self.set_task()

    def remove_task4(self):
        global c
        global conn
        global number
        global date_name
        task = self.ui.task4.text()
        c.execute(f'DELETE FROM {date_name} WHERE task = "{task}"')
        conn.commit()
        self.remover(number)
        self.set_task()

    def remove_task5(self):
        global c
        global conn
        global number
        global date_name
        task = self.ui.task5.text()
        c.execute(f'DELETE FROM {date_name} WHERE task = "{task}"')
        conn.commit()
        self.remover(number)
        self.set_task()

    def remove_task6(self):
        global c
        global conn
        global number
        global date_name
        task = self.ui.task6.text()
        c.execute(f'DELETE FROM {date_name} WHERE task = "{task}"')
        conn.commit()
        self.remover(number)
        self.set_task()

    def remove_task7(self):
        global c
        global conn
        global number
        global date_name
        task = self.ui.task7.text()
        c.execute(f'DELETE FROM {date_name} WHERE task = "{task}"')
        conn.commit()
        self.remover(number)
        self.set_task()

    def remove_task8(self):
        global c
        global conn
        global number
        global date_name
        task = self.ui.task8.text()
        c.execute(f'DELETE FROM {date_name} WHERE task = "{task}"')
        conn.commit()
        self.remover(number)
        self.set_task()

    def remover(self, num):
        self.ui.task1.clear()
        self.ui.task2.clear()
        self.ui.task3.clear()
        self.ui.task4.clear()
        self.ui.task5.clear()
        self.ui.task6.clear()
        self.ui.task7.clear()
        self.ui.task8.clear()
        if num == 8:
            self.ui.task8.hide()
            self.ui.sub8.hide()
            self.ui.delete8.hide()
            self.ui.timer8.hide()
            self.ui.timerd8.hide()
        elif num == 7:
            self.ui.task7.hide()
            self.ui.sub7.hide()
            self.ui.delete7.hide()
            self.ui.timer7.hide()
            self.ui.timerd7.hide()
        elif num == 6:
            self.ui.task6.hide()
            self.ui.sub6.hide()
            self.ui.delete6.hide()
            self.ui.timer6.hide()
            self.ui.timerd6.hide()
        elif num == 5:
            self.ui.task5.hide()
            self.ui.sub5.hide()
            self.ui.delete5.hide()
            self.ui.timer5.hide()
            self.ui.timerd5.hide()
        elif num == 4:
            self.ui.task4.hide()
            self.ui.sub4.hide()
            self.ui.delete4.hide()
            self.ui.timer4.hide()
            self.ui.timerd4.hide()
        elif num == 3:
            self.ui.task3.hide()
            self.ui.sub3.hide()
            self.ui.delete3.hide()
            self.ui.timer3.hide()
            self.ui.timerd3.hide()
        elif num == 2:
            self.ui.task2.hide()
            self.ui.sub2.hide()
            self.ui.delete2.hide()
            self.ui.timer2.hide()
            self.ui.timerd2.hide()
        elif num == 1:
            self.ui.task1.hide()
            self.ui.sub1.hide()
            self.ui.delete1.hide()
            self.ui.timer1.hide()
            self.ui.timerd1.hide()

    def page_clock(self):    ############################################################ ui หน้าคั้งนาฟิกา
        global page_time
        page_time = 1
        self.ui.hh.clearFocus()
        self.ui.hh.setPlaceholderText("ชั่วโมง")   #################################### เซ็ตตั้งเวลาเริ่มต้นเป็น 00
        self.ui.mm.setPlaceholderText("นาที")   ####################################
        self.ui.ss.setPlaceholderText("วินาที")   ####################################

    def page_clock_day(self):    ############################################################ ui หน้าคั้งนาฟิกา
        global page_time
        page_time = 1
        self.ui.hh.clearFocus()
        self.ui.hh.setPlaceholderText("ปี")   #################################### เซ็ตตั้งเวลาเริ่มต้นเป็น 00
        self.ui.mm.setPlaceholderText("เดือน")   ####################################
        self.ui.ss.setPlaceholderText("วัน")   ####################################    
 
    def page_clock_cancel(self):
        global page_time
        page_time = 0

    
    def timer(self):  ##########################เรื่องเวลา
        global c
        global conn
        global date_name
        global date_full
        global timecount
        global time_min
        global time_hour
        

        # get time
        currentTime = QTime.currentTime()
        display_text = currentTime.toString('hh:mm:ss')
        self.ui.now_time.setText(display_text)

        # set date
        date_full2 = str(date.today())    ##############################################วันนี้
        mounth = calendar.month_name[int(date_full2[5:7])]
        day = date.today().strftime("%A")

        self.ui.date.setText('%s, %s %s' % (day, mounth, date_full2[8:]))
        self.ui.date2.setText('%s, %s %s' % (day, mounth, date_full2[8:]))
        self.ui.date3.setText('%s, %s %s' % (day, mounth, date_full2[8:]))

        # set date - database
        date_full = str(date.today()).split('-')
        date_name = 'date' + date_full[0] + date_full[1] + date_full[2]
        #print("datafull"+date_name)
        date_name_ofyear = date_full[0] +":"+ date_full[1] +":"+ date_full[2]

        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute(f'''CREATE TABLE IF NOT EXISTS {date_name}(
                    task text,
                    number integer,
                    status integer
                 )''')
        conn.commit()

        # Update task
        self.set_task()
        self.set_completed()

        c.execute(f'''CREATE TABLE IF NOT EXISTS {date_name+'time'}(
                    time text
                 )''')
        conn.commit()

        # clock                                ######################### เตื่อนเมือถึงเวลา
        print(date_name_ofyear)                      ################################################################### เวลาในเครื่องคอม
       # year1 = 0
        clocks = c.execute(f'SELECT * FROM {date_name+"time"}')
        timecount +=1
        #print("clocks" + date_name)                         ###################################################################################เเสดงค่าของวันนี้
        for row in clocks:
            print(row[0])           #######################################เอาเวลาที่เราตั้งมาเทียบกับเวลาปัจจุบัน เช่น ตอนนี้เวลา13:22:20 เราอยากตั้งเตื่อน10วิข้างหน้าก็ตั้ง 13:20:30ในช่องใส่เวลา 
            print("dis"+display_text)                ###################################################################################เเสดงเวลาปัจุบันเเบบ realtime  

            #print(year1)
            if str(list(row)[0]) == str(display_text) and changtime == False:          ############################เวลา ที่ระบุ
                if(stopSongs == False):
                    mixer.init()
                    mixer.music.play()
                self.ui.stackedWidget.setCurrentWidget(self.ui.stop_timer)
                c.execute(f'DELETE FROM {date_name+"time"} WHERE time = "{display_text}"')
                conn.commit()
                break
            
            
            if str(list(row)[0]) == str(date_name_ofyear) and changtime == False:     ############################เช็ควัน เดือน ปี ที่ระบุ
                #mixer.init()
                #mixer.music.play()
                #self.ui.stackedWidget.setCurrentWidget(self.ui.stop_timer)
                year1 = 1
                #conn.commit()

            if str(list(row)[0]) == str(display_text) and year1 == 1 and changtime == False:          ############################เวลา ที่ระบุ
                if(stopSongs == False):
                    mixer.init()
                    mixer.music.play()
                self.ui.stackedWidget.setCurrentWidget(self.ui.stop_timer)
                c.execute(f'DELETE FROM {date_name+"time"} WHERE time = "{display_text}"')
                c.execute(f'DELETE FROM {date_name+"time"} WHERE time = "{date_name_ofyear}"')
                conn.commit()


            if(timecount < 10):
                timestr = str(timecount)
                timestr = "0" + timestr

            if(timecount >= 10):
                timestr = str(timecount)

            if(timecount == 60):
                timestr = "00"
                time_min +=1
                timecount = 0
            
            if(time_min < 10):
                timestr1 = str(time_min)
                timestr1 = "0" + timestr1

            if(time_min >= 10):
                timestr1 = str(time_min)

            if(time_min == 60):
                timestr1 = "00"
                time_hour +=1
                time_min = 0

            if(time_hour < 10):
                timestr2 = str(time_hour)
                timestr2 = "0" + timestr2

            if(time_hour >= 10):
                timestr2 = str(time_hour)

            
            sum = timestr2 +":"+ timestr1 +":" + timestr

            
            
            print("sum",sum)
            
            if(str(list(row)[0]) == sum and changtime == True ):
                if(stopSongs == False):
                    mixer.init()
                    mixer.music.play()
                self.ui.stackedWidget.setCurrentWidget(self.ui.stop_timer)
                c.execute(f'DELETE FROM {date_name+"time"} WHERE time = "{sum}"')
                conn.commit()
                


           
            

                
               

    def set_clock(self):
        global c
        global conn
        global date_name
        global timecount
        global time_min
        global time_hour

        timecount = 0
        time_min  = 0
        time_hour =0

        print("oncilck")

        clock = str(self.ui.hh.text()+':'+self.ui.mm.text()+':'+self.ui.ss.text())   ###########เก็บข้อมูล
        #print(clock)              ################################################################################### รับเวลาที่เรากรอกตอนตั้งเวลามา
        self.ui.hh.clear()
        self.ui.mm.clear()
        self.ui.ss.clear()
        new_data = ("""INSERT INTO {}(time) VALUES ('{}');""".format(date_name+'time', clock))
        #print(new_data)       ############################################# รับค่ามาใส่
        c.execute(new_data)         
        conn.commit()

    def stop_clock(self):
        mixer.music.stop()

    def sub_task1(self):
        task = self.ui.task1.text()
        self.sub_tasks(task)

    def sub_task2(self):
        task = self.ui.task2.text()
        self.sub_tasks(task)

    def sub_task3(self):
        task = self.ui.task3.text()
        self.sub_tasks(task)

    def sub_task4(self):
        task = self.ui.task4.text()
        self.sub_tasks(task)

    def sub_task5(self):
        task = self.ui.task5.text()
        self.sub_tasks(task)

    def sub_task6(self):
        task = self.ui.task6.text()
        self.sub_tasks(task)

    def sub_task7(self):
        task = self.ui.task7.text()
        self.sub_tasks(task)

    def sub_task8(self):
        task = self.ui.task8.text()
        self.sub_tasks(task)

    def sub_tasks(self, task):
        global c
        global conn
        global date_name
        global number
        num = 1
        sql_update_query = """Update {} set status = {} where task = '{}'""".format(date_name, num, str(task))
        c.execute(sql_update_query)
        conn.commit()
        self.remover(number)
        self.set_task()

    def calender_search(self):
        global c
        global conn
        self.ui.com1_cal.hide()
        self.ui.com2_cal.hide()
        self.ui.com3_cal.hide()
        self.ui.com4_cal.hide()
        self.ui.com5_cal.hide()
        self.ui.com6_cal.hide()
        self.ui.com7_cal.hide()
        self.ui.com8_cal.hide()
        self.ui.task1_cal.hide()
        self.ui.task2_cal.hide()
        self.ui.task3_cal.hide()
        self.ui.task4_cal.hide()
        self.ui.task5_cal.hide()
        self.ui.task6_cal.hide()
        self.ui.task7_cal.hide()
        self.ui.task8_cal.hide()
        self.ui.True1.hide()
        self.ui.True2.hide()
        self.ui.True3.hide()
        self.ui.True4.hide()
        self.ui.True5.hide()
        self.ui.True6.hide()
        self.ui.True7.hide()
        self.ui.True8.hide()
        self.ui.False1.hide()
        self.ui.False2.hide()
        self.ui.False3.hide()
        self.ui.False4.hide()
        self.ui.False5.hide()
        self.ui.False6.hide()
        self.ui.False7.hide()
        self.ui.False8.hide()
        if len(self.ui.date_cal.text()) == 10:
            names = self.ui.date_cal.text().split('/')
            name = 'date'+names[0]+names[1]+names[2]
            print(name)  ######################################################################## เราวันเดือนปีที่เรากรอกใน calender มา
            
            c.execute(f'''CREATE TABLE IF NOT EXISTS {name}(
                        task text,
                        number integer,
                        status integer
                     )''')
            conn.commit()

            tasks = c.execute(f'SELECT * FROM {name}')
            #print(tasks)             ######################################################################## จำนวนงาน
            count_com = 0
            count_task = 0
            for row in tasks:
                if row[2] == 1 and len(row[0]) != 0:
                    count_com += 1
                    if count_com == 1:
                        self.ui.com1_cal.show()
                        self.ui.True1.show()
                        self.ui.com1_cal.setText(row[0])
                    elif count_com == 2:
                        self.ui.com2_cal.show()
                        self.ui.True2.show()
                        self.ui.com2_cal.setText(row[0])
                    elif count_com == 3:
                        self.ui.com3_cal.show()
                        self.ui.True3.show()
                        self.ui.com3_cal.setText(row[0])
                    elif count_com == 4:
                        self.ui.com4_cal.show()
                        self.ui.True4.show()
                        self.ui.com4_cal.setText(row[0])
                    elif count_com == 5:
                        self.ui.com5_cal.show()
                        self.ui.True5.show()
                        self.ui.com5_cal.setText(row[0])
                    elif count_com == 6:
                        self.ui.com6_cal.show()
                        self.ui.True6.show()
                        self.ui.com6_cal.setText(row[0])
                    elif count_com == 7:
                        self.ui.com7_cal.show()
                        self.ui.True7.show()
                        self.ui.com7_cal.setText(row[0])
                    elif count_com == 8:
                        self.ui.com8_cal.show()
                        self.ui.True8.show()
                        self.ui.com8_cal.setText(row[0])

                elif row[2] == 0 and len(row[0]) != 0:
                    count_task += 1
                    if count_task == 1:
                        self.ui.task1_cal.show()
                        self.ui.False1.show()
                        self.ui.task1_cal.setText(row[0])
                    elif count_task == 2:
                        self.ui.task2_cal.show()
                        self.ui.False2.show()
                        self.ui.task2_cal.setText(row[0])
                    elif count_task == 3:
                        self.ui.task3_cal.show()
                        self.ui.False3.show()
                        self.ui.task3_cal.setText(row[0])
                    elif count_task == 4:
                        self.ui.task4_cal.show()
                        self.ui.False4.show()
                        self.ui.task4_cal.setText(row[0])
                    elif count_task == 5:
                        self.ui.task5_cal.show()
                        self.ui.False5.show()
                        self.ui.task5_cal.setText(row[0])
                    elif count_task == 6:
                        self.ui.task6_cal.show()
                        self.ui.False6.show()
                        self.ui.task6_cal.setText(row[0])
                    elif count_task == 7:
                        self.ui.task7_cal.show()
                        self.ui.False7.show()
                        self.ui.task7_cal.setText(row[0])
                    elif count_task == 8:
                        self.ui.task8_cal.show()
                        self.ui.False8.show()
                        self.ui.task8_cal.setText(row[0])
        else:
            self.ui.date_cal.clear()
            self.ui.date_cal.setPlaceholderText("Enter date : ปี/เดือน/วัน") #เปลี่ยนเวลา ###########################################################################

    #def contact(self):
        #webbrowser.open('https://bioly.io/AbbasAtaei')

    def file_save(self):            ########################save ไฟล์เสียง##################################################################################
        files = [('All Files', '*.*'), 
             ('Python Files', '*.py'),
             ('Text Document', '*.txt')]
        file = asksaveasfile(filetypes = files, defaultextension = files)
    

    def file_open(self):           ########################open ไฟล์เสียง##################################################################################
        files = [('All Files', '*.*'), 
             ('Python Files', '*.py'),
             ('Text Document', '*.txt')]
        file = askopenfile(filetypes = files, defaultextension = files)
        setalams = file.name
        setalams = file.name.split("/")
        checkalams = 1
        

        check = 0
        for x in setalams:
            check += 1
            if(check == len(setalams)-2):
                setalams_real = setalams[check]

            if(check == len(setalams)-1):
                setalams_real = str(setalams_real + "/" + setalams[check])
        
        print(setalams_real)
        mixer.init()
        mixer.music.load(setalams_real)    ######################################################เปลี่ยนไฟล์เสียง

    
    
    def music_off(self):

        global stopSongcheck
        global stopSongs
        stopSongcheck += 1

        if(stopSongcheck%2 == 0):
            stopSongs = False

        else:
            stopSongs = True  

    def chang_t(self):

        global changtimecheck
        global changtime
        changtimecheck += 1

        if(changtimecheck%2 == 0):
            changtime = False

        else:
            changtime = True  



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    root = Root()
    sys.exit(app.exec_())
