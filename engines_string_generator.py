#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Some functions to build suitable search strings for each base
"""
def scopus_string(keywords, title = None, conference = None):

    #use the keywords to build a suitable string
    terms = ' OR '
    terms = terms.join('"{0}"'.format(w) for w in keywords)

    scopus = "TITLE-ABS-KEY (%s)" % (terms)

    #Scopus
    if title:        
        scopus = "TITLE-ABS-KEY (%s)" % (terms)
        complement = " AND TITLE (\"%s\")" % (title)
        scopus = scopus + complement
    
    if conference:
        scopus = "TITLE-ABS-KEY (%s)" % (terms)
        complement = " AND SRCTITLE: (\"%s\")" % (conference)
        scopus = scopus + complement

    return scopus

def ieee_string(keywords, title= None, conference = None):
    
    #use the keywords to build a suitable string
    terms = ' OR '
    terms = terms.join('"{0}"'.format(w) for w in keywords)    

    #IEEE
    ieee = "((\"Document Title\":\"%s\"))" % (terms)
    if title:        

        ieee = "((\"Document Title\":\"%s\"))" % (terms)
        complement = " AND (\"Document Title\": \"%s\")"  % (title)
        ieee = ieee + complement

    if conference:
        
        ieee = "((\"Document Title\":\"%s\"))" % (terms)
        complement = " AND (\"Publication Title\": \"%s\")"  % (conference)
        ieee = ieee + complement

    return ieee

def spring_string(keywords, title= None, conference = None):
    
    #use the keywords to build a suitable string
    terms = ' OR '
    terms = terms.join('"{0}"'.format(w) for w in keywords)    

    #IEEE or Springer
    springer = "(%s)" % (terms)
    
    if title:        

        springer = "(%s)" % (terms)
        complement = " AND (title: \"%s\")"  % (title)
        springer = springer + complement

    if conference:        

        springer = "(%s)" % (terms)
        complement = " AND (publication-title: \"%s\")"  % (conference)
        springer = springer + complement

    return springer


def sciente_direct_string(keywords, title = None, conference = None):

    #Sciente Direct   
    terms = ' OR '
    terms = terms.join('Title-Abstr-Key('"{0}"') '.format(w) for w in keywords)
    
    direct =  terms    

    if title:        

        complement = " AND Title(\"%s\")" % (title)
        direct = direct + complement

    if conference:        

        complement = " AND Title(\"%s\")" % (conference)
        direct = direct + complement

    return direct


def acm_string(keywords, title = None, conference = None):
    
    terms = ' OR '
    terms = terms.join('((acmdlTitle:(+"{0}") OR recordAbstract:(+"{0}") OR keywords.author.keyword:(+"{0}"))'.format(w) for w in keywords)    
    
    acm = terms

    if title:        
        complement = " AND (acmdlTitle:(+\"%s\"))" % (title)
        acm = acm + complement

    if conference:        
        complement = " AND (\"publication name\":(\"%s\"))" % (conference)
        acm = acm + complement

    return acm
    