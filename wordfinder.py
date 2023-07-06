"""Word Finder: finds random words from a dictionary."""
import random 
import linecache

class WordFinder:

    def __init__(self, file_name):
        """Target the file to read from"""
        self.file = file_name

    def random_word(self):
        dictionary = open(f"{self.file}", "r")

        #Calculating the number of lines which a word occupies in the given dictioanry
        length = len(dictionary.readlines())


        #Generating a random number based on the length found. 
        random_number = random.randint(0, length-1)

        #Generating the random word. 
        target = linecache.getline(f"{self.file}", random_number)

        dictionary.close()

        return target.rstrip()

    def __repr__(self):
        """Showing a representation of what the new variable is"""
        f"<WordFinder target file to read is:{self.file}"
       
    
