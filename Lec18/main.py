import json # Модуль для работы с .json файлами

# Считывание из .json
answer = None # Преинициализация переменной для хранения результата вызова .load()
with open("input.json", "r") as fhand:
    answer = json.load(fhand)

print(answer)


# Запись в .json
data = {
    "name" : ("Bob", "hjgj"),
    "is_valid": True,
    "chars" : ['Char1', "Char2", "Char3", {"one": 1, "two":2}],
    "location" : None,
    "age" : 29,
}

with open("output.json", "w") as fhand:
    json.dump(data, fhand, indent=4) # indent - параметр , отвечающий за форматирование файла .json

# Сериализация в json - преобразование байтовой последовательности в содержание json файла
# Десериализация json - считывание данных из json и конвертация в байты