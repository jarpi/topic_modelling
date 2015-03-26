# -*- coding: utf-8 -*-
#!/usr/bin/env python 
from gensim.models import Word2Vec 
from nltk.corpus import brown, movie_reviews, treebank 

if __name__ == '__main__':
	brown_sentences = Word2Vec(brown.sents())
	movie_sentences = Word2Vec(movie_reviews.sents()) 
	treebank_sentences = Word2Vec(treebank.sents()) 

	print brown_sentences.most_similar('money', topn=5) 
	print movie_sentences.most_similar('money', topn=5) 
	print treebank_sentences.most_similar('money', topn=5) 

