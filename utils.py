import json

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

"""
# Example addWord
newWord = {"word": "Katherine", "pages": [{"url": "~/Desktop/Images/LOML/Katherine.png", "freq": "1"}]}
data = addWord(readJSON("sample.json"), newWord)
writeJSON(data)
"""