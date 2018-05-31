#!/usr/bin/env python
# -*- coding: utf-8 -*-

def scopus_string(keywords, follow_up= False):

    #use the keywords to build a suitable string
    terms = ' OR '
    terms = terms.join('"{0}"'.format(w) for w in keywords)

    scopus = "TITLE-ABS-KEY (%s)" % (terms)

    #Scopus
    if follow_up:        
        scopus = "TITLE-ABS-KEY (%s)" % (terms)
        complement = " AND ({1})"
        scopus = scopus + complement
    
    return scopus

def ieee_spring_string(keywords, follow_up= False):
    
    #use the keywords to build a suitable string
    terms = ' OR '
    terms = terms.join('"{0}"'.format(w) for w in keywords)    

    #IEEE or Springer
    ieee = "source-query (%s)" % (terms)
    if follow_up:        

        ieee = "source-query (%s)" % (terms)
        complement = " AND (\"Document Title\":\"{1}\"))"
        ieee = ieee + complement
    return ieee


def sciente_direct_string(keywords, follow_up= False):

    #Sciente Direct   
    terms = ' OR '
    terms = terms.join('Title-Abstr-Key({0}) '.format(w) for w in keywords)
    
    direct = "source-query "  + terms    
    if follow_up:        

        complement = " AND Title(\"{1}\")"
        direct = direct + complement

    return direct


def acm_string(keywords, follow_up= False):
    
    terms = ' OR '
    terms = terms.join('Title-Abstr-Key({0}) '.format(w) for w in keywords)    