
from typing import KeysView
from selenium import webdriver
from datetime import date
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


import datetime
import calendar
import time




#############  stopping program till time  9:40 AM #################################

time_2 = datetime.timedelta(hours= 9, minutes=40)
while 1:
    currTime={
        'hour':time.localtime().tm_hour,
        'min':time.localtime().tm_min
    }
    time_1=datetime.timedelta(hours= currTime['hour'],minutes= currTime['min'])
    diff=str(time_2-time_1)

    if diff=='0:00:00':
        break
    time.sleep(2)




################ Setting up webDriver ################
chrome_options = Options()
chrome_options.add_argument("--use-fake-ui-for-media-stream")
chrome_options.add_argument('use-fake-device-for-media-stream')
chrome_browser = webdriver.Chrome(chrome_options=chrome_options)
chrome_browser.maximize_window()


chrome_browser.get('https://cuchd.blackboard.com/')



######### clicking ok button of cookies ################
time.sleep(3)
ok_button = chrome_browser.find_element_by_class_name('button-1')
# ok_button.implicitly_wait(20000)
webdriver.ActionChains(chrome_browser).click(ok_button).perform()



################### Login to BB  #############################

time.sleep(2)
user_input = chrome_browser.find_element_by_id('user_id')
user_password = chrome_browser.find_element_by_id('password')
SignIn = chrome_browser.find_element_by_id('entry-login')
user_input.clear()
user_input.send_keys('20BCS1563')
user_password.send_keys('Prabhjot@singh1')
time.sleep(1)
webdriver.ActionChains(chrome_browser).click(SignIn).perform()



#####################  Join class Link #############################
first=1
def joinClass(first):
    link = chrome_browser.find_element(By.ID, 'sessions-list-dropdown')
    login_form = chrome_browser.find_element_by_css_selector('ul#sessions-list li:last-child')
    joiningLink = login_form.find_element_by_tag_name('a')
    link.click()
    time.sleep(1)
    joiningLink.click()
    time.sleep(2)
    allTabs=chrome_browser.window_handles
    chrome_browser.switch_to.window(allTabs[1])
    close1=chrome_browser.find_element(By.CLASS_NAME,'close')
    close1.click()
    time.sleep(2)
    if first==1:
        close2=chrome_browser.find_element(By.CLASS_NAME,'later-tutorial-button')
        close2.click()
        close3=chrome_browser.find_element(By.ID,   'tutorial-dialog-tutorials-menu-learn-about-tutorials-menu-close')
        close3.click()
    time.sleep(5)
    chrome_browser.close()
    chrome_browser.switch_to.window(allTabs[0])



#################### open class Automatic function #########################
def openClass(classCode,first):
    time.sleep(5)
    search_button = chrome_browser.find_element_by_class_name('ng-empty')
    chrome_browser.implicitly_wait(20)
    search_button.send_keys(classCode)
    time.sleep(5)
    testing = chrome_browser.find_element_by_id('course-columns-current')
    webdriver.ActionChains(chrome_browser).click(testing).perform()

    joinClass(first)



###############  TimeTable #############################

timeTable = [
    ['CST-211', 'CST-218', 'CST-212', None, 'SMT-236'],
    ['CSP-212', 'CSP-212', 'CST-214', None, 'CST-218', 'CSP-219', 'CSP-219'],
    ['CST-211', 'CST-214', 'SMT-236', None, 'SMT-236', 'CSP-215'],
    ['TDT-202', 'TDT-202', 'CST-214', 'CST-212', None, 'SMT-236'],
    ['UCY-246', 'CSP-212', 'CSP-212', None, 'CST-211'],
    ['UCY-246', 'CSP-212', 'CSP-212', 'None', 'CST-211']
]



##################### getting Todays Day #########################
def getTodayDay(x):
    switcher = {
        'Sunday': None,
        'Monday': 0,
        'Tuesday': 1,
        'Wednesday': 2,
        'Thursday': 3,
        'Friday': 4,
        'Saturday': 5  # change it to none (was trying something)
    }
    return switcher.get(x, "Invalid day of week")


my_date = date.today()
todaysDay = calendar.day_name[my_date.weekday()]
Day = getTodayDay(todaysDay)
print(Day)



#############  close current course content ################3
def close_course_content():
    closeButton = chrome_browser.find_element(By.CLASS_NAME, "bb-close")
    webdriver.ActionChains(chrome_browser).click(closeButton).perform()

    
###########  Clear Serch Box ##################
def clear_search_box():
    filled_search_button = chrome_browser.find_element_by_class_name(
        'ng-not-empty')
    filled_search_button.clear()


for i in timeTable[Day]:
    if i=='None':
        print('###################################  None found  #####################')
        time.sleep(20)
        continue
    openClass(i)
      first=0
    time.sleep(5)
    close_course_content()
    clear_search_box()


chrome_browser.quit()
