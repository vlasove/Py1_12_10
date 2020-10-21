import math 
from calculus import rectangles # Обращение к пакетному модулю с разделенным пространством имен
from calculus.rectangles import area #Совмещение пространств имен модуля rectangles пакета calculus 
# для функции area

print("pi:", math.pi)
print("e:", math.e)

#print(dir(math)) # Посмотреть на все доступные элементы в модуле

print("Perimeter(10,20):", rectangles.perimeter(10,20))
print("Area(10,20):", rectangles.area(10, 20))


from flask import Flask

# setup.py => создание данного файла позволит вам устанавливать пользовательские модули через pip 
# под всю систему