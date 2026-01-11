# 0. open the file
def file_open():
    with open('./words.txt', 'r') as f:
        words = f.readlines()
    
    words_list = [word.strip() for word in words]

    # same as
    # words_list = []
    # for word in words:
    #     words_list.append(word.strip())

    return words_list

# 1. check if the given word is valid
def is_valid(word, words):
    word_upper = word.upper()
    if word_upper in words:
        return True
    else:
        return False
    
# 3. create `is_anagram` that returns True if 2 words are anagrams
def is_anagram(word1, word2):
    word1_list = list(word1)
    word2_list = list(word2)

    word1_list.sort()
    word2_list.sort()

    if word1_list == word2_list:
        return True
    else:
        return False

# 2. find anagrams for the given word

def find_anagrams(user_word, words_list):
    user_word_upper = user_word.upper()

    anagrams = []
    for word in words_list:
        if is_anagram(user_word_upper, word):
            anagrams.append(word)

    return anagrams

def main():
    words = file_open()
    print("Anagram checker!!!")
    user_word = input("Input a word to find its anagrams: ")

    if is_valid(user_word, words):
        results = find_anagrams(user_word, words)
        print(results)
    else:
        print("That is not a word")


main()

