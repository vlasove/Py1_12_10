with open("input.txt", "r") as fhand: # with - интерфейсный оператор, вызывающий обратную функцию по завершению
    content = fhand.read() # считывает весь файл целиком
    print(content)
    content2 = fhand.read() # повторное считывание внутри одного открытия продолжается с места прошлого закрытия считывания
    print(content2)
    #print(fhand.readable())


with open("input.txt", "r") as fhand:
    first_line = fhand.readline()
    print(first_line)
    second_line = fhand.readline()
    print(second_line)
    third_line = fhand.readline()
    print(third_line)
    fourth_line = fhand.readline() #== "" # EOF
    print(fourth_line)

with open("input.txt", "r") as fhand:
    all_lines = [msg.strip() for msg in fhand.readlines()]
    print(all_lines)