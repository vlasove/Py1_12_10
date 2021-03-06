# 2. Области определения функций

# Тело функции - локальная область видимости для этой функции
# Внутри нее видны только те параметры, которы были ЛИБО там созданы
# ЛИБО поступили в качестве аргументов при вызове функции

# global - директива -> Теперь переменная с этим именем ВИДНА ВО ВСЕХ ОБЛАСТЯХ ВИДИМОСТИ 
# ДАННОГО МОДУЛЯ. КРОМЕ локальных областей тел функций

age = 22
if age > 20:
    def hello():
        print("Hello")
    hello()
else:
    hello()
hello()


# 2.2 Определение функции внутри функции

def add(a:int):
    """
    Внешняя функция. Принимает аргумент 'a' и возвращает функ. объект add2
    """
    def add2(b:int):
        """
        Внутренняя функция. Принимает 'b'. Знает про 'a' тк находится в одной локальной области
        Возврвщает сумму a + b
        """
        return a + b 
    return add2 

result = add(12)
# def add2(b:int):
#   return 12 + b

result = add(15)
# def add2(b:int):
#   return 15 + b
print("Result:", result, "Type:", type(result))
print("result(10):", result(10))

print("Closure result:", add(13)(17))


