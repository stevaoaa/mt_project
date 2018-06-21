#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import re
import random

import html.parser

from datetime import datetime
from datetime import timedelta

#local
import engines_string_generator as engines

"""
    (Waterman's "Reservoir Algorithm") from Knuth's "The Art of Computer Programming"
    #https://stackoverflow.com/questions/3540288/how-do-i-read-a-random-line-from-one-file-in-python
"""
def random_line(afile):
    
    afile.seek(0)
    line = next(afile)
    for num, aline in enumerate(afile):
      if random.randrange(num + 2): continue
      line = aline

    #some keywords have a description. Eg.: Exploit (computer security) -> remove content surrounded by (). 
    new_line = re.sub(r'\([^)]*\)', '', line)
    return new_line


"""
    Given a csv file pickup a random line with a list of keywords
"""
def random_keywords(afile):
    keywords = []

    #convert the csv line entry into a list 
    line = random_line(afile)
    line = line.strip()
    keywords = line.split(",")

    #avoid entrys with less than 2 keywords or empyt lines
    if len(keywords) <2 or (keywords == None):
        return random_keywords(afile)
    else:
        
        if len(keywords) > 4:
            return keywords[:4]
        
        return keywords

"""
    Given a file turn it into a list
"""
def file_in_list(afile):

    result = []

    #just run into the lines of the file and append the to a list
    for line in afile:
        line = line.strip()
        result.append(line)

    return result

"""
    Calculate elapsed time between two dates
    #https://stackoverflow.com/questions/3096953/how-to-calculate-the-time-interval-between-two-time-strings
"""
def calculate_elapsed_time(s1, s2):
    
    # for example
    #s1 = '10:33:26'
    #s2 = '11:33:26' 
    
    #formmat
    FMT = '%H:%M:%S'

    tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
    
    #avoid issues turning the day
    if tdelta.days < 0:
        tdelta = timedelta(days=0, seconds=tdelta.seconds, microseconds=tdelta.microseconds)
    
    return tdelta


def create_search_string(keywords, engine, title = None, conference = None):
    
    if engine == "ACM":

        if ((not title) and (not conference)):
            search_string = engines.acm_string(keywords)
        
        if title:
            search_string = engines.acm_string(keywords, title = title)

        if conference:
            search_string = engines.acm_string(keywords, conference = conference)
        
        return search_string

    if engine == "IEEE":

        if ((not title) and (not conference)):
            search_string = engines.ieee_string(keywords)

        if title:
            search_string = engines.ieee_string(keywords, title = title)

        if conference:
            search_string = engines.ieee_string(keywords, conference = conference)
                
        return search_string

    if engine == "Scidirect":

        if ((not title) and (not conference)):
            search_string = engines.sciente_direct_string(keywords)        

        if title:
            search_string = engines.sciente_direct_string(keywords, title = title)

        if conference:
            search_string = engines.sciente_direct_string(keywords, conference = conference)

        return search_string

    if engine == "Scopus":

        if ((not title) and (not conference)):
            search_string = engines.scopus_string(keywords)

        if title:
            search_string = engines.scopus_string(keywords, title = title)

        if conference:
            search_string = engines.scopus_string(keywords, conference = conference)
        
        return search_string

    if engine == "Springer":

        if ((not title) and (not conference)):
            search_string = engines.spring_string(keywords)

        if title:
            search_string = engines.spring_string(keywords, title = title)

        if conference:
            search_string = engines.spring_string(keywords, conference = conference)

        return search_string


"""
    Remove HTML tags from results (it occours on IEEE results)
    Udacity solution: https://www.youtube.com/watch?v=HPkNPcYed9M&feature=youtu.be&t=35s
"""
def remove_html_markup(s):
    
    tag = False
    quote = False
    out = ""

    for c in s:
            if c == '<' and not quote:
                tag = True
            elif c == '>' and not quote:
                tag = False
            elif (c == '"' or c == "'") and tag:
                quote = not quote
            elif not tag:
                out = out + c
    return out


"""
    Given a list, for each element remove HTML tags and decode ASCII characters 
"""
def format_results(unformated_results):

    formated_results = []
    for entry in unformated_results:
        
        #remove HTML tags
        entry = remove_html_markup(entry)
        
        #convert HTML ASCII codes
        """
            ("'", '&#39;'),
            ('"', '&quot;'),
            ('>', '&gt;'),
            ('<', '&lt;'),
            ('&', '&amp;')
        """ 
        entry = html.parser.unescape(entry)
        formated_results.append(entry)

    return formated_results
    