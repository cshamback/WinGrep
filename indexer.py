from utils import readJSON, writeJSON, createJSONWord, addWord, removeSW, removeAN
 
class Indexer: 
    def __init__(self):
        pass
    
    # iterate through a numpy array of data and generate JSON.
    def index(self, dirs): 
        pass

    # can human words be read from the file by python?
    def isReadable(self, extension: str):
        return extension in {".txt", ".csv", ".json", ".html", ".xml", ".log", ".py", ".js", ".css", ".md"}

    # locate all human-readable words and update the JSON; uses NLTK 
    def analyzeText(self, text, filepath):
        # prepare text (remove stopwords and non-alphanumeric characters)
        text = text.lower()
        text = removeAN(text)    
        words = removeSW(text)

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
            newWord = createJSONWord(key, value, filepath)
            addWord(json, newWord)
        writeJSON(json)

    # locate all human-readable words and update the JSON
    def analyzeName(self, name):
        pass

indx = Indexer()
indx.analyzeText("The quick brown fox jumped over his lazy dog. The dog ate the fox.", "~/Downloads/sampleText.txt")