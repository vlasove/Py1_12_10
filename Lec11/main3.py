# Изменяемость
a_list = ["one", "two", "five"]
a_str = "Qello world"

# Подтверждение неизменяемости базового типа
b_str = "H" + a_str[1:]
print(b_str)

# Списочная изменяемость
a_list[-1] = "three"
print("a_list:", a_list)