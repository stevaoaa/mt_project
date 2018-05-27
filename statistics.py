#!/usr/bin/env python
# -*- coding: utf-8 -*-

from util import file_in_list, calculate_elapsed_time

from sklearn.metrics import jaccard_similarity_score


"""
    Given two files calculate similarity using Jaccard coeficient
"""
def check_similarity(source, follow_up):
    
    source_list = file_in_list(source)
    follow_up_list = file_in_list(follow_up)

    jaccard = jaccard_similarity_score(source_list, follow_up_list)

    return jaccard

"""
    Given a csv result file Calculate ROCOF for each 1 hour interval
"""
def get_ROCOF(result_file):

    with open(result_file, 'rU') as json_data:

        #get the first result time    
        starting_time = result_file[0][-1]

        for line in result_file:

            #get next time
            next_time = line[-1]

            #get elapsed time
            elapsed_time = calculate_elapsed_time(starting_time, next_time)

            #less than 1 hour
            if elapsed_time.seconds < 3600:
                pass

            #1 hour should calculate ROCOF with data
            else:
                pass


"""
    Given a csv result file Calculate ROCOA for each 1 hour interval
"""
def get_ROCOA(result_file):
    pass