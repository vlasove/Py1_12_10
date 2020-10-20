# Изменяемость кортежа
sample = ("one", 1, "eins")
sample[1] = 2000

# Неизменяемость кортежа - неизменяемость храниммых значений
total = ([1,2,3], [2,3,4,5])
print("total before:", total)
total[0].append(20)
print("total after:", total)