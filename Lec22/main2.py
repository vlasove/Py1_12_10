# 4. Декорирование
# Декоратор - это функциональное замыкание, принимающее в качестве параметра функци.
# и заворачивающее его в дополнительные участки программного кода, без изменения
# кода оборачиваемой функции

def my_decorator(func):
    """
    Декоратор
    """
    def wrapper():
        """
        Функциональная обертка
        """
        print("First line from decorator")
        func()
        print("Second line from decorator")
    return wrapper 

@my_decorator
def hello():
    print("Hello world!")

@my_decorator
def goodbye():
    print("Good bye!")

hello()

#goodbye = my_decorator(goodbye)
goodbye()