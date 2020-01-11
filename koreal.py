# -*- coding: utf-8 -*-
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

url = 'http://www.letskorail.com/'

# https://sites.google.com/a/chromium.org/chromedriver/downloads
# os에 맞는 셀레니움 크롬 드라이버 설치후 driver 경로 지정 필요

driver = webdriver.Chrome('c:/selenium_chrome_driver/chromedriver_win32/chromedriver')
driver.get(url)
handles = driver.window_handles
size = len(handles)
# print(size)
main = driver.current_window_handle
# print (handles)
# print(main)
for handles in handles:
    if handles != main:
        driver.switch_to.window(handles)
        driver.close()

driver.switch_to.window(main)

booking = driver.find_element_by_css_selector('img[src*="/images/btn_reserve.gif"]')
booking.click()

driver.implicitly_wait(1)
start = driver.find_element_by_css_selector('#start')
# print (start.get_attribute('value'))
start.clear()

ys = '용산'
ys = unicode(ys.decode(('utf-8')))
start.send_keys(ys)

get = driver.find_element_by_css_selector('#get')
get.clear()

gj = '광주송정'
gj = unicode(gj.decode(('utf-8')))
get.send_keys(gj)

s_year = driver.find_element_by_css_selector('#s_year > option[value="2020"]')
s_year.click()
s_month = driver.find_element_by_css_selector('#s_month > option[value="01"]')
s_month.click()
s_day = driver.find_element_by_css_selector('#s_day > option[value="23"]')
s_day.click()
s_hour = driver.find_element_by_css_selector('#s_hour > option[value="16"]')
s_hour.click()

while True:
    search = driver.find_element_by_css_selector('img[src*="/images/btn_inq_tick.gif"]')
    search.click()

    popchk = driver.find_elements_by_css_selector('#chkNotSee')
    if len(popchk) > 0:
        popchk[0].click()

    driver.implicitly_wait(1)

    reservation20 = driver.find_elements_by_css_selector('img[name="btnRsv2_0"]')
    reservation10 = driver.find_elements_by_css_selector('img[name="btnRsv1_0"]')

    reservation21 = driver.find_elements_by_css_selector('img[name="btnRsv2_1"]')
    reservation11 = driver.find_elements_by_css_selector('img[name="btnRsv1_1"]')

    reservation23 = driver.find_elements_by_css_selector('img[name="btnRsv2_3"]')
    reservation13 = driver.find_elements_by_css_selector('img[name="btnRsv1_3"]')

    reservation24 = driver.find_elements_by_css_selector('img[name="btnRsv2_4"]')
    reservation14 = driver.find_elements_by_css_selector('img[name="btnRsv1_4"]')

    if len(reservation20) > 0:
        reservation20[0].click()
        break

    if len(reservation10) > 0:
        reservation10[0].click()
        break

    if len(reservation21) > 0:
        reservation21[0].click()
        break

    if len(reservation11) > 0:
        reservation11[0].click()
        break

    if len(reservation23) > 0:
        reservation23[0].click()
        break

    if len(reservation13) > 0:
        reservation13[0].click()
        break

    if len(reservation24) > 0:
        reservation24[0].click()
        break

    if len(reservation14) > 0:
        reservation14[0].click()
        break

while True:
    try:
        WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                       'Timed out waiting for PA creation ' +
                                       'confirmation popup to appear.')

        alert = driver.switch_to.alert
        alert.accept()
        print("alert accepted")
    except TimeoutException:
        break

driver.implicitly_wait(1)

id = '아이디'
pwd = '패스워드'

txtMember = driver.find_element_by_css_selector('#txtMember')
txtMember.clear()
txtMember.send_keys(id)

txtPwd = driver.find_element_by_css_selector('#txtPwd')
txtPwd.clear()
txtPwd.send_keys(pwd)

login = driver.find_element_by_css_selector('img[src*="/images/btn_login.gif"]')
login.click()

driver.implicitly_wait(1)

