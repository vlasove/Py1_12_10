# Декорирование
# 1. Функции - это объекты первого рода (их можно присваивать в переменные, передават ькак аргументы и т.д.)
def hello():
    print("Hello world")


tmp = hello # Функции можно присваивать в переменные
sampler = [tmp, hello, hello]
for f in sampler:
    f()


# Передача функции в качестве параметра
def outer_func(f):
    print("First line outer func")
    f()
    print("Second line outer func!")

# Возврат функции
def reproductor():
    return lambda x : 2*x**2

result = reproductor()


print("Result(2):", result(2))
print("Result(10):", reproductor()(10))