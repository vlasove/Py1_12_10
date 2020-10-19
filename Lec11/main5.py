# Сколько раз в списке встречается тот или иной элемент?
num = [10, 20, 30, 10, 20, 10, 20, 10]
print("10 counts in list:", num.count(10))

# Индекс первого вхождения элемента
print("20 id is:", num.index(20))

ids = []
for i in range(len(num)):
    if num[i] == 10:
        ids.append(i)

print(ids)