# coding=utf-8 
import sys 
from textblob.classifiers import NaiveBayesClassifier 

train_set = [
    ('i love this sandwich.', 'pos'),
    ('i like', 'pos'), 
    ('i do like', 'pos'), 
    ('this is an amazing place!', 'pos'),
    ('i feel very good about these beers.', 'pos'),
    ('this is my best work.', 'pos'),
    ('what an awesome view', 'pos'), 
    ('he is my friend', 'pos'), 
    ('do you like', 'pos'), 

    ('i do not like this restaurant', 'neg'),
    ("i don't like this",'neg'),  
    ('i am tired of this stuff.', 'neg'),
    ("i can't deal with this", 'neg'),
    ('he is my sworn enemy!', 'neg'),
    ('enemy', 'neg'), 
    ('my boss is horrible.', 'neg'),  
    ('i do not like', 'neg'), 
    ('i hate', 'neg') 
    ] 


# positiveSet = ['./texts/positive-words.txt']
# negativeSet = ['./texts/negative-words.txt']  

def train_positive(): 
    global train_set 
    for document in positiveSet: 
        for line in open(document): 
            train_set.append((line.replace('\n','').decode('utf-8'),'pos'))

def train_negative(): 
    global train_set 
    for document in negativeSet: 
        for line in open(document): 
            train_set.append((line.replace('\n','').decode('utf-8'),'neg')) 

test_set = [
	('The beer was good.', 'pos'),
    ('I do not enjoy my job', 'neg'),
    ("I ain't feeling dandy today.", 'neg'),
    ("I feel amazing!", 'pos'),
    ('Gary is a friend of mine.', 'pos'),
    ("I can't believe I'm doing this.", 'neg')
    ] 

if __name__ == '__main__': 
    # print "Initiallizing classifier... (training...)" 
    # train_positive() 
    # train_negative() 
    # print train_set 
    # classifier = NaiveBayesClassifier(train_set) 
    
    # with open('./texts/words.txt', 'r') as fp: 
    #     classifier = NaiveBayesClassifier(fp, format="csv") 
    #     print classifier.accuracy(test_set) 
    #     print classifier.show_informative_features() 

    classifier = NaiveBayesClassifier(train_set) 
    print train_set 
    print classifier.accuracy(test_set) 
    print classifier.show_informative_features() 
    print "Ready " 
    while 1:
        try:
            line = sys.stdin.readline() 
            prob_dist = classifier.prob_classify(line.lower()) 
            print prob_dist.max() 
            print "PROB POS: " + str(round(prob_dist.prob("pos"), 2))
            print "PROB NEG: " + str(round(prob_dist.prob("neg"), 2)) 
        except KeyboardInterrupt:
            break
        if not line:
            break

