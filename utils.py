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
def addWord(newWord):

    jsonArr = readJSON("sample.json") # get JSON from file (automatically converted to array of dicts)

    # get single word from JSON; will always be the value with key "word"
    singleWord = newWord["word"]
    existingJSONWord = findWordInJSON(jsonArr, singleWord) # search entire existing JSON for this word: existingJSONWord is an int

    if(existingJSONWord == None):   
        jsonArr.append(newWord) # add new word to that JSON

    else: # if word is already in the json file

        # check if path and freq are also already there
        # this should happen rarely, if ever
        for i in range(0, len(jsonArr[existingJSONWord]["pages"])): # iterate thru every page that word is on
            if(newWord["pages"][0]["path"] in jsonArr[existingJSONWord]["pages"][i]["path"]):
                return

        # create new dict to add. format: {"path": "path string", "freq": n}
        # format of newWord is {"word": word, "pages": [{"path": path, "freq": freq}]}
        dataToInsert = {"path": newWord["pages"][0]["path"], "freq": newWord["pages"][0]["freq"]}

        # append a dict containing the new word's path and frequency to the "pages" array for the given word
        # GOD that's a lot of data access 
        jsonArr[existingJSONWord]["pages"].append(dataToInsert)
    
    writeJSON(jsonArr) # write whatever changes we made to jsonArr to file

# searches for a string in a JSON list; returns first index where it was found or None
def findWordInJSON(data: list, word: str):
    for i in range(0, len(data)):
        currWord = data[i]["word"]
        if currWord == word: 
            return i
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
        #print(f"Directory: {dirPath}")
        if(target in subDirs): 
            #print(f"Target found: {dirPath}/{target}")
            return dirPath

        for filename in fileNames: 
            #print(f"File: {filename}")

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