# Список - упорядоченная (индексируемая) коллекция, способная хранить элементы ЛЮБОГО типа.

# Пустой список
a_list= []
b_list = list() # Вызов конструктора

print("a_list:", a_list, "len:", len(a_list), "type:", type(a_list))

# Преинициализированный список
c_list = ["one", "two", "three", 4]


# Обращение к элементам
print("id=0,", c_list[0])
print("id=last,", c_list[-1])
# Выход за границы
#c_list[10]


# Операции среза
print(c_list[0:2])


# Базовый функционал
first = [1,2,3]
second = [4,5,6]

concat = first + second 
print("concat:", concat)

concat_mult = [0] * 100
print(concat_mult)

print("len:", len(concat))
print("sum:", sum(concat))
print("min/max:", min(concat), "/", max(concat))

# Индексируемый цикл for
for i in range(0, len(concat), 1):
    print("Id =", i, "Elem =", concat[i])

# Поэлементный цикл for
for elem in concat[::-1]:
    print("Elem =", elem)