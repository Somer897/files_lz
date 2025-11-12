import docx
import matplotlib.pyplot as plt
import pandas as pd

#открытие файла
doc = docx.Document('lion.docx')

#где будет находиться текст
text = []

#список для букв
letters = {}

#список для слов
words = {}

#чтение текста
for paragraph in doc.paragraphs:
    text.append(paragraph.text)

#разбиение на абзацы
full_text = '\n'.join(text)

#перевод букв на строчный тип
full_text = full_text.lower()
word_text = full_text.split()
#удаление ненужных символов
punc = '/?!.,"«»[](){}-–:;—_1234567á890äâѵ°ȃ=ôęï―ç…όù*îö№üóûòêèàé’'
for i in range(0, len(punc)) :
    if punc[i] in full_text: 
        full_text = full_text.replace(punc[i], '')

#цикл для нахождения слов в тексте
for i in word_text:
    #если слово есть в словаре - счетчик накручивается
    if i in words:
        words[i] += 1
        #если слова нету, то добавляет его в словарь
    else:
        words.update({i:1})


#цикл для нахождения букв в тексте
#"влезаем" в слова в тексте
for i in full_text:
    #а теперь из слов в буквы
    for j in i:
        #если есть буква в словаре, то счетчик +1
        if j in letters:
            letters[j] += 1
        #если буквы нету, то добавляет ее в словарь
        else:
            letters.update({j:1})

#создание осей для графика
keys = list(letters.keys())
values = list(letters.values())

#создаем график через бар, т.к. он создаёт НУЖНЫЙ график для нас, в отличии от plot
plt.bar(keys, values)

#называем оси и сам график
plt.xlabel("буквы")
plt.ylabel("Количество")
plt.title("Гистограмма количества букв")

#показ графика
plt.show()

#save
doc.save('lion.docx')

#создаем списки для слов, количества встреч в "раз" и в %
word = [] 
kol = []  
percent = [] 

#заполняем эти списки с помощью нашего словаря
for key in words.keys(): 
    kol.append(words[key])
    word.append(key)
    #высчитываем процент встреч слов
    percent.append(int(words[key])/len(words)*100)

#делаем словарь с помощью этих 3 списков
slovli = {'Слово': word, 'Частота встречи, раз' : kol, 'Частота встречи в %' : percent}

#переделываем список в таблицу
table = pd.DataFrame(slovli)

#выводим таблицу
print(table)