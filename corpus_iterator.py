# -*- coding: utf-8 -*-
#!/usr/bin/env python 
from utils import Utils  
from gensim import corpora, models, similarities 

class MyCorpus: 
	def __init__(self, documentList, stopList): 
		self.documentList = documentList 
		self.utils = Utils() 
		self.dictionary = [] 
		# collect statistics about all tokens 
		for documentFile in self.documentList: 
			self.dictionary = corpora.Dictionary(self.utils.cleanStopWordsPunctuations(line, stopList) for line in open(documentFile))
		# remove stop words and words that appear only once
		# stop_ids = [dictionary.token2id[stopword] for stopword in stoplist
		            # if stopword in dictionary.token2id]
		# once_ids = [tokenid for tokenid, docfreq in dictionary.dfs.iteritems() if docfreq == 1]
		# self.dictionary.filter_tokens(stop_ids + once_ids) # remove stop words and words that appear only once
		# self.dictionary.compactify() # remove gaps in id sequence after words that were removed
		print(self.dictionary) 
	
	def __iter__(self): 
		for documentFile in self.documentList: 
			for line in open(documentFile): 
				print (line) 
				# assume there's one document per line, tokens separated by whitespace 
				yield self.dictionary.doc2bow(line.split()) 

	def convertToBOW(self, keyword): 
		return self.dictionary.doc2bow(keyword.lower().strip().split()) 

	def getCorpusDictionary(self): 
		return self.dictionary 


