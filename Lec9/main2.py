# Множество - неупорядоченная (неиндексируемая) коллекция, способная хранить элементы любых типов, уникализируя последние.
# Строка - упорядоченная (индексируемая) коллекция, способная хранить элементы одного типа.


# Индексация
message = "Hello world!"
print("First letter:", message[0])
print("Second letter:", message[1])
print("Last letter:", message[len(message) - 1])
# last_id = len(collection) - 1
print("Another last letter:", message[-1])
print("Another prelast letter:", message[-2])


# Перебор элементов по индексам при помощи цикла (часто используется при сложных правилах переборов элементов)
for i in range(len(message) -1, 0, -2):
    print("Letter id:", i, "Letter value:", message[i])

# Просто подряд перебрать все элементы
for letter in message:
    print(letter)


# Проверка вхождения элемента(подстроки) в строку
if "H" in message:
    print("H in message!")

# Взятие длины
print("Length:", len(message))