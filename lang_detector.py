# -*- coding: utf-8 -*-
#!/usr/bin/env python 
from nltk.corpus import movie_reviews 
from textblob.classifiers import NaiveBayesClassifier  
import sys 

train =	[ 
		("amor", "spanish"),
		("perro", "spanish"),
		("playa", "spanish"), 
		("sal", "spanish"), 
		("oceano", "spanish"), 
		("love", "english"),
		("dog", "english"),
		("beach", "english"),
		("salt", "english"),
		("ocean", "english") 
		] 
test = [
		("ropa", "spanish"), 
		("comprar", "spanish"), 
		("agua", "spanish"), 
		("telefono", "spanish"), 
		("clothes", "english"), 
		("buy", "english"), 
		("shirt", "english"), 
		("water", "english"), 
		("telephone", "english") 
	   ] 

def extractor(word): 
	feats = {} 
	last_letter = word[-1] 
	feats["last_letter({0})".format(last_letter)] = True 
	return feats 

if __name__ == '__main__': 
	# customDicts = {'./texts/wordsEn.txt':'english','./texts/wordsEs.txt':'spanish','./texts/wordsEs2.txt':'spanish'} 
	""" customDicts = {'./texts/wordsEn.txt':'english','./texts/wordsEs2.txt':'spanish'} 
	for customDictFilename, customDictLang in customDicts.items(): 
		currentDict = open(customDictFilename,'r') 
		for line in currentDict: 
			wordTrain = (line.replace('\r','').replace('\n',''),customDictLang) 
			train.append(wordTrain) 
		currentDict.close() """ 
	# print train 
	lang_detector = NaiveBayesClassifier(train, feature_extractor=extractor) 
	# lang_detector = NaiveBayesClassifier(train) 
	print lang_detector.accuracy(test) 
	lang_detector.show_informative_features(5) 
	while 1:
		try:
			line = sys.stdin.readline() 
			# print line 
			print lang_detector.classify(line) 
		except KeyboardInterrupt:
			break
		if not line:
			break

