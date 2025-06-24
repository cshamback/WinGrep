from utils import *
from crawler import *
from indexer import *
from queryEngine import *

# global Database is numpy array
# must be accessed inside functions using global keyword ie. "global Database"
Database = np.empty((0,))

crwlr = Crawler()
indx = Indexer()
qe = QueryEngine()

# BFS the entire file tree. Store all file and folder paths in the NP array Database 
#Database = crwlr.crawl()
#print("Crawling complete. Files explored:", crwlr.filesExplored)
#print(Database)

# iterate through every file stored in Database. 
# if the file is human-readable, analyze it and add the results to a JSON file
#indx.index(Database)
#print("Indexing complete. Words encountered:", indx.wordsEncountered)

# get each word from the query and find corresponding results in sample.json
results = qe.processQuery("the quick brown fox jumped over the lazy dog")