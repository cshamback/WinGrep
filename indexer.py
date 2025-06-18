from utils import readJSON, writeJSON, createJSONWord, addWord, removeSW, removeAN
import json
 
class Indexer: 
    def __init__(self):
        pass
    
    # iterate through a numpy array of files and generate JSON.
    def index(self, db): 
        # read every file
        for path in db:

            # determine if file is readable via extension
            split = path.rsplit(".", 1) # split from the right one time, returns ["before", "after"]
            extension = f".{split[-1]}"
            if(not self.isReadable(extension)): 
                # print("Found a file that is not readable: ", path)
                continue

            # read file
            try:
                with open(path, "r") as f:
                    content = f.read()

                    # index file contents 
                    self.analyzeText(content, path)

            except FileNotFoundError:
                # TODO: do something about the case where this is a directory and not a file
                print(f"ERROR: file {path} was not found.")
            except json.JSONDecodeError as e: 
                print(f"ERROR: could not read from file {path}")
            except Exception as e: 
                print(f"ERROR: {e} for path {path} in Indexer.index()")

    # can human words be read from the file by python?
    def isReadable(self, extension: str):
        return extension in {".txt", ".csv", ".json", ".html", ".xml", ".log", ".py", ".js", ".css", ".md"}

    # locate all human-readable words in a single file and update the JSON; uses NLTK 
    def analyzeText(self, text, filepath):
        # TODO: add functionality to get words from a non-sentence string 

        # prepare text (remove stopwords and non-alphanumeric characters)
        text = text.lower()
        text = removeAN(text) # remove non-alphanumeric chars
        words = removeSW(text) # remove stopwords

        # get all words and their frequencies to be added to the JSON
        map = {} # dict of words and their frequencies, <word, frequency>
        for word in words: 
            if word in map: 
                map[word] = map[word] + 1
            else:
                map[word] = 1

        # update JSON
        json = readJSON('sample.json')
        
        for key, value in map.items():
            newWord = createJSONWord(key, value, filepath) # ENTIRE JSONWord
            addWord(json, newWord)

        writeJSON(json)

    # locate all human-readable words and update the JSON using only file names
    def analyzeName(self, name, filepath):
        pass

#indx = Indexer()
#indx.analyzeText("The quick brown fox jumped over his lazy dog. The dog ate the fox.", "~/Downloads/sampleText.txt")