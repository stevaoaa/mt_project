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

class Scidirect(unittest.TestCase):

    def __init__(self, stringBusca, webDriver):
        
        self.stringBusca = stringBusca
        self.webDriver = webDriver

    def setUp(self):
        self.driver = self.webDriver
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.sciencedirect.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_scidirect(self,title = None, conference = None):

        self.setUp()

        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("Advanced search").click()
        driver.find_element_by_id("qs").clear()
        driver.find_element_by_id("qs").send_keys(self.stringBusca)
        if title:
            driver.find_element_by_id("tak").send_keys(title)
        
        if conference:
            driver.find_element_by_id("pub").send_keys(conference)

        element = driver.find_element_by_xpath("//button[@type='submit']")
        driver.execute_script("arguments[0].click();", element)

        try:
        
            if (len(driver.find_elements_by_css_selector("span.search-body-results-text")) > 0):
                numResults = driver.find_element_by_css_selector("span.search-body-results-text").text
            else:
                numResults = driver.find_element_by_css_selector("h1.search-body-results-text").text
            
            numResults = locale.atoi(numResults.split()[0])
            numResultsPage = driver.find_elements_by_class_name("SearchNavigation")[0].find_elements_by_class_name("active-per-page")[0].text
            numResultsPage = locale.atoi(numResultsPage.split()[0])
            if numResults < numResultsPage:
                numResultsPage = numResults

            artigos_list = []
            published_list = []

            for i in range(0, numResultsPage):

                resultItems = driver.find_elements_by_class_name("ResultList")[0].find_elements_by_class_name("ResultItem")[i]
                artigos_list.append(resultItems.find_elements_by_tag_name("a")[0].text)
                published_list.append(resultItems.find_elements_by_class_name("subtype-srctitle-link")[0].text)

            #remove possible HTML markups and HTML Codes
            artigos_list = util.format_results(artigos_list)
            published_list = util.format_results(published_list)

            return [numResults, artigos_list, published_list]
        except Exception as e:
            print("E: Exception while extracting Science Direct information!\n{string}".format(string = self.stringBusca))
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