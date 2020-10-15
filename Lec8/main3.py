# Операции над множествами.
# Операции над одним множеством

nums = set([10, 20, 30, 40, 50, 50, 50])
print("Length:", len(nums))

total_sum = sum(nums) # sum() можно применять только к коллециям из числовых значений
print("Total sum:", total_sum)

cur_min = min(nums) # min()/max() - можно применять только к коллекциям, состоящих из СРАВНИМЫХ друг с другом элементов
cur_max = max(nums)
print("Min:", cur_min, "Max:", cur_max)


# Перебор элементов во множестве (в каком порядке будут перебираться - не известно)
for elem in nums:
    print("Current elem:", elem)