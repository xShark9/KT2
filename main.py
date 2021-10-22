from functools import reduce
from textblob import TextBlob
import re
import collections
from textwrap import TextWrapper, dedent
import ast

c= 0
das = 0
i = 0
a= ""
b = ""
u = ""
b =[]
u1=""
z={}
txt = []
file = open("ex.txt", "rt", encoding="utf-8")
data = file.read().replace('','')
datas = data
print(datas)
# Хранит все слова в 1 списке
words = data.split()
pattern = r'[.,-?!]'
data3 = re.findall(pattern,data)

for i in data3:
    a += str(i)

for char in set(a):
    z[char]=a.count(char)

# Хранит количество букв по каждому слову
words2 = [len(i.replace('-','').replace('«','').replace('»','').replace('!','').replace('?','').replace('.','').replace(',','')) for i in words]

words3 = list(map(len,words))

double = dict(zip(words,words2))
data = re.split(r'[.?!].',data)
coll = data
#print(coll)
coll = sorted(coll, key=lambda t: t.count(" "))
#print(coll)
#print('. '.join(coll))

for i in coll:
    u += str(i)

# Хранит в себе значение количества предложений
das = len(data)

data1 = [sentence.split() for sentence in data]

# Хранит в себе значение количества слов в предложении
data2 = [len(sentence) for sentence in data1]

# Соединение двух списков предложений и количества слов в них
l = list(zip(data, data2))
d = {
    'Всего слов': len(words),
    'Всего предложений': das,
    'Предложения': l,
    'Слова': double,
    'Знаки препинания': z,
}

print(d)

try:
    n = int(input("Введите n = "))
    if n <= das:
        try:
            split_text = re.split("(!|\.|\?)+", datas)
            txt = []
            for i in range(0, len(split_text) - 1, 2):
                    txt.append(split_text[i].lstrip() + split_text[i + 1])
            for i in range(0, len(txt), n):
                b = txt[i: n + i:]
                with open("файл.txt", "a") as file:
                    print(*b, file=file)
                print(b)
        except BaseException:
            print("")
    else:
        print("Вы ввели число больше, чем количество предложений")
except Exception:
    print("Введите целое число: ")





