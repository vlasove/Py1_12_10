# Генераторные выражения
lst = [10, 20, 30, 40, 50] * 10
gen_obj = (x for x in lst)

print("Lst size:", lst.__sizeof__())
print("Gen obj:", gen_obj.__sizeof__())

# print(len(gen_obj)) - функция len() возвращает количество элементов только в старых версиях Python 3.7 и нжие

for elem in gen_obj:
    print("Element:", elem)
    break