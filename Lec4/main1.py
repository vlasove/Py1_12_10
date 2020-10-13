a_int = 10
b_int = 20

expression = (a_int > 5) and (b_int < 30)



if expression:
    print("if body working")

print("STOP WORKING")

### Операции сравнения
print("5 > 3", 5 > 3)
print("5 >= 5", 5 >= 5)
print("3 < 5", 3 < 5)
print(" 3 <= 7", 3<=7)
print("5 == 5", 5 == 5)
print("4 != 5", 4 != 5)
print("3.0 == 3", 3.0 == 3)

### Логика над строками
name = "Water"

print("`Wat` in Water", 'Wat' in name)

email = "qwerty@gmail.com"
if "@" in email:
    print("This is valid email")
    print("Email:", email)

