# Множество - это ссылочный тип
a_set = set([1,2,3,4])
b_set = a_set #.copy() -> создаем новую область в памяти и выдаем на нее ссылку

b_set.add(10)
print("a_set:", a_set)
print("b_set:", b_set)