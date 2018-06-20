#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import csv
import json

"""
	Read an json object file and returns a pandas dataframe obj
"""
def read_file_as_json(file_path):
	
	data = []
	
	with open(file_path, 'rU') as json_data:

		for entry in json_data:

			json_obj = json.loads(entry) #as json

			#computer science
			if "DBLP" in json_obj["sources"]:
				data.append(json_obj["entities"])  
	return data




if __name__ == '__main__':

	#dataset
	#http://labs.semanticscholar.org/corpus/

	#dataset path 
	path = "/media/stevao/Seagate Expansion Drive/dataset"
	
	#path = os.getcwd() + "/dataset" #test

	#csv
	output_file = open("keywords.csv","a")

	#writer
	output_writer = csv.writer(output_file)
	
	#For each file in dataset
	for root, dirs, files in os.walk(path):
		
		for f in files:

			print("Handling: %s" % (f))

			keywords = []
			full_path = path +"/" + f

			#parse the json to a list with the entities
			keywords = read_file_as_json(full_path)

			#save the keywords in a file
			for entry in keywords:
				
				#ignore utf-8 error in some keywords
				try:
					output_writer.writerow(entry)
				except:
					pass
	print("Finished")
	