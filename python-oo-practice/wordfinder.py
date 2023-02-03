"""Word Finder: finds random words from a dictionary."""

import random


class WordFinder:
    """finds random words from dictionary"""
    def __init__(self, path):
        """Read dictionary and print # of items that are read"""
        dict_file = open(path)
        self.words = self.parse(dict_file)
        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        """parse the dict_file for the list of words"""
        return [w.strip() for w in dict_file]

    def random(self):
        """Return a random word"""
        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """word finder that excludes comments and blank lines"""
    def parse(self, dict_file):
        """parse dict_file and return list of words without comments and or blanks"""
        return [w.strip() for w in dict_file if w.strip() and not w.startswith("#")] 
