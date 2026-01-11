# This is where I'll code

class AnagramChecker:
    def __init__(self, word):
        # 1. load the anagrams.txt
        with open('anagrams.txt', 'r') as f:
            self.word_list = f.readlines()
        # 2. checks words.txt that it's a real word
        # 3. sets the word as a attribute if it's real
        self.word = word
        
    # create method check_word to see if it's a word
    def check_word(self):
        return self.word in self.word_list
        #checks if the word is in words.txt

    # create get_anagram - returns all anagrams

    # create is_anagram - checks if 2 words are anagrams

meat = AnagramChecker("meat")