# Haotian He
# Homework 1 for LING 571
# January 16, 2014

import nltk
from nltk.tokenize import RegexpTokenizer

grammar = nltk.data.load('file:grammar.cfg') # loads the grammar
parser = nltk.parse.EarleyChartParser(grammar) # builds a parser for the grammar
example = open('sentences.txt', 'r') # reads the example sentences

# initialize the counting
sentCount = 0;
parsCount = 0;
totalParsCount = 0;

for line in example: # reads each sentence

    tokenizer = RegexpTokenizer('\w+|\$[\d\.]+|\S+')
    tokens = tokenizer.tokenize(line) # makes each sentence lowercase and splitted
    sentCount += 1 # counts the number of sentences in this example
    
    trees = parser.nbest_parse(tokens) # parses the given sentence to get parse trees that represent possible structures for the given sentence
    for tree in trees: # prints the parse trees
        print str(tree) + "\n"
        parsCount += 1 # counts the number of parses for the sentence

    if parsCount == 1: # prints the number of parses under the tree
        print str(parsCount) + " parse" + "\n"
    else:
        print str(parsCount) + " parses" + "\n"
    print "\n"

    totalParsCount += parsCount
    parsCount = 0;

print "The average number of parses per sentence obtained by the grammar is " + str(int(round(totalParsCount/sentCount))) # prints the statement of the performance