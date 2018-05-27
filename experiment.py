#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import csv

from datetime import datetime  


"""
    run source and follow_up queries and store results in a file
"""
def source_followup_execution(filename, mp_publish = None, mp_title = None, reverse_swap = None, top1_absent = None):
    
    starting_time = datetime.now()

    results = []
    
    #gathering results for any metamorphic relation
    if mp_publish:
        pass

    if mp_title:
        pass
    
    if reverse_swap:
        pass
    
    if top1_absent:
        pass
    else:
        print("Error in use. Need to specify ONE Metamorphic Relatioship!")
        sys.exit(-1) #ERROR CODE

    #begging of the operation
    results.append(starting_time)

    #saving results into CSV file
    with open(filename, "wb") as sheet:
        out = csv.writer(sheet, delimiter=',',quoting=csv.QUOTE_ALL)
        out.writerow(results)

    

if __name__ == '__main__':
    pass