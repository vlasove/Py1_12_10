import re 

# Содержится 6 функций:
# re.match() - поиск по шаблону в начале строки
# re.search() - поиск по шаблону во всей строке. Отдает первый удовлетворивший шаблону
# re.findall() - поиск по шаблону во всей строке. Возвращает СПИСОК всех элементов ...
# re.split() - разделяет строку по шаблону
# re.sub() - ищет шаблон в строке. Если находит - заменяет его на другую подстроку
# re.compile() - предкомпиляция шаблона

# 1. re.match()
answer = re.match(r'AV', 'AVAV VAVAV VAV')
#print(answer.group(0)) если наход - можно посмотреть
# если не найдет - answer -> None

print("Start id:", answer.start())
print("End id:", answer.end())

# 2. re.search()
answer = re.search(r'Bobby', 'This is Bobby. He is Bobbynice guy')
if answer is None:
    print(answer)
else:
    print("Finded:", answer.group(0))
    print("Start id:", answer.start())
    print("End id:", answer.end())

# 3. re.findall()
answer = re.findall(r'Bobby', 'This is Bobby. He is Bobbynice guy')
print(answer)

# 4. re.split()
answer = re.split(r'q', 'asdqwdqdquwqdqdqwdqwdnqjwdqqqdqdqqd')
print(answer)


# 5. re.sub()
answer = re.sub(r'Bobby', 'Alice', 'This Bobby. Bobby nice guy.')
print(answer)


# 6. re.compile()
pattern = re.compile('Bobby')
answer = pattern.findall('This is Bobby. He is Bobbynice guy')
print(answer)


# Что можно использовать в качестве шаблона?
# .                  любой символ, кроме \n
# +                  единичное и более вхождение шаблона СЛЕВА строки
# *                  нулевое и более вхождений шаблона СЛЕВА строки
# \w                 любую цифру или букву (\W - все символы, кроме букв и цифр)
# \d                 любую цифру [0-9] (\D - все кроме цифр)
# ^ и $              начало и конец строки 
# [..]               любой символ кроме тех что в скобках указан


answer = re.findall(r'.', 'Bobby nice guy')
print(answer)

answer  = re.findall(r'@\w+.\w+', "bobby@yandex.ru, victor@google.com, fedya@mail.ru, masha@rambler.ru")
print(answer)

# Вытащить первое слово из строки
answer = re.findall(r'^\w+', 'Bobby nice guy')
print(answer)