# Look into pathlib

f = open('./week3/day5/secrets.txt', 'r+')
text = f.read()
print(text)
f.write('\nbut I normally eat lettuce')
f.close()

# with open('./week3/day5/secrets.txt', 'r+') as f:
#     text = f.read()
#     print(text)
#     f.write('\nbut I normally eat lettuce')