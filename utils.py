import json
import numpy as np
import nltk 
import re
import os

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#=============================================================================================================================================================================
# JSON -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#=============================================================================================================================================================================

# write JSON to a .json file
def writeJSON(data):
    jsonObj = json.dumps(data, indent=4) # converts python object to JSON-formatted string
    # print(jsonObj)
    if(jsonObj != "[]"):
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
    try: 
        with open(path, 'r') as infile: 
            data = json.load(infile)
            # print("Data found by ReadJSON: ", data)
        return data
    except json.JSONDecodeError:
        print("JSON is empty. Please put a pair of square brackets in the JSON file.")
        return ""
    except Exception as e:
        print(f"ERROR: {e} for {path}")
    return ""

# create JSON string for a single word given its frequency and filepath
def createJSONWord(word: str, freq: int, path: str):
    return {"word": word, "pages": [{"path": path, "freq": freq}]}

# add a new word to the existing JSON data: either add a new word to the array, or add to the Pages array of an existing word 
# can use this to overwrite the old copy of data with the new one, or create a new version separately
def addWord(data, newWord):

    # get single word from JSON; will always be the value with key "word"
    singleWord = newWord["word"]
    # print(f"{singleWord} found in {newWord}")

    # search entire existing JSON for this word
    existingJSONWord = findWordInJSON(data, singleWord)
    if(existingJSONWord == None):
        print("Did not find an existing JSONWord in the JSON file for", singleWord)
        
        # add a brand new word to the dictionary     
        jsonArr = readJSON("sample.json") # get JSON from file (automatically converted to array of dicts)
        jsonArr.append(newWord) # add new word to that JSON
        writeJSON(jsonArr)
        print()


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
# currently just finds a file or directory path
def bfs(root, target):

    for dirPath, subDirs, fileNames in os.walk(root):
        print(f"Directory: {dirPath}")
        if(target in subDirs): 
            print(f"Target found: {dirPath}/{target}")
            return dirPath

        for filename in fileNames: 
            print(f"File: {filename}")

            if(filename == target):
                print(f"Target found in folder: {dirPath} Full path: {dirPath}/{target}")
                return dirPath

    return None

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

    #print("Result: ", result)
    return result

#bfs("Home", "toad.txt")