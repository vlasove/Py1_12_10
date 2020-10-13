# Вещественные числа (float)

a_float = 23.5
b_float = 12.9 

# Ввод
# c_float = float(input())
# 1-3 как у int()
# 4) Разрешается наличие одного символа точки `.`

print("Sum:", a_float + b_float) # -,*, /

print("Pow:", a_float ** b_float)
print("Intger Div:", a_float // b_float)
print("Modulus:", a_float % b_float)


# Разрешается смешение числовых типов
first_int = 20
second_float = 20.5

print("Sum:", first_int + second_float) # -, *, /, **, %, //
# Результат всегда - вещественное число

third_float = 28.12341
third_int = int(third_float)
print("Third int:", third_int)
#float(third_int)