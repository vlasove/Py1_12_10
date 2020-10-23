# Генератор - это "ленивый" итерируемый объект. Следующую итерацию начинает
# ТОЛЬКО по требованию
def sample_gen(num):
    """
    Генератор чисел от num до 0
    """
    print("Generator started")
    while num > 0:
        yield num**2 # yield - возврат значения и запоминание состояния вызова функции. В следующий раз выполнение начнется с этого места
        num -= 1




values = sample_gen(4)
print("Next elemt:", next(values))
print("Next element:", next(values))
print("Next element:", next(values))
print("Next element:", next(values))
#print("Next element:", next(values))

lst = [i**2 for i in range(1, 100000)]
print("Lst size:", lst.__sizeof__())

values_new = sample_gen(100000)
print("Generator size:", values_new.__sizeof__())
# for elem in values_new:
#     print("Current element:", elem)


