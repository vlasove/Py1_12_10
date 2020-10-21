# Чтобы открыть файл надо
fhand = open("input.txt", "r") # Первый аргумент - путь до файла, В случае если файл в другой точки системы -
# абсолютный путь , Второй аргумент - режим работы с файлом r - read
# fhand = FileHandler
#print(fhand) # fhand не хранит никакой информации про начинку файла
line = fhand.read()
print(line)

fhand.close()