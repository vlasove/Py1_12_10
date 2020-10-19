a_list = ["one", "three", "five"]
a_list.append("three") # Операция добавления элемента в конец
print("Total:", a_list)

a_list.insert(0, "zero") # Операция добавления в произвольное место
print("Total:", a_list)


elem = a_list.pop(0) # Удаление и возврат проиндексированного элемента (по умолчанию - последний)
print("Last elem:", elem, "List:", a_list)

if "three" in a_list:
    a_list.remove("three") # Удаление элемента по его значению
print("After remove:", a_list)