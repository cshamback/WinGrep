import json
import numpy as np
import nltk 
import re

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#=============================================================================================================================================================================
# JSON -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#=============================================================================================================================================================================

# write JSON to a .json file
def writeJSON(data):
    jsonObj = json.dumps(data, indent=4)
    try: 
        with open("sample.json", "w") as outfile: 
            outfile.write(jsonObj)
    except FileExistsError:
        print("sample.json already exists.")
    except:
        print("Unable to write to file.")
    else: 
        print("Success! JSON written.")

# read JSON from a .json file
def readJSON(path):
    with open(path, 'r') as infile: 
        data = json.load(infile)
    return data

# create JSON string for a single word given its frequency and filepath
def createJSONWord(word: str, freq: int, path: str):
    return {"word": word, "pages": [{"path": path, "freq": freq}]}

# add a new word to the existing JSON data: either add a new word to the array, or add to the Pages array of an existing word 
# can use this to overwrite the old copy of data with the new one, or create a new version separately
def addWord(data, newWord):

    # get word from JSON; will always be the value with key "word"
    word = newWord["word"]
    
    # update data as needed 
    for i in range(len(data)): # data is a list 
        if data[i]["word"] == word: # if the current word in the list is the same as the word we're adding  
            print(f"{word} is already in the dict.")

            # add a new line to the pages list 
            data[i]["pages"].append(newWord["pages"][0]) # the "pages" will be an array with 0 elements 
            return data 
    
    print(f"Need to add {word} to dict.")
    data.append(newWord) # add ALL the data including frequency and location, along with the word 
        
    return data 

# searches for a string in a JSON list; returns all its data
def findWordInJSON(data: list, word: str):
    for item in data: # creates a copy, not a direct reference 
        currWord = item["word"]
        if currWord == word: 
            return item
    return None

"""
# Example addWord
newWord = {"word": "Katherine", "pages": [{"path": "~/Desktop/Images/LOML/Katherine.png", "freq": "1"}]}
data = addWord(readJSON("sample.json"), newWord)
writeJSON(data)
"""

#=============================================================================================================================================================================
# DSA ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#=============================================================================================================================================================================

# Breadth-First Search used by crawler to traverse all dicts
def bfs(root):
    currDir = root
    dirs = np.empty(1, str)

    print(dirs)

def printList(lst: list):
    for item in lst: 
        print(item)

def printDict(dict):
    for key, value in dict.items():
        print(f"{key}: {value}")

#=============================================================================================================================================================================
# NLTK -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#=============================================================================================================================================================================

# remove all non-alphanumeric chars
def removeAN(text):
    return re.sub(r'[^\w\s]', '', text) # sub non-alphanumeric chars in string with '' (nothing)

# remove all stopwords using NLTK (Natural Language Toolkit)
def removeSW(text):
    # use NLTK to only get useful words (remove stop words)
    try:
        nltk.data.find('tokenizers/punkt_tab')
    except LookupError:
        nltk.download('punkt_tab')
    try: 
        nltk.data.find('corpora/stopwords')
    except LookupError: 
        nltk.download('stopwords')
    
    stopWords = set(stopwords.words('english'))
    wordTokens = word_tokenize(text)

    result = [] 

    for w in wordTokens:
        if w not in stopWords:
            result.append(w)

    print("Result: ", result)
    return result