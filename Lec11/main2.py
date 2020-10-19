# Список - ссылочный тип
a_list = [1,2,3]
b_list = a_list[:] # .copy() и [:] эквивалентны в создании полных копий списков
b_list.append(10)

print("a_list:", a_list)
print("b_list:", b_list)