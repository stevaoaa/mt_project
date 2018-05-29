#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import datetime

import unittest

#local
import util
import statistics

"""
    This class simple execute some functions in order to see how things are going until mix all things together
"""
class SimplisticTest(unittest.TestCase):


    #util.py tests
    def test_random_line(self):

        path_file = os.getcwd() + "/dataset/keywords_sample.csv"

        with open(path_file, "r") as afile:
            line = util.random_line(afile)
        
        print(("A random line from a file: %s") % (line))
        self.assertTrue(True)



    def test_random_keywords(self):
        
        path_file = os.getcwd() + "/dataset/keywords_sample.csv"

        with open(path_file, "r") as afile:
            keywords = util.random_keywords(afile)
        
        print(("A random keywords list from a file: %s") % (keywords))
        self.assertTrue(isinstance(keywords, list))



    def test_file_in_list(self):
        path_file = os.getcwd() + "/dataset/keywords_sample.csv"

        with open(path_file, "r") as afile:
            alist = util.file_in_list(afile)
        
        print(("A list from a file: %s") % (alist[:2]))
        self.assertTrue(isinstance(alist, list))


    def test_calculate_elapsed_time(self):
        
        # for example
        s1 = str(datetime.datetime.now().strftime('%H:%M:%S'))
        time.sleep(1) #wait one second
        s2 = str(datetime.datetime.now().strftime('%H:%M:%S'))

        delta = util.calculate_elapsed_time(s1,s2) 
        
        #difference between 2 dates in '%H:%M:%S' format
        print(("Difference between dates: %s") % (delta))
        self.assertTrue(True)

    #statistics.py tests
    def test_check_similarity(self):
        
        path_file = os.getcwd() + "/dataset/keywords_sample.csv"

        with open(path_file, "r") as afile:
            alist = util.file_in_list(afile)

        #calculate jaccard wit a list and the same list reversed. Should be lower
        jaccard = statistics.check_similarity(alist, alist[::-1])
        print(("Jaccard Coefficient: %s") % (jaccard)) 
        self.assertTrue(True)

    def test_get_ROCOF(self):
        pass

    def test_get_ROCOA(self):
        pass


if __name__ == '__main__':
    unittest.main()