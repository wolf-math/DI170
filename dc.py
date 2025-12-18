word = input("type a string with consecutive duplicate letters: ")
new_word = ""

for letter in word:
    if word[letter] == word[letter - 1]:
        continue
    else:
        new_word += word[letter]

print(new_word)
