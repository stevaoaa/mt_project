# -*- coding: utf-8 -*-

#local
import util

import locale

import unittest, time, re

from six.moves import reload_module

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import sys

class IEEE(unittest.TestCase):

    def __init__(self, stringBusca, webDriver):
        locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
        #locale.setlocale(locale.LC_ALL, 'English_United States.1252')
        self.stringBusca = stringBusca
        self.webDriver = webDriver

    def setUp(self):
        self.driver = self.webDriver
        self.driver.implicitly_wait(30)
        self.base_url = "https://ieeexplore.ieee.org/search/advsearch.jsp?expression-builder"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_IEEE(self):

        self.setUp()

        reload_module(sys)
        # sys.setdefaultencoding('utf8')

        driver = self.driver
        driver.get(self.base_url)

        driver.find_element_by_css_selector("#command-search-tab > a > span").click()

        import time
        time.sleep(5)

        driver.find_element_by_id("expression-textarea").clear()        
        driver.find_element_by_id("expression-textarea").send_keys(self.stringBusca)

        element = driver.find_element_by_id("submit-search")
        driver.execute_script("arguments[0].click();", element)

        try:
            numberResult = locale.atoi(driver.find_element_by_xpath("//div[@id='xplResultsContainer']/section/div[2]/div/span/span[2]").text)
            
            #numResultPage = driver.find_element_by_css_selector("span.ng-scope > span.strong.ng-binding").text
            #nPage1 = numResultPage.find("-")
            #nPage2 = numResultPage[nPage1 + 1:nPage1 + 3]
            #numberResultPage = int(nPage2)

            artigos_list = []
            published_list = []

            WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "article-list")))

            # List-results-items
            if (len(driver.find_elements_by_xpath("//span[@class='strong ng-binding']")) > 0):
                numArtigos_Pagina = int(
                    str(driver.find_elements_by_xpath("//span[@class='strong ng-binding']")[0].text)[2:])
            else:
                numArtigos_Pagina = int(
                    str(driver.find_elements_by_xpath("//span[@class='strong']")[0].text))

            while (len(driver.find_elements_by_class_name("List-results-items")) < numArtigos_Pagina):
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            resultItems = driver.find_elements_by_class_name("List-results-items")
            cont = 0

            for result in resultItems:
                cont += 1
                titleFollowUP = result.find_elements_by_class_name("col-22-24")[0].find_elements_by_tag_name("a")[
                    0].get_attribute("innerHTML").replace("[::", "").replace("::]", "")
                artigos_list.append(titleFollowUP)
                publishedFollowUP = \
                    result.find_elements_by_class_name("col-22-24")[0].find_elements_by_class_name("description")[
                        0].find_elements_by_tag_name("a")[0].get_attribute("innerHTML").replace("[::", "").replace(
                        "::]", "")
                published_list.append(publishedFollowUP)
            
            #remove possible HTML markups and HTML Codes
            artigos_list = util.format_results(artigos_list)
            published_list = util.format_results(published_list)

            return [numberResult, artigos_list, published_list]
        except Exception as e:
            print("E: Exception while extracting IEEE information!\n{string}".format(string = self.stringBusca))
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
    