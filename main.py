from utils import *
from crawler import *
from indexer import *

# global Database is numpy array
# must be accessed inside functions using global keyword ie. "global Database"
Database = np.empty((0,))

crwlr = Crawler()
indx = Indexer()

# BFS the entire file tree. Store all file and folder paths in the NP array Database 
Database = crwlr.crawl()
print("Crawling complete.")
#print(Database)

# iterate through every file stored in Database. 
# if the file is human-readable, analyze it and add the results to a JSON file
indx.index(Database)