#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import csv
import datetime  

#selenium
from selenium import webdriver


#local
import util
from scripts.ACM_search import ACM
from scripts.IEEE_search import IEEE
from scripts.Springer_search import Springer
from scripts.SCOPUS_search import Scopus
from scripts.Scidirect_search import Scidirect

"""
    run source and follow_up queries and store results in a file
"""
def source_followup_execution(dataset_file, results_file, engine, driver):
    
    #get the time using a specific format
    starting_time = datetime.datetime.now().strftime('%H:%M:%S')

    results = []

    #open dataset file
    with open(dataset_file, "r") as dataset:

        #get keywords
        keywords = util.random_keywords(dataset) 
        print (keywords)
        #gathering results for any metamorphic relation
            

    if engine == "ACM":

        #source search
        source_string = util.create_search_string(keywords, engine)

        #create the bot
        acm_bot = ACM(source_string,driver)

        #get the source query results
        source_results = acm_bot.test_ACM()
        
        #get the first paper from source query
        papers_list = source_results[1]
        first_paper = papers_list[0]
        print(source_results[0])
        
        #generate the followup string
        follow_string = util.create_search_string(keywords, engine, first_paper)

        #create the bot
        acm_bot = ACM(follow_string, driver)

        #run the followup query
        follow_up_results = acm_bot.test_ACM()
        print(follow_up_results[0])


    if engine == "IEEE":
        pass

    if engine == "Scidirect":
        pass

    if engine == "SCOPUS":
        pass

    #begging of the operation
    results.append(starting_time)

    #saving results into CSV file
    with open(results_file, "wb") as sheet_results:
        out = csv.writer(sheet_results, delimiter=',',quoting=csv.QUOTE_ALL)
        out.writerow(results)

    

if __name__ == '__main__':
    
    #build driver path
    base_dir = '/home/stevao/workspace'
    source_dir = base_dir + '/mt_project/scripts/drivers/chromedriver'
    driver = webdriver.Chrome(source_dir)

    dataset_file = os.getcwd() + "/dataset/keywords_sample.csv"
    results_file = os.getcwd() + "misa_gato.csv"

    #run a test 
    source_followup_execution(dataset_file, results_file,"ACM",driver)