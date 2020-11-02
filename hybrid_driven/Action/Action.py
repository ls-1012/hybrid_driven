#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# File:         Action.py
# Author:       ls
# Date:         2020/10/21 13:04
#-------------------------------------------------------------------------------
import os
import traceback
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from Util.Dir import make_time_dir
from Util.ObjectMap import find_element
from Util.ParseConfig import read_ini_file_option
from Conf.ProjVar import PageElementLocator_file_path
from Util.DateAndTime import *
from Util.Log import *

driver=""
my_log=MyLog()
log=my_log.get_logger()
def open_browser(browser_name):
    global driver
    if "ie" in browser_name.lower():
        driver=webdriver.Ie(executable_path="d:/Iedriverserver")
    elif "chrome" in browser_name.lower():
        driver = webdriver.Chrome(executable_path="d:/chromedriver")
    elif "firefox" in browser_name.lower():
        driver = webdriver.Firefox(executable_path="d:/geckodriver")
    else:
        print("请输入正确的浏览器：ie,firefox,chrome")

    return driver

def visit(url):
    global driver
    driver.get(url)

def input(xpath_exp,content):
    global driver
    if is_xpath(xpath_exp):
        driver.find_element_by_xpath(xpath_exp).senk_keys(content)
    else:
        element=get_element(xpath_exp)
        element.send_keys(content)




def click(xpath_exp):
    global driver
    if is_xpath(xpath_exp):
        print(xpath_exp)
        driver.find_element_by_xpath(xpath_exp).click()
    else:
        element=get_element(xpath_exp)
        element.click()


def switch_to_frame(xpath_exp):
    global driver
    if is_xpath(xpath_exp):
        frame = driver.find_element_by_xpath(xpath_exp)
        # frameid=frame.get_attribute("id")
    else:
        frame=get_element(xpath_exp)

    driver.switch_to.frame(frame)

def switch_back():
    global driver
    driver.switch_to.default_content()

def sleep(seconds):
    time.sleep(float(seconds))

def quit():
    global driver
    driver.quit()

def assert_result(expect_result):
    global driver
    # # element=None
    # if is_xpath(xpath_exp):
    #     element=driver.find_element_by_xpath(xpath_exp)
    # else:
    #     element = get_element(xpath_exp)
    # log.info("xpath_exp:%s" % xpath_exp.text)
    # log.info("expect_result:%s" % expect_result)
    assert expect_result in driver.page_source


def get_element(locator_exp):
    sectionname=locator_exp.split(",")[0]
    optionname=locator_exp.split(",")[1]

    locator_exp = read_ini_file_option(PageElementLocator_file_path, section_name=sectionname, option_name=optionname)
    element = find_element(driver,locator_exp.split(">")[0],locator_exp.split(">")[1])

    return element

def is_xpath(locator_xpath):
    if ("//" in locator_xpath) or ("[" in locator_xpath) or ("@" in locator_xpath):
        return True
    return False


def captureScreen():
    global driver
    try:
        png_path=os.path.join(make_time_dir(),TimeUtil().get_chinesedatetime()+".png")
        print(png_path)
        driver.get_screenshot_as_file(png_path)
    except IOError as e:
        print(e)

if __name__=="__main__":
    try:
        open_browser("chrome")
        visit("http://mail.qq.com")
        switch_to_frame("//iframe[@id='login_frame']")
        try:
            click("//a[contains(.,'帐号密码登录')]")
        except NoSuchElementException:
            traceback.print_exc()

        input("qqmail_loginPage,loginPage.user","573369709")
        input("qqmail_loginPage,loginPage.passwd","myself1314")
        click("qqmail_loginPage,loginPage.loginButton")

        click('qqmail_homePage,homePage.addressLink')
        switch_to_frame("qqmail_contactsPage,contactsPage.mainFrame")
        click("qqmail_contactsPage,contactsPage.addContactButton")

        input("qqmail_contactsPage,contactsPage.name","小小")
        # input("qqmail_contactsPage,contactsPage.email")
        # input("qqmail_contactsPage,contactsPage.tel")
        # input("qqmail_contactsPage,contactsPage.country")
        # input("qqmail_contactsPage,contactsPage.province")
        # input("qqmail_contactsPage,contactsPage.city")
        # input("qqmail_contactsPage,contactsPage.street")
        # input("qqmail_contactsPage,contactsPage.birthday")
        # input("qqmail_contactsPage,contactsPage.qq_acount")
        # click("qqmail_contactsPage,contactsPage.saveButton")


        #
        # quit()
    except AssertionError:
        traceback.print_exc()

    except Exception:
        traceback.print_exc()