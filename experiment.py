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

    if engine == "ACM":

        if m_relation == "MPublished":
            results = metamorphic_relations.MPublished(engine, keywords, driver)

        if m_relation == "MPTitle":
            pass

        if (m_relation == "MPReverseJD") or (m_relation == "SwapJD"):
            pass

        if m_relation == "Top1Absent":
            pass

    if engine == "IEEE":
        
        if m_relation == "MPublished":
            results = metamorphic_relations.MPublished(engine, keywords, driver)

        if m_relation == "MPTitle":
            pass

        if (m_relation == "MPReverseJD") or (m_relation == "SwapJD"):
            pass

        if m_relation == "Top1Absent":
            pass


    if engine == "Scidirect":
        
        if m_relation == "MPublished":
            results = metamorphic_relations.MPublished(engine, keywords, driver)

        if m_relation == "MPTitle":
            pass

        if (m_relation == "MPReverseJD") or (m_relation == "SwapJD"):
            pass

        if m_relation == "Top1Absent":
            pass


    if engine == "SCOPUS":
        
        if m_relation == "MPublished":
            results = metamorphic_relations.MPublished(engine, keywords, driver)

        if m_relation == "MPTitle":
            pass

        if (m_relation == "MPReverseJD") or (m_relation == "SwapJD"):
            pass

        if m_relation == "Top1Absent":
            pass


    if engine == "Springer":
        
        if m_relation == "MPublished":
            results = metamorphic_relations.MPublished(engine, keywords, driver)

        if m_relation == "MPTitle":
            pass

        if (m_relation == "MPReverseJD") or (m_relation == "SwapJD"):
            pass

        if m_relation == "Top1Absent":
            pass


    #saving results into CSV file
    with open(results_file, "a") as sheet_results:
        out = csv.writer(sheet_results, delimiter=',',quoting=csv.QUOTE_ALL)
        out.writerow(results)

    

if __name__ == '__main__':
    
    #build driver path
    base_dir = '/home/stevao/workspace'
    source_dir = base_dir + '/mt_project/scripts/drivers/chromedriver'
    driver = webdriver.Chrome(source_dir)

    dataset_file = os.getcwd() + "/dataset/keywords_sample.csv"
    results_file = os.getcwd() + "/misa_gato.csv"

    #run a test 
    execute_query(dataset_file, results_file,"IEEE", "MPublished", driver)