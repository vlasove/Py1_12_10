# Строки (str)

first_str = 'a'
empry_str = ''
second_str = "Some string"

print("Sample:", first_str, "Type:", type(first_str))
print("Sample:", empry_str, "Type:", type(empry_str))
print("Sample:", second_str, "Type:", type(second_str))

# Конкатенация
concat = first_str + second_str
print("Result concat:", concat)

concat_mult = "Hello" * 3
print("Result concat mult:", concat_mult)

# Подсчет длины строки len()

print("Sample:", second_str, "Len:", len(second_str))
print("Sample:", empry_str, "Len:", len(empry_str))

# Ввод
input_str = input()
a_int = 23
b_float = 23.999

answer = str(a_int) + "#######" + str(b_float)
print("Answer:", answer)