from utils import *
from crawler import *
from indexer import *

# global Database is numpy array
# must be accessed inside functions using global keyword ie. "global Database"
Database = np.empty((0,))

crwlr = Crawler()
indx = Indexer()

Database = crwlr.crawl()
print("Crawling complete. Database: ")
print(Database)