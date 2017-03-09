# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import unittest
driver = webdriver.Chrome()
driver.get("http://www.gftbank.cn/")

driver.find_element_by_xpath('html/body/header/div[1]/div/ul[2]/li[2]/a').click()
time.sleep(1)
driver.find_element_by_id('signUp_btn').click()
time.sleep(2)
driver.find_element_by_xpath(".//*[@id='layui-layer1']/div[3]/a").click()