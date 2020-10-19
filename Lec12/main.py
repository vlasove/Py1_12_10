# Списочные выражения (list comprehension)

# nums = []
# for i in range(2, 101, 2):
#     nums.append(i)

#nums = [x for x in range(2, 101, 2)]

nums = [1,2,3,4,5]
str_nums = [str(x) for x in nums]
print(str_nums)

# Условие в списочном выражении
# nums = []
# for i in range(11):
#     if i % 2 == 0:
#         nums.append(i**2)
#     else:
#         nums.append(i)
nums = [i**2 for i in range(11) if i %2 == 0]
nums = [i**2 if i%2==0 else i for i in range(11)]

x = 10 if True else 11
print(x)
print(nums)