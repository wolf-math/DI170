from anagram_checker import Anagram

def main():
    print("Welcome to the Anagram Checker!!!")
    print("This is the funnest game ever!!1")

    user_word = input("Please enter a word: ")

    user_word_instance = Anagram(user_word)

    if user_word_instance.is_word:
        results = user_word_instance.find_anagrams()
        print(results)

if __name__ == "__main__":
    main()
