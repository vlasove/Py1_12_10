# Как обрабатывать исключения?
def dangerous(n:int):
    """
    Делит на n
    """
    return 1 / n

# Блок-обработчик исключения
try:
    #Помещается потенциально опасный код
    print("In try block")
    dangerous(2)
    print("After 1/0")
except:
    # Выполняется если внутри try произошла исключительная ситуация
    print("Except block working!")

print("Done!")
