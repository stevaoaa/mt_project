#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sklearn.metrics import jaccard_similarity_score

import ast
import pandas as pd

#local
import util


"""
    Given two files calculate similarity using Jaccard coeficient
"""
def check_similarity(source, follow_up):
    
    source_list = util.file_in_list(source)
    follow_up_list = util.file_in_list(follow_up)
    try:
        jaccard = jaccard_similarity_score(source_list, follow_up_list)
    except:
        jaccard = 0
    return jaccard

"""
    Just check if the results from swap have the same size (avoid a wrong calculation of jaccard coeficient)
"""
def check_results(afile):
    
    #read from csv file
    # model: [source_string, num_results, papers, conferences, follow_string, num_results, papers, conferences, fault, time]
    my_csv = pd.read_csv(afile, usecols =[2,6], header= None)
    id = 1
    for index, row in my_csv.iterrows():
                
        try:
            source = ast.literal_eval(row[2])
            follow = ast.literal_eval(row[6])
            paper = source[0]
            if paper not in follow:
                print("Index: %d" % (id))
        except:
            print("Error in: %d" % (id))
        
        id = id +1


"""
    Given a csv result file Calculate ROCOF for each 1 hour interval
"""
def get_ROCOF(result_file):

    #get the last element from the first result line    
    starting_time = next(result_file)[-1]

    for line in result_file:

        #get next time
        next_time = line[-1]

        #get elapsed time
        elapsed_time = util.calculate_elapsed_time(starting_time, next_time)

        #less than 1 hour
        if elapsed_time.seconds < 3600:
            pass

        #1 hour should calculate ROCOF with data
        else:
            pass
