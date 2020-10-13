# Бзовые типы данных.
# 5 базовых типов в языке: int, float, bool, str, NoneType

# Целые числа (или int)
a_int = 10
b_int = 20

print("Sum:", a_int + b_int)
print("Sub:", a_int - b_int)
print("Mult:", a_int * b_int)
print("Div:", a_int / b_int)

print("Integer Div:", a_int // b_int)
print("Modulus:", a_int % b_int)

print("Power:", a_int ** b_int)


# Явное приведение типов к целому числу.
first_int = int(input()) # int("10") -> 10
second_int = int(input()) # int("20") -> 20

print(first_int + second_int)

# Что можно преобразовать к числовому типу?
# 1) Данные состоят ЦЕЛИКОМ из числовых символов
# 2) Данные состоят из числовых символов + разрешается символ `-` в самом начале
# 3) Разрешается обрамление символьно-числовой последовательности пробелами/табуляциями/переносами (символы пустоты)
