# -*- coding: utf-8 -*-

#local
import util

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
import sys

class Springer(unittest.TestCase):

    def __init__(self, stringBusca, webDriver):

        self.stringBusca = stringBusca
        self.webDriver = webDriver

    def setUp(self):
        self.driver = self.webDriver
        self.driver.implicitly_wait(30)
        self.base_url = "https://link.springer.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_springer(self):

        self.setUp()

        reload(sys)
        # sys.setdefaultencoding('utf8')

        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("query").send_keys(self.stringBusca)
        driver.find_element_by_id("search").click()

        try:
            numberResult = locale.atoi(driver.find_elements_by_tag_name("h1")[0].find_elements_by_tag_name("strong")[0].text)
            
            tBodyResults = driver.find_elements_by_id("results-list")[0].find_elements_by_tag_name("li")
            artigos_list = []
            published_list = []

            for result in tBodyResults:
                if (len(result.find_elements_by_class_name("content-type")) == 0):
                    numberResult -= 1
                else: 
                    type_public = result.find_elements_by_class_name("content-type")[0].text
                
                    if type_public != "Book":
                        artigos_list.append(result.find_elements_by_tag_name("h2")[0].find_elements_by_tag_name("a")[0].text)
                        if (len(result.find_elements_by_class_name("meta")) == 0):
                            published_list.append('')
                        else:
                            if (len(result.find_elements_by_class_name("meta")[0].find_elements_by_class_name("enumeration")) == 0):
                                numberResult -= 1
                            else:
                                eleme1 = result.find_elements_by_class_name("meta")[0].find_elements_by_class_name("enumeration")[0]
                                if (len(eleme1.find_elements_by_tag_name("a")) == 0):
                                    numberResult -= 1
                                else:
                                    elem2 = eleme1.find_elements_by_tag_name("a")[0].get_attribute("title")
                                    published_list.append(elem2)
                    else:
                        numberResult -= 1

            #remove (content inside parenthesis) of published list to avoid break follow-up query
            import re
            published_list = [re.sub(r" ?\([^)]+\)", "", item) for item in published_list]

            return [numberResult, artigos_list, published_list]
        except Exception as e:
            print("E: Exception while extracting Springer information!\n{string}".format(string = self.stringBusca))
            print(e)
            return [0, [], []]
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: 
            print(e)
            return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
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
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
	unittest.main()


