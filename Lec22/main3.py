import time
from main2 import my_decorator

def benchmark(func):
    """
    Декоратор замеряющий время выполнения функции
    """
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("Total time is:", end-start)
    return wrapper 



@my_decorator
@benchmark
def worker():
    lst = [i**2 for i in range(1, 100000)]
    for i in range(len(lst)):
        lst[i] += 1

worker()
