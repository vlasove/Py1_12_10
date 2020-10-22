# Как обрабатывать исключения?
def dangerous(n:int):
    """
    Делит на n
    """
    return 1 / n

# Блок-обработчик исключения
try:
    #Помещается потенциально опасный код
    n = int(input())
    dangerous(n)
# Типизированные обработчики
except ZeroDivisionError as z_err:
    print("Division by zero! Try another value!:", z_err)
    #print(dir(z_err)) что можно делать с z_err
except ValueError as v_err:
    print("Can not convert to int:", v_err)
except KeyboardInterrupt as k_err:
    print("Dont use CTRL+C:", k_err)
except BaseException as b_err:
    print("something:", b_err)


print("Done!")
