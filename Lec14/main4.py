# А как задать дефолтные параметры?
# ПРАВИЛО - параметры со значением по умолчанию ВСЕГДА УКАЗЫВАТЬ В КОНЦЕ ПЕРЕЧИСЛЕНИЯ ВСЕХ ПАРАМЕТРОВ ФУНКЦИИ
def add( a:int = 1, b:int = 1, c:int = 1) -> int:
    """
    Расчет супер-суммы
    """
    res = a + b **2 + c ** 3 
    return res 

print(add(1,2,3))
print(add(1,2))
print(add(1))
print(add(b=20, c = 30, a= 20))
