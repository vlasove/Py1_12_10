# Возврат значений из функций
def funcname():
    a = 20
    return a + 10 # Передача значения вызывающей стороне + немедленное завершение работы функции

res = funcname()
print(res)

# А что если
def func_empty():
    a = 20 
    #return None - по умолчанию функция возвращает None
    return 

result = func_empty()
print(result)


# Вовзрат нескольких значений
def func_mult():
    tup = (1,2,3)
    return tup 

a,b,c = func_mult()
print("a:", a, "b:", b, "c:", c)