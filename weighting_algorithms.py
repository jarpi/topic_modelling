# -*- coding: utf-8 -*-
#!/usr/bin/env python 
from TfIdf import TfIdf 
from lsi import LSI 
from lda import LDA 
import sys 
import logging
import math, nltk, datetime, string 
from nltk.corpus import stopwords  


logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO) 

if __name__ == '__main__':
	startTime = datetime.datetime.now()  
	documentList = ["./texts/t11.txt","./texts/t22.txt"] 
	# documentList = ["./texts/test_shak1.txt"] 
	# documentList = ["./texts/shak.txt"] 
	totalDocs = len(documentList) 
	# Add language check on init and load correct stopwords list   
	stopList = stopwords.words('english') 
	# Init weighting libraries 
	TfIdf = TfIdf(documentList, stopList) 
	LSI = LSI(documentList, stopList) 
	LDA = LDA(documentList, stopList) 
	# Loop to get this argument 
	print "Ready " 
	while 1:
		try:
			line = sys.stdin.readline()
			print (TfIdf.runQuery(line)) 
			print (LSI.runQuery(line)) 
			print (LDA.runQuery(line)) 
		except KeyboardInterrupt:
			break
		if not line:
			break 



