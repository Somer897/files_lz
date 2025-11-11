import docx
import matplotlib

#открытие файла
doc = docx.Document('lion.docx')

#где будет находиться текст
text = []

#чтение текста
for paragraph in doc.paragraphs:
    text.append(paragraph.text)

#разбиение на абзацы
full_text = '\n'.join(text)

#счетчик слова
word = str(input('какое ваше слово(буква): '))
kol = full_text.count(word)

print(kol)