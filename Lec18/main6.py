# Как обрабатывать исключения? Часть 2.
def dangerous(n:int):
    """
    Делит на n
    """
    return 1 / n


try:
    n = int(input())
    dangerous(n)
except ZeroDivisionError as z_err:
    print("Div by zero:", z_err)
except ValueError as v_err:
    print("Can not convert:", v_err)
except:
    print("alles")
else:
    # Блок else выполняется только в ситуациях, когда исключение не было выброшено совсем
    print("Else block")
finally:
    # Finally работает в любой ситуации. Было исключение или нет - неважно
    print("Finally block")

