# This will open a web browser, sign into venmo, and pay someone some money

from selenium.webdriver import Chrome
import cPickle as pickle
import SendKeys
import time
import venmoInfo
import datetime
import os

CHROME_DRIVER_PATH = 'C:\ChromeDriver\chromedriver.exe'
VENMO_URL = 'https://venmo.com/'

browser = Chrome(CHROME_DRIVER_PATH)
browser.get(VENMO_URL)

if os.path.isfile('cookies.pkl'):
    # there is a cookie file

    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        browser.add_cookie(cookie)

    # click on the sign in link
    signin_link = browser.find_element_by_link_text("Sign in")
    signin_link.click()

    # enter the email and password and send it
    username_box = browser.find_element_by_class_name("email-username-phone")
    username_box.send_keys(venmoInfo.my_u)
    password_box = browser.find_element_by_class_name("password")
    password_box.send_keys(venmoInfo.my_p)
    send_button = browser.find_element_by_class_name("login")
    send_button.click()

    # enter the person's name you want to pay
    time.sleep(5)
    name_box = browser.find_element_by_class_name("onebox_prefill")
    name_box.click()
    name_text_box = browser.find_element_by_class_name("paddingUnifier")
    name_text_box.send_keys(venmoInfo.payee_name)
    payment_box = browser.find_element_by_class_name("mainTextBox")
    payment_box.click()
    datetime_now = datetime.datetime.now()
    SendKeys.SendKeys(venmoInfo.amount + venmoInfo.description, with_spaces=True)

    # click the send button
    send_button = browser.find_element_by_id("onebox_send_button")
    send_button.click()

else:
    # click on the sign in link
    signin_link = browser.find_element_by_link_text("Sign in")
    signin_link.click()
    print("Couldn't find the cookie file, you will need two factor authorization and then cookie will be saved")
    # wait a while until the user fully signs in
    time.sleep(60)
    # Save the cookies
    pickle.dump(browser.get_cookies(), open("cookies.pkl", "wb"))

browser.close()
