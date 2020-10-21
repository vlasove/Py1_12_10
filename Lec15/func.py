# Модуль - любой файл с расширением .py

def add(a:int, b:int):
    """
    This func for a + b 
    """
    return a + b

def sub(a:int, b:int):
    """
    This func for a - b 
    """
    return a - b 


def mult(a:int, b:int):
    """
    This func for a * b
    """
    return a * b 

def div(a:int, b:int):
    """
    This func for a / b
    """
    return a / b 

temperature =  36.6

#print(__name__) # Переменная-caller. __main__ если модуль вызван напрямую
# в случае если модуль был импортирован, то __name__ примет значение имени модуля
if __name__ == "__main__":
    print(add(2,3) + mult(3,4) + sub(10, 2) + div(2,2))