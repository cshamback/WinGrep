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

        print("Processed query:", words)

        results = self.getWords(words) # returns a list (unordered)
        results = self.orderWords(results) # returns a list (ordered) - 2D arr of path vs. words and frequencies

        return results

    # search thru JSON to get all results (including path and freq) belonging to words in the query 
    def getWords(self, words: list):
        # TODO: allow a phrase to be searched for, like "import nltk", not just words
        results = []

        # search through JSON map to find results containing those words 
        self.json = readJSON('sample.json') # returns a list of dicts

        for word in words: # look at every word in the query 
            wordIndex = findWordInJSON(self.json, word) # returns an index 
            if wordIndex != None:           
                wordFound = self.json[wordIndex] # json object with single word string and an array of pages/frequencies

                for i in range(len(wordFound["pages"])):

                    currentPage = wordFound["pages"][i] # each of these is a dict: {"path": "path string", "freq", n}
                    currentPath = currentPage["path"]

                    # search through results for the current path
                    foundMatch = False
                    for k in range(len(results)):
                        if(results[k]["path"] == currentPath):
                            results[k]["words"][wordFound["word"]] = wordFound["pages"][i]["freq"] # add word and its frequency to this path in the results

                            foundMatch = True
                            break
                    if(foundMatch == False):
                        # print("Did not find path", currentPath, "in search results. Appending now.")
                        results.append({"path": currentPath, "words": {wordFound["word"]: wordFound["pages"][i]["freq"]}})
        return results

    def orderWords(self, unorderedResults: list):
        result = [] # 2D arr, each item is [{result}, int(frequency)]
        
        # add results and the number of words in them to an array
        for i in range(0, len(unorderedResults)):
            currResult = unorderedResults[i]

            # count total words found in result 'words' dict
            count = 0
            for key, value in currResult["words"].items():
                count = count + int(value)

            newResult = [currResult, count]
            #print("New result to add: ", newResult)
            result.append(newResult)

        # sort the results by number of words per result, most words first
        result = sorted(result, key = lambda x: x[1], reverse = True) # sort by second column; to reverse add "reverse = True" as a parameter after "x[1]"
            
        return [row[0] for row in result]