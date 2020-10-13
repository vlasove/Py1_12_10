# Пользователь вводит СКОЛЬКО-ТО положительных чисел (любое отрицательное число - знак завершения работы программы)
# Необходимо подсчитать максимальное и минимальное значения чисел, введенных пользователем

cur_max = -100
cur_min = 1000000000000000

while True:
    user_input = int(input())
    if user_input < 0:
        break 
    else:
        if user_input > cur_max:
            cur_max = user_input
        
        if user_input < cur_min:
            cur_min = user_input


print("Current max:", cur_max)
print("Current min:", cur_min)

