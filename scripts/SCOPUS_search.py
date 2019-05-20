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

class Scopus(unittest.TestCase):

    def __init__(self, stringBusca, webDriver):
        
        self.stringBusca = stringBusca
        self.webDriver = webDriver

    def setUp(self):
        self.driver = self.webDriver
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.scopus.com/search/form.uri?display=advanced&/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_Scopus(self):

        self.setUp()

        reload_module(sys)
        # sys.setdefaultencoding('utf8')

        driver = self.driver
        driver.get(self.base_url)
        
        try:
            driver.find_element_by_id("clearLink").click()
        except:
            pass

        driver.find_element_by_id("searchfield").send_keys(self.stringBusca)
        element = driver.find_element_by_id("advSearch")

        time.sleep(5)

        driver.execute_script("arguments[0].click();", element)
        artigos_list = []
        published_list = []

        try:
            numResultados_source = locale.atoi(driver.find_element_by_class_name("resultsCount").text)
            #trFirstResult = driver.find_element_by_id("resultDataRow0")
            tBodyResults = driver.find_element_by_id("srchResultsList").find_element_by_tag_name("tbody").find_elements_by_class_name("searchArea")

            for result in tBodyResults:
                artigos_list.append(result.find_elements_by_tag_name("td")[0].find_elements_by_tag_name("a")[0].text)
                try:
                    published_list.append((result.find_elements_by_tag_name("td")[3].find_elements_by_tag_name("a")[0].text))
                except:
                    strf = result.find_elements_by_tag_name("td")[3].text
                    var =  ""

                    for c in strf:
                        if (c.isdigit()):
                            break
                    var = var + c
                    published_list.append(var)

            #remove possible HTML markups and HTML Codes
            artigos_list = util.format_results(artigos_list)
            published_list = util.format_results(published_list)
            
            return [numResultados_source, artigos_list, published_list]
        except Exception as e:
            print("E: Exception while extracting Scopus information!\n{string}".format(string = self.stringBusca))
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
    