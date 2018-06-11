#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import csv

#selenium
from selenium import webdriver


#local
import util
import metamorphic_relations


"""
    run source and follow_up queries and store results in a file
"""
def execute_query(dataset_file, results_file, engine, m_relation, driver):
    
    keywords = []
    results = []
    
    #open dataset file
    with open(dataset_file, "r") as dataset:

        #get keywords
        keywords = util.random_keywords(dataset) 


    #gathering results for any metamorphic relation      

    if m_relation == "MPublished":
        results = metamorphic_relations.MPublished(engine, keywords, driver)

    if m_relation == "MPTitle":
        results = metamorphic_relations.MPTitle(engine, keywords, driver)

    if (m_relation == "MPReverseJD") or (m_relation == "SwapJD"):
        results = metamorphic_relations.MPReverseJD_SwapJD(engine, keywords, driver)

    if m_relation == "Top1Absent":
        results = metamorphic_relations.Top1Absent(engine, keywords, driver)

    #saving results into CSV file
    with open(results_file, "a") as sheet_results:
        out = csv.writer(sheet_results, delimiter=',',quoting=csv.QUOTE_ALL)
        out.writerow(results)

    

if __name__ == '__main__':
    
    #build driver path
    base_dir = '/home/stevao/workspace/mt_project'
    driver_path = base_dir + '/scripts/drivers/chromedriver'
    driver = webdriver.Chrome(driver_path)

    dataset_file = base_dir + "/dataset/keywords_sample.csv"
    
    engines = ["ACM", "IEEE", "Scidirect", "Scopus", "Springer"]
    relations = ["MPublished", "MPTitle", "MPReverseJD", "SwapJD","Top1Absent"] 

    #Verify the execution
    if len(sys.argv) < 3:
        print('Usage: python experiment.py engine, relation')
        sys.exit(-1)


    engine    = str(sys.argv[1]) #engine used
    relation  = str(sys.argv[2]) #metamorphic relation
    
    if engine not in engines:
        print('Please use a valid engine: ', engines)
        sys.exit(-1)

    if relation not in relations:
        print('Please use a valid metamorphic relation: ', relations)
        sys.exit(-1)

    #creating a result file
    file_name = engine + '_' + relation + '.csv'

    result_dir = base_dir + '/results'

    #check the directory result..
    try:
        #check the status of the dir to generate a exception if it not exists	
        os.stat(result_dir)
    except:
        #when the exception is triged create the directory
        os.mkdir(result_dir)

    #destination path
    results_file = result_dir + '/' + file_name

    #run a test with 20 queries
    for i in range(20):
        execute_query(dataset_file, results_file,engine, relation, driver)