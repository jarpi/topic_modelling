# -*- coding: utf-8 -*-
#!/usr/bin/env python 
import math 

docs = {} 
totalWordsInDoc = {}

def tf(ocurrences,totalWordsInDoc): 
	return 1+float(math.log(ocurrences))
def idf(totalDocs,docsContainingWord): 
	return round(float(1+math.log(totalDocs/docsContainingWord,10)),4)

def getDocsContainingWord(word): 
	wordInDocs = 0 
	for docKey, docValue in docs.items(): 
		if docValue.has_key(word): 
			wordInDocs += 1 
	return wordInDocs 
def getDocTotalWords(docKey): 
	return totalWordsInDoc[docKey] 

if __name__ == '__main__':
	documentList = ["./texts/t11.txt","./texts/t22.txt"]; 
	totalDocs = len(documentList) 
	# Parse documents 
	for documentFilename in documentList: 
		docs[documentFilename] = {} 
		doc = open(documentFilename,'r')  
		for line in doc: 
			i = 0
			for word in line.lower().replace('\n',' ').replace('\r','').replace('.','').replace('"','').split(' '): 
				if (word != ""): 
					docs[documentFilename][word] = docs[documentFilename].get(word,0) + 1 
					i+=1 
			totalWordsInDoc[documentFilename] = i 
		doc.close() 
	# Calc tfidf 
	for docKey, docWordList in docs.items(): 
		for wordKey, wordValue in docWordList.items(): 
			#print "WORDKEY: {} WORDVALUE: {} TOTALWORDS: {} TOTALDOCS: {} WORDAPPEARSIN: {}".format(wordKey,wordValue, getDocTotalWords(docKey),len(docs),getDocsContainingWord(wordKey)) 
			a = tf(wordValue, getDocTotalWords(docKey)) 
			b = idf(len(docs),getDocsContainingWord(wordKey)) 
			docs[docKey][wordKey] = round(a*b, 5) 
	# Print most relevant words 
	for docKey, docWordList in docs.items(): 
		print docKey 
		for w in sorted(docs[docKey], key=docs[docKey].get, reverse=True): 
  			print "Word: {} Value: {}".format(w, docs[docKey][w]) 
