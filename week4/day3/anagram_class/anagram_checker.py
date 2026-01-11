class Anagram:
    def __init__(self, word):
        with open('./words.txt', 'r') as f:
            words = f.readlines()
            self.words_list = [word.strip() for word in words]
        
        if word.upper() in self.words_list:
            print(f"user word is {word}")
            self.word = word.upper()
            self.is_word = True
        else:
            print("not a word")
            self.is_word = False

    def is_anagram(self, word1):
        word1_list = list(word1)
        word2_list = list(self.word)

        word1_list.sort()
        word2_list.sort()

        if word1_list == word2_list:
            return True
        else:
            return False

    def find_anagrams(self):
        anagrams = []
        for word in self.words_list:
            if self.is_anagram(word):
                anagrams.append(word)

        return anagrams
