i = 0 
while i < 10:
    print(i, i**2)
    i += 1



for i in range(20, 1, -3): # range(start, stop[, step)
    print(i, i**2)

# В качестве start-stop-step разрешается использовать только ЦЕЛЫЕ числа

print("Шаг по умолчанию") # range(start, stop, step=1)
for j in range(0, 10):
    print(j, j**2)


counter = int(input())
print("Старт по умолчанию")# range(start=0, stop, step=1)
for j in range(counter):
    print(j, j**2)
    if j == 8:
        break 