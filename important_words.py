# -*- coding: utf-8 -*-
#!/usr/bin/env python 
import logging 
import math, nltk, datetime, string 
from nltk.corpus import stopwords 
from gensim import corpora, models, similarities 
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO) 


# TF - Term frequency (List frequencies for each word) 
def tf(ocurrences): 
	return float(1 + math.log(ocurrences))

docs = {} 
docLines = {} 
if __name__ == '__main__':
	startTime = datetime.datetime.now() 
	documentList = ["./texts/t11.txt","./texts/t22.txt"]; 
	# documentList = ["./texts/shak.txt"]; 
	totalDocs = len(documentList) 
	for documentFilename in documentList: 
		doc = open(documentFilename,'r')  
		for line in doc: 
			tokenized_sentence = nltk.word_tokenize(line.translate(None, string.punctuation))  
			for token in tokenized_sentence: 
				token = token.lower() 
				if (token not in stopwords.words('english')):
					docLines[token] = docLines.get(token,0) + 1
		doc.close() 
	for docLineKey, docLineValue in docLines.items(): 
		docLines[docLineKey] = tf(docLineValue)  
	output = open('output.txt', 'w') 
	for w in sorted(docLines, key=docLines.get, reverse=True): 
  			output.write("Word: {} Value: {}\n".format(w, docLines[w])) 
	output.write("TOTALTIME: {}".format(datetime.datetime.now()-startTime)) 
	output.close() 


