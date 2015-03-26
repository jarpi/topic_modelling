# -*- coding: utf-8 -*-
#!/usr/bin/env python 
from textblob.classifiers import NaiveBayesClassifier 
from textblob import TextBlob 

train_set = [
	('I love this sandwich.', 'pos'),
    ('This is an amazing place!', 'pos'),
    ('I feel very good about these beers.', 'pos'),
    ('This is my best work.', 'pos'),
    ("What an awesome view", 'pos'),
    ('I do not like this restaurant', 'neg'),
    ('I am tired of this stuff.', 'neg'),
    ("I can't deal with this", 'neg'),
    ('He is my sworn enemy!', 'neg'),
    ('My boss is horrible.', 'neg')
    ] 

test_set = [
	('The beer was good.', 'pos'),
    ('I do not enjoy my job', 'neg'),
    ("I ain't feeling dandy today.", 'neg'),
    ("I feel amazing!", 'pos'),
    ('Gary is a friend of mine.', 'pos'),
    ("I can't believe I'm doing this.", 'neg')
] 

if __name__ == '__main__':
	cl = NaiveBayesClassifier(train_set) 
	# Try to classify text, after training 
	print(cl.classify("Their burgers are amazing")) 
	print(cl.classify("I don't like their pizza.")) 
	# Try with text blob 
	blob = TextBlob("The beer was amazing. But the hangover was horrible. "
                "My boss was not pleased.", classifier=cl)
	for sentence in blob.sentences: 
		print (sentence) 
		print (sentence.classify()) 
	# Accuracy on test set 
	print "Accuracy: {}".format(cl.accuracy(test_set)) 
	# Informative features 
	cl.show_informative_features(5) 


