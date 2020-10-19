# Сортируемость
num = [20, 30, 1, 2, -10, 2, 18, 9, 200]

# 2-ой способ - использовать отсортированную копию без изменения оригинала
sort_num = sorted(num, reverse=True)
print("Sorted copy:", sort_num)
print("Origin num:", num)
# 1 - ый способ сортировка с изменением текущего списка
num.sort(reverse=True) # reverse - сортировка в обратную сторону
print("Num:", num)


# Сортировка строк
names = ["Alice", "Bob", "Fedya", "Alex", "Tim"]
names.sort()
print("Names:", names)

print(dir(names))
