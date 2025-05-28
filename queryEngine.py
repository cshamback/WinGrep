from utils import removeAN, removeSW, readJSON, findWordInJSON, printList, printDict

class QueryEngine: 
    def __init__(self):
        pass

    # holds the entire procedure for processing a query
    # separate query into individual, useful words -> get all those words from JSON and their data -> order the words -> return useful info to user 
    def processQuery(self, query: str):
        # separate into words, remove stopwords and symbols 
        query = query.lower()
        queryString = removeAN(query)
        words = removeSW(queryString)

        results = self.getWords(words) # returns a list (unordered)
        results = self.orderWords(results) # returns a list (ordered) - 2D arr of path vs. words and frequencies

        return results

    # search thru JSON to get all results (including path and freq) belonging to words in the query 
    def getWords(self, words: list):
        results = []

        # search through JSON map to find results containing those words 
        self.json = readJSON('sample.json') # returns a list of dicts

        for word in words:
            wordData = findWordInJSON(self.json, word)
            if wordData != None: 
                # TODO: change this to format [[path, (word, frequency), (word, frequency), ...], ...]
                results.append(wordData) # creates a list of only words that are in the search
        return results

    def orderWords(self, words: list):
        result = []
        
        # order results by number of unique words per page (highest at top)
        # [[path, (word, frequency), (word, frequency), ...], ...]

        return result
    
qe = QueryEngine()
printList(qe.processQuery("Fox jumped over dog axe"))