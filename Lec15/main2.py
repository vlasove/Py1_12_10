# Mapping 
elements = ['1', '2', '3', '4', '5', '6'] # Хочу прибавить единицу к каждому числу , предварительно превратив все строки
# в int

# Решение с помощью list comprehension
elements = [int(x) + 1 for x in elements]
print("After LC:", elements)

elements2 = ['1', '2', '3', '4', '5', '6']
# Решение при помощи функции map
result_map = list(map(lambda x : int(x) + 2**3, elements2)) # Первый аргумент - функ.объект (С ОДНИМ ПАРМЕТРОМ),
# который применяется ко всем элемента коллекции; второй аргумент -
# коллекция, по которой можно ходить циклом for (итераторы - iterable)
print("After MAP():", result_map)