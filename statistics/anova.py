#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import csv


import numpy as np

from pandas import *
from scipy  import stats

if __name__ == '__main__':
    #Independent Variables
	randomDists = ['ACM','IEEE', 'Scidirect','Springer']
	xLabel = 'Search Engine'
	
	metamorphic_relations = ['MPTitle', 'MPublished', 'SwapJD', 'Top1Absent']
	
	if (len(sys.argv) == 1):
		print('Usage: python bloxplot.py relation (\'MPTitle\', \'MPublished\', \'SwapJD\', \'Top1Absent\')')
		sys.exit(-1)
	
	metamorphic_relation = str(sys.argv[1]) #Metamorphic Relation
	
	if (metamorphic_relation == 'MPTitle'):
		#MPTitle
		ACM  = []
		IEEE  = []
		SciDirect = []
		Springer = []
	elif (metamorphic_relation == 'MPublished'):
		#MPublished
		ACM  = []
		IEEE  = []
		SciDirect = []
		Springer = []
	elif (metamorphic_relation == 'SwapJD'):
		#SwapJD
		ACM  = [0.365, 0.398333333, 0.225, 0.341666667, 0.462592593, 0.336666667, 0.343333333, 0.186666667, 0.275, 0.266666667, 0.25, 0.231666667, 0.306666667, 0.34, 0.313333333, 0.303333333, 0.401666667, 0.406666667, 0.166666667, 0.326666667, 0.248333333, 0.261666667, 0.243333333, 0.23, 0.308333333, 0.208333333, 0.285, 0.241111111, 0.32, 0.346666667, 0.243333333, 0.330606061, 0.303333333]
		IEEE  = [0.309333333, 0.421333333, 0.518666667, 0.358666667, 0.328, 0.430666667, 0.393333333, 0.325333333, 0.442666667, 0.425333333, 0.505333333, 0.438666667, 0.484, 0.389333333, 0.432, 0.398666667, 0.505333333, 0.352, 0.54, 0.445333333, 0.444, 0.461333333, 0.424, 0.473333333, 0.705333333, 0.44, 0.389333333, 0.293333333, 0.302666667, 0.310666667, 0.328, 0.498666667, 0.312]
		SciDirect = [0.338666667, 0.306666667, 0.385333333, 0.269333333, 0.318761905, 0.221333333, 0.2, 0.322666667, 0.170666667, 0.372, 0.298111365, 0.348, 0.253333333, 0.361333333, 0.346666667, 0.342666667, 0.402666667, 0.344, 0.330666667, 0.538666667, 0.333333333, 0.264, 0.273333333, 0.410666667, 0.433333333, 0.225894737, 0.336, 0.206666667, 0.182666667, 0.385101449, 0.396592593, 0.365333333, 0.238333333]
		Springer = [0.969210526, 0.987602339, 1, 0.993333333, 0.874187995, 0.984444444, 0.962745098, 0.996666667, 0.961904762, 0.992592593, 0.971520468, 1, 0.921666667, 0.93, 0.996666667, 1, 0.989454191, 0.957777778, 0.966666667, 0.972962963, 0.952807018, 0.921666667, 1, 0.980392157, 0.994736842, 1, 0.93, 0.946410256, 0.982962963, 0.987037037, 0.936246782, 0.964814815, 0.98]
	elif (metamorphic_relation == 'Top1Absent'):
		#Top1Absent
		ACM  = []
		IEEE  = []
		SciDirect = []
		Springer = []

	print(metamorphic_relation)
	print ('\n============= ANOVA FOR ACM, IEEE, SciDirect, Springer =============')
	#anova for each configuration
	f4_value, p4_value = stats.f_oneway(ACM, IEEE, SciDirect, Springer)
	
	if p4_value < 0.01:
		print ("f4_value = {f4_value} | p4_value = {p4_value} ".format(f4_value = f4_value, p4_value = p4_value))
	print ('====================================================================\n')