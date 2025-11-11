import docx
import matplotlib.pyplot as plt

#открытие файла
doc = docx.Document('lion.docx')

#где будет находиться текст
text = []

#списокдля букв
letters = {}

#чтение текста
for paragraph in doc.paragraphs:
    text.append(paragraph.text)

#разбиение на абзацы
full_text = '\n'.join(text)

#перевод букв на строчный тип
full_text = full_text.lower()

#удаление ненужных символов
punc = '/?!.,"«»[](){}-–:;—_1234567á890äâѵ°ȃ=ôęï―ç…όù*îö№üóûòêèàé’'
for i in range(0, len(punc)) :
    if punc[i] in full_text: 
        full_text = full_text.replace(punc[i], '')


#счетчик слов
#задаем искомое слово
word = str(input('какое ваше слово: '))
#находим количество слов
kol = full_text.count(word)
#вычисляем процент использвания
percent = ((kol / len(full_text))*100)

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

#create document
dox = docx.Document()

#create here table
table = dox.add_table(rows = 2, cols = 3)

#give style to the table
table.style = 'Table Grid'

#give data to cells of the table
table.cell(0, 0).text = "Слово"
table.cell(0, 1).text = "Количество повторений"
table.cell(0, 2).text = "% от остальных слов"
table.cell(1, 0).text = str(word)
table.cell(1, 1).text = str(kol)
table.cell(1, 2).text = str(percent)

#save document
dox.save('Word.docx')