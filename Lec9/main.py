a_set = set([1,2,3,1,1,1,2,3,4, "hello"])

# dir() -> отобразить все доступные методы для данного объекта
#print(dir(a_set))

# .remove() -> позволяет удалить конкретный элемент из множества
print("Before deleting:", a_set)
if "hello" in a_set:
    a_set.remove("hello")

print("After deleting:", a_set)

# .pop() -> позволяет удалить случайный элемент
a_set.pop()
print("After pop:", a_set)