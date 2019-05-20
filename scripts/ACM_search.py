# -*- coding: utf-8 -*-

#local
import util

import sys
import locale

from six.moves import reload_module

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


class ACM(unittest.TestCase):

	def __init__(self, stringBusca, webDriver):
		
		self.stringBusca = stringBusca
		self.webDriver = webDriver

	def setUp(self):
		self.driver = self.webDriver
		self.driver.implicitly_wait(30)
		self.base_url = "https://dl.acm.org/advsearch.cfm?coll=DL&dl=ACM#"
		self.verificationErrors = []
		self.accept_next_alert = True

	def test_ACM(self):

		self.setUp()

		reload_module(sys)
		#sys.setdefaultencoding('utf8')

		driver = self.driver
		driver.get(self.base_url)

		if (not (driver.find_element_by_id("therunqueryedit").is_displayed())):
			driver.find_element_by_id("vh").click()
		driver.find_element_by_id("therunqueryedit").send_keys(self.stringBusca)
		time.sleep(2)
		driver.find_element_by_name("Go").click()

		try:			
			trFirstResult = driver.find_elements_by_id("results")[0].find_elements_by_class_name("details")[0]
			trNumberResult = driver.find_elements_by_id("resultstats")[0].find_elements_by_id("resfound")[0]
			numberResult = locale.atoi(trNumberResult.find_elements_by_id("searchtots")[0].find_elements_by_tag_name("strong")[0].text)
			numberPage = driver.find_elements_by_id("results")[0].find_elements_by_class_name("pagerange")[0].text
			nPage1 = numberPage.find("of")
			nPage2 = numberPage.find("–")
			nPage3 = numberPage[nPage2+2:nPage1-1]
			numberResultPage = locale.atoi(nPage3)
			artigos_list = []
			published_list = []

			for i in range(0,numberResultPage):
				trFirstResult = driver.find_elements_by_id("results")[0].find_elements_by_class_name("details")[i]
				artigos_list.append(trFirstResult.find_elements_by_class_name("title")[0].find_elements_by_tag_name("a")[0].text)
				if (len(trFirstResult.find_elements_by_class_name("source")[0].find_elements_by_tag_name("span")) < 2):
					numberResult -= 1
				else:
					published_list.append(trFirstResult.find_elements_by_class_name("source")[0].find_elements_by_tag_name("span")[1].text)
			
            #remove possible HTML markups and HTML Codes
			artigos_list = util.format_results(artigos_list)
			published_list = util.format_results(published_list)
			
			return [numberResult, artigos_list, published_list]
		except Exception as e:
			print("E: Exception while extracting ACM information!\n{string}".format(string = self.stringBusca))
			print(e)
			return [0, [], []]

	def is_element_present(self, how, what):

		try:
			self.driver.find_element(by=how, value=what)
		except NoSuchElementException as e:
			print(e)
			return False
		return True

	def is_alert_present(self):

		try:
			self.driver.switch_to_alert()
		except NoAlertPresentException as e:
			print(e)
			return False
		return True

	def close_alert_and_get_its_text(self):

		try:
			alert = self.driver.switch_to_alert()
			alert_text = alert.text
			if self.accept_next_alert:
				alert.accept()	
			else:
				alert.dismiss()
			return alert_text
		finally:
			self.accept_next_alert = True

	def tearDown(self):
		self.driver.quit()
		self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
	unittest.main()
	