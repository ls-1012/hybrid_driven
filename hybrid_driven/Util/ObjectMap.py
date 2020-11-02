#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# File:         ObjectMap.py
# Author:       ls
# Date:         2020/10/14 16:40
#-------------------------------------------------------------------------------

from selenium import webdriver
from selenium.common.exceptions import WebDriverException, NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
import traceback
import time
from .Log import *

my_log = MyLog()
log = my_log.get_logger()
# 查找一个元素的封装
def find_element(driver,locate_method,locate_exp):
    try:
        # 设置超时时间，超时后报异常
        log.info("locate_method:%s,locate_exp:%s" %(locate_method,locate_exp))
        element=WebDriverWait(driver,10).until(lambda x:x.find_element(locate_method,locate_exp))

        return element
    except TimeoutException as e:
        traceback.print_exc()
        raise e

    except NoSuchElementException as e:
        traceback.print_exc()
        raise e

    except WebDriverException as e:
        traceback.print_exc()
        raise e

# 查找多个元素的封装
def find_elements(driver, locate_method, locate_exp):
    try:
        elements = WebDriverWait(driver, 10).until(lambda x: x.find_elements(locate_method, locate_exp))
        # print("element: ", elements)

        return elements

    except NoSuchElementException as e:
        traceback.print_exc()
        raise e

    except WebDriverException as e:
        traceback.print_exc()
        raise e

if __name__=='__main__':
    driver=webdriver.Chrome(executable_path='d:/chromedriver')
    driver.get("http://mail.qq.com")

    # input_box=driver.find_element("id","query")
    # input=driver.find_element_by_xpath("//*[@class='s-top-login-btn c-btn c-btn-primary c-btn-mini lb']")
    # #获取href属性的值，就获取到了链接
    # print(input.get_attribute("href"))
    # #完整的获取这个元素对应的html
    # print(input.get_attribute("outerHTML"))
    # #获取 该元素的内部的html源代码
    # print(input.get_attribute("innerHTML"))
    # driver.switch_to.frame("login_frame")
    frameid=find_element(driver,"xpath","//*[@id='login_frame']")
    print("frameid",frameid)
    driver.switch_to.frame(frameid)
    input_box=find_element(driver,"id","u")
    print(input_box)
    input_box.send_keys("光荣之路")

    # # 拿到页面的源码，一般可以用于断言
    # pagesource=driver.page_source


    # 下面这个方法等价于driver.find_element_by_id("kw")
    # from selenium.webdriver.common.by import By
    # element = driver.find_element(by=By.ID, value="kw")

    # input_eles = find_elements(driver, "xpath", "//input")
    # print(len(input_eles))
    # time.sleep(5)
    driver.quit()