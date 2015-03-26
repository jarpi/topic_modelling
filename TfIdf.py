# -*- coding: utf-8 -*-
#!/usr/bin/env python 
from utils import Utils 
from corpus_iterator import MyCorpus 
from gensim import corpora, models, similarities 

class TfIdf: 
	def __init__(self, documentList, stopList): 
		self.documentList = documentList 
		self.stopList = stopList 
		self.texts = [] 
		self.corpus = [] 
		self.tfidfModel = [] 
		self.index = [] 
		self.utils = Utils()  
		self.isInitialized = False  
		self.initMe()

	def runQuery(self,keyword): 
		if (self.isInitialized): 
			# self.dictionary.doc2bow(keyword.lower().strip().split())
			vec = self.corpus.convertToBOW(keyword) 
			sims = self.index[self.tfidfModel[vec]]  
			return (list(enumerate(sims))) 
		return [] 

	def initMe(self): 
		if (not self.isInitialized): 
			# self.texts = self.utils.cleanStopWordsPunctuations(self.documentList, self.stopList) 
			# self.dictionary = corpora.Dictionary(self.texts) 
			# print (self.dictionary) 
			# self.corpus = [self.dictionary.doc2bow(text) for text in self.texts] 
			self.corpus = MyCorpus(self.documentList, self.stopList) 
			# print (self.corpus) 
			self.tfidfModel = models.TfidfModel(self.corpus) 
			# self.index = similarities.SparseMatrixSimilarity(self.tfidfModel[self.corpus], num_features=12) 
			self.index = similarities.Similarity('./', self.tfidfModel[self.corpus], num_features=200, chunksize=128, shardsize=16384) 
			# print (self.dictionary.token2id) 
			self.isInitialized = True   






