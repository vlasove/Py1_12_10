# Инициализация пустого словаря
empty = {}
empty_d = dict()

print(empty, len(empty), type(empty))

# Инициализация не пустого словаря
nums = {10:"ten", 6:"six"}
print(len(nums))
# Добавление новой пары
nums[5] = "five" # Для инициализации новой пары необходимо в строке присваивания указать как новый ключ так и значение
print(nums)


# Проверка вхождения
if 5 in nums: # проверка вхождения КЛЮЧА
    print("5 in nums")

# Явная проверка вхождения ключа
if 5 in nums.keys():
    print("5 in nums.keys()")

# Явная проверка вхождения значения
if "six" in nums.values():
    print("`six` in nums.values()")


# Перебор пар при помощи цикла for
for s in nums:
    print(s)

# Явный перебор ключей
for k in nums.keys():
    print("Key:", k, "value:", nums[k])

# Явный перебор значений
for v in nums.values():
    print("Val:", v)


# Перебор пар
for k, v in nums.items(): # .items() - возвращаеь набор двуэлементных кортежей
    print("Key:", k, "Val:", v)