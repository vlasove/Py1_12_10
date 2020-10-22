# Исключительная ситуация - ситуация, после которой дальнейшее выполнение кода невозможно
import json


print( 1 / 0)
# Файла нет
with open("input2.json", "r") as fhand:
    answer = json.load(fhand)