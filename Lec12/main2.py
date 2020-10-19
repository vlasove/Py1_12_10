# Обработка строковых последовательностей
message = "Hello world I'm Bob and I'm 99 years old"

# Строковый метод split() позволяет разбить строку на список слов
words = message.split()
print(words)

# А как из списка слов сделать обратно строчку?
message_new = ", ".join(words) # Принимает на вход список из строк и разделяет их неким сепаратором " "
print(message_new, type(message_new), len(message_new))



# А что если нужно собрать строку из не строковых литералов?
nums = [10, 20, 30, 40, 50, 60]
print(", : ,".join([str(x) for x in nums]))