# Кортеж - упорядоченная (индексируемая) коллекция, способная хранить элементы любого типа, 
# и поддерживает неизменяемость коллекции


num_tup = (1,2,3,4,5) # tuple - кортеж

# Создание пустого кортежа
a_tup = ()
b_tup = tuple()

print("a_tup:", a_tup, "len:", len(a_tup), "type:", type(a_tup))

# Создание кортежа единичной длины
c_tup = (1,) # ставим запятую для того чтобы Python не снимал скобки
print(type(c_tup))

# Конкатенацию кортежей
left = (10, 20, 30)
right = (40,50, 60)

total = left + right 
print(total)


# Индексация
print("First elem:", total[0])
print("Last elem:", total[-1])
print("Slice:", total[1:4])

for i in range(len(total)):
    print("id:", i, "elem:", total[i])

for elem in total:
    print(elem)