#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import datetime

import unittest

#selenium
from selenium import webdriver

#local
import util
import engines_string_generator
from analyzes import metrics 


from scripts.ACM_search import ACM
from scripts.IEEE_search import IEEE
from scripts.Springer_search import Springer
from scripts.SCOPUS_search import Scopus
from scripts.Scidirect_search import Scidirect


"""
    This class simple execute some functions in order to see how things are going until mix all things together
"""

def test_random_line():

    path_file = os.getcwd() + "/dataset/keywords_sample.csv"

    with open(path_file, "r") as afile:
        line = util.random_line(afile)
    
    print(("A random line from a file: %s") % (line))


def test_random_keywords():
    
    path_file = os.getcwd() + "/dataset/keywords_sample.csv"

    with open(path_file, "r") as afile:
        keywords = util.random_keywords(afile)
    
    print(("A random keywords list from a file: %s") % (keywords))


def test_file_in_list():
    path_file = os.getcwd() + "/dataset/keywords_sample.csv"

    with open(path_file, "r") as afile:
        alist = util.file_in_list(afile)
    
    print(("A list from a file: %s") % (alist[:2]))


def test_calculate_elapsed_time():
    
    # for example
    s1 = str(datetime.datetime.now().strftime('%H:%M:%S'))
    time.sleep(1) #wait one second
    s2 = str(datetime.datetime.now().strftime('%H:%M:%S'))

    delta = util.calculate_elapsed_time(s1,s2) 
    
    #difference between 2 dates in '%H:%M:%S' format
    print(("Difference between dates: %s") % (delta))

    
#metrics.py tests
def test_check_similarity():
    
    path_file = os.getcwd() + "/dataset/keywords_sample.csv"

    with open(path_file, "r") as afile:
        alist = util.file_in_list(afile)

    #calculate jaccard wit a list and the same list reversed. Should be lower
    jaccard = metrics.check_similarity(alist, alist[::-1])
    print(("Jaccard Coefficient: %s") % (jaccard)) 


def test_get_ROCOF():
    path_file = os.getcwd() + "/dataset/keywords_sample.csv"
    with open(path_file, "r") as afile:
        first_line = next(afile)

    #get the last element (thus, the time of execution)
    last_element = first_line[-1]
    print(last_element)


def test_create_search_string():

    path_file = os.getcwd() + "/dataset/keywords_sample.csv"

    with open(path_file, "r") as afile:
        keywords = util.random_keywords(afile)

        result = engines_string_generator.ieee_string(keywords,title="Some title of test")
        print("IEEE|Springer String: %s" % (result))

        result = engines_string_generator.spring_string(keywords,title="Some title of test")
        print("Springer String: %s" % (result))

        result = engines_string_generator.scopus_string(keywords,title="Some title of test")
        print("Scopus String: %s" % (result))

        result = engines_string_generator.sciente_direct_string(keywords,title="Some title of test")
        print("Science Direct String: %s" % (result))

        result = engines_string_generator.acm_string(keywords,title="Some title of test")
        print("ACM String: %s" % (result))


def test_run_a_query(engine, keywords, driver):
    
    title = 'Need a bigger string to simulate a cenario that that exceeds the maximum size allowed by the search base science direct'

    #generate string
    source_string = util.create_search_string(keywords, engine, title= title)

    print("String: ", source_string)

    #create the bots
    acm_bot = ACM(source_string,driver)
    ieee_bot = IEEE(source_string,driver)
    scidirect_bot = Scidirect(source_string,driver)
    scopus_bot = Scopus(source_string,driver)
    springer_bot = Springer(source_string,driver)

    source_results = []

    #get the source query results
    if engine == "ACM":
        source_results = acm_bot.test_ACM()

    if engine == "IEEE":
        source_results = ieee_bot.test_IEEE()

    if engine == "Scidirect":
        source_results = scidirect_bot.test_scidirect()

    if engine == "Springer":
        source_results = springer_bot.test_springer()

    if engine == "Scopus":
        source_results = scopus_bot.test_Scopus()

def test_check_similarity_from_file():
    
    base_dir = os.getcwd()
    afile = "Top1Absent_IEEE_v2.csv"
    file_path = base_dir + "/results/" + afile
    
    metrics.check_results(file_path)

if __name__ == '__main__':
    
    #parameters
    engine = "Scidirect"
    keywords = ["Adaptive system", "Computer science", "Computer virus", "Electrical engineering"]
    
    #build driver path
    base_dir = os.getcwd()
    driver_path = base_dir + '/scripts/drivers/chromedriver'
    #driver = webdriver.Chrome(driver_path)

    #run a execution here
    test_check_similarity_from_file()