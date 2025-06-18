import numpy as np
import os

class Crawler: 
    root = None

    def __init__(self):
        self.root = self.findRoot()
    
    # BFS all files starting at root, store paths in numpy arr
    def crawl(self): 
        files = np.empty((0,)) # empty 1D array
        print(files)

        for dirPath, subDirs, fileNames in os.walk(self.root):
            # TODO: add configurable list of directory/file names to be ignored: can be "contains" or "ends with"
            if (dirPath.endswith("__pycache__") or ".git/objects" in dirPath):
                # print(f"ALERT: Found skippable directory {dirPath}. Skipping.")
                continue # skip this directory 

            for dir in subDirs: 
                if(dir not in files):
                    # print(f"Folder: {dir}")
                    files = np.append(files, dir)

            for filename in fileNames: 
                # print(f"File: {filename}")
                files = np.append(files, filename)

        return files    
    
    # called during crawler initialization, gets root dir to start crawling from
    # returns root directory name as string
    def findRoot(self):
        currentPath = os.getcwd() # get Current Working Directory
        parentPath = os.path.dirname(currentPath)

        # if parentPath = currentPath, we've found the root 
        while os.path.dirname(currentPath) != parentPath:            
            currentPath = parentPath

        return currentPath
    
# will need to be called when indexing starts 
#crawler = Crawler()
#Database = crawler.crawl()