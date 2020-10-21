# Запись в файл
with open("output.txt", "a") as fhand: # 'w' - режим работы на ПОЛНУЮ ПЕРЕЗАПИСЬ ФАЙЛА
                                        # 'a' - режим работы на ДОЗАПИСЬ
    fhand.write("\n" + "Hey!") # .write() - принимает на вход единую строку (одну)
    fhand.writelines(["One\n", "Two\n", "Three\n"])


#import json 