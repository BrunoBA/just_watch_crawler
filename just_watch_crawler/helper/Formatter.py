import json 

class Formatter:
    def __init__(self, dictionary) -> None:
        self.dictionary = dictionary
    
    def __str__(self) -> str:
        return json.dumps(self.dictionary, indent = 2) 