#!/usr/bin/env python
# -*- coding: utf-8 -*-


import datetime  

#local
import util
import statistics

from scripts.ACM_search import ACM
from scripts.IEEE_search import IEEE
from scripts.Springer_search import Springer
from scripts.SCOPUS_search import Scopus
from scripts.Scidirect_search import Scidirect

"""
    Will handle MR exections
"""
def MPublished(engine, keywords, driver):

    #get the time using a specific format
    starting_time = datetime.datetime.now().strftime('%H:%M:%S')

    results = []

    #source search
    source_string = util.create_search_string(keywords, engine)

    #create the bots
    acm_bot = ACM(source_string,driver)
    ieee_bot = IEEE(source_string,driver)
    scidirect_bot = Scidirect(source_string,driver)
    scopus_bot = Scopus(source_string,driver)
    springer_bot = Springer(source_string,driver)

    #get the source query results
    if engine == "ACM":
        source_results = acm_bot.test_ACM()

    if engine == "IEEE":
        source_results = ieee_bot.test_IEEE()

    if engine == "Scidirect":
        source_results = scidirect_bot.test_scidirect()

    if engine == "Springer":
        source_results = springer_bot.test_springer()

    if engine == "SCOPUS":
        source_results = scopus_bot.test_Scopus()

    #get the first paper from source query
    source_papers = source_results[1]
    first_paper = source_papers[0]
    
    #get the conference of the first paper
    conferences_list = source_results[2]
    first_conference = conferences_list[0]

    #generate the followup string
    follow_string = util.create_search_string(keywords, engine, conference= first_conference)

    #create a new instance of the bots
    acm_bot = ACM(follow_string, driver)
    ieee_bot = IEEE(follow_string, driver)
    scidirect_bot = Scidirect(follow_string, driver)
    scopus_bot = Scopus(follow_string, driver)
    springer_bot = Springer(follow_string, driver)


    #get the followup query results
    if engine == "ACM":
        follow_up_results = acm_bot.test_ACM()

    if engine == "IEEE":
        follow_up_results = ieee_bot.test_IEEE()

    if engine == "Scidirect":
        follow_up_results = scidirect_bot.test_scidirect()

    if engine == "Springer":
        follow_up_results = springer_bot.test_springer()

    if engine == "SCOPUS":
        follow_up_results = scopus_bot.test_Scopus()
    
    #papers from follow up query
    followup_papers = follow_up_results[1]

    if first_paper in followup_papers:
        #working good
        fault = False
    else:
        #there is a bug
        fault = True

    results = [source_string] + source_results + [follow_string] + follow_up_results + [fault] + [starting_time]

    return results


def MPTitle(engine, keywords, driver):

    #get the time using a specific format
    starting_time = datetime.datetime.now().strftime('%H:%M:%S')

    results = []

    #source search
    source_string = util.create_search_string(keywords, engine)

    #create the bots
    acm_bot = ACM(source_string,driver)
    ieee_bot = IEEE(source_string,driver)
    scidirect_bot = Scidirect(source_string,driver)
    scopus_bot = Scopus(source_string,driver)
    springer_bot = Springer(source_string,driver)

    #get the source query results
    if engine == "ACM":
        source_results = acm_bot.test_ACM()

    if engine == "IEEE":
        source_results = ieee_bot.test_IEEE()

    if engine == "Scidirect":
        source_results = scidirect_bot.test_scidirect()

    if engine == "Springer":
        source_results = springer_bot.test_springer()

    if engine == "SCOPUS":
        source_results = scopus_bot.test_Scopus()

    #get the first paper from source query
    source_papers = source_results[1]
    first_paper = source_papers[0]
    
    #get the conference of the first paper
    conferences_list = source_results[2]
    first_conference = conferences_list[0]

    #generate the followup string
    follow_string = util.create_search_string(keywords, engine, title= first_paper)

    #create a new instance of the bots
    acm_bot = ACM(follow_string, driver)
    ieee_bot = IEEE(follow_string, driver)
    scidirect_bot = Scidirect(follow_string, driver)
    scopus_bot = Scopus(follow_string, driver)
    springer_bot = Springer(follow_string, driver)


    #get the followup query results
    if engine == "ACM":
        follow_up_results = acm_bot.test_ACM()

    if engine == "IEEE":
        follow_up_results = ieee_bot.test_IEEE()

    if engine == "Scidirect":
        follow_up_results = scidirect_bot.test_scidirect()

    if engine == "Springer":
        follow_up_results = springer_bot.test_springer()

    if engine == "SCOPUS":
        follow_up_results = scopus_bot.test_Scopus()
    
    #papers from follow up query
    followup_papers = follow_up_results[1]

    if first_paper in followup_papers:
        #working good
        fault = False
    else:
        #there is a bug
        fault = True

    results = [source_string] + source_results + [follow_string] + follow_up_results + [fault] + [starting_time]

    return results



def MPReverseJD_SwapJD(engine, keywords, driver):
    
    #get the time using a specific format
    starting_time = datetime.datetime.now().strftime('%H:%M:%S')

    results = []

    #source search
    source_string = util.create_search_string(keywords, engine)

    #create the bots
    acm_bot = ACM(source_string,driver)
    ieee_bot = IEEE(source_string,driver)
    scidirect_bot = Scidirect(source_string,driver)
    scopus_bot = Scopus(source_string,driver)
    springer_bot = Springer(source_string,driver)

    #get the source query results
    if engine == "ACM":
        source_results = acm_bot.test_ACM()

    if engine == "IEEE":
        source_results = ieee_bot.test_IEEE()

    if engine == "Scidirect":
        source_results = scidirect_bot.test_scidirect()

    if engine == "Springer":
        source_results = springer_bot.test_springer()

    if engine == "SCOPUS":
        source_results = scopus_bot.test_Scopus()
    
    #shufle the keywords
    from random import shuffle
    shuffle(keywords)

    #generate the followup string
    follow_string = util.create_search_string(keywords, engine)

    #create a new instance of the bots
    acm_bot = ACM(follow_string, driver)
    ieee_bot = IEEE(follow_string, driver)
    scidirect_bot = Scidirect(follow_string, driver)
    scopus_bot = Scopus(follow_string, driver)
    springer_bot = Springer(follow_string, driver)


    #get the followup query results
    if engine == "ACM":
        follow_up_results = acm_bot.test_ACM()

    if engine == "IEEE":
        follow_up_results = ieee_bot.test_IEEE()

    if engine == "Scidirect":
        follow_up_results = scidirect_bot.test_scidirect()

    if engine == "Springer":
        follow_up_results = springer_bot.test_springer()

    if engine == "SCOPUS":
        follow_up_results = scopus_bot.test_Scopus()


    #get the first paper from source query
    num_source = source_results[0]
    source_papers = source_results[1]
    
    #get followup results
    num_followup = follow_up_results[0]
    followup_papers = follow_up_results[1]
    
    #If the number of results is diferent then found a anomaly
    if num_source == num_followup:
        anon = False
    else:
        anon = True

    #check similarity from both results
    jaccard = statistics.check_similarity(source_papers, followup_papers)

    results = [source_string] + source_results + [follow_string] + follow_up_results + [anon] + [jaccard] + [starting_time]

    return results



def Top1Absent(engine, keywords, driver):

    #get the time using a specific format
    starting_time = datetime.datetime.now().strftime('%H:%M:%S')

    results = []

    #source search
    source_string = util.create_search_string(keywords, engine)

    #create the bots
    acm_bot = ACM(source_string,driver)
    ieee_bot = IEEE(source_string,driver)
    scidirect_bot = Scidirect(source_string,driver)
    scopus_bot = Scopus(source_string,driver)
    springer_bot = Springer(source_string,driver)

    #get the source query results
    if engine == "ACM":
        source_results = acm_bot.test_ACM()

    if engine == "IEEE":
        source_results = ieee_bot.test_IEEE()

    if engine == "Scidirect":
        source_results = scidirect_bot.test_scidirect()

    if engine == "Springer":
        source_results = springer_bot.test_springer()

    if engine == "SCOPUS":
        source_results = scopus_bot.test_Scopus()

    #get the first paper from source query
    source_papers = source_results[1]
    first_paper = source_papers[0]
    
    #get the conference of the first paper
    conferences_list = source_results[2]
    first_conference = conferences_list[0]

    #generate the followup string
    follow_string = util.create_search_string(keywords, engine, title= first_paper)

    #create a new instance of the bots
    acm_bot = ACM(follow_string, driver)
    ieee_bot = IEEE(follow_string, driver)
    scidirect_bot = Scidirect(follow_string, driver)
    scopus_bot = Scopus(follow_string, driver)
    springer_bot = Springer(follow_string, driver)


    #get the followup query results
    if engine == "ACM":
        follow_up_results = acm_bot.test_ACM()

    if engine == "IEEE":
        follow_up_results = ieee_bot.test_IEEE()

    if engine == "Scidirect":
        follow_up_results = scidirect_bot.test_scidirect()

    if engine == "Springer":
        follow_up_results = springer_bot.test_springer()

    if engine == "Scopus":
        follow_up_results = scopus_bot.test_Scopus()
    
    #papers from follow up query
    followup_papers = follow_up_results[1]

    #check if the first paper of both query is equal
    if first_paper == followup_papers[0]:
        #working good
        fault = False
    else:
        #there is a bug
        fault = True

    results = [source_string] + source_results + [follow_string] + follow_up_results + [fault] + [starting_time]

    return results