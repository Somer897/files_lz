f = open('lion.docx', 'r').read()
text = f.split()
words = {}

for item in text:
    if item in words:
        words[item] += 1
    else:
        words.update({item:1})

print(words)