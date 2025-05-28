import numpy as np

class Crawler: 
    def __init__(self):
        pass
    
    # BFS all files starting at root, store paths in numpy arr
    def crawl(self, root: str): 
        files = np.empty()
        return files