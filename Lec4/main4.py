# if expression:
#     body
# elif expression2:
#     body2
# elif expression3:
#     body3 
# .....
# else:
#     body_else

num = int(input())

if num > 0 and num % 2 == 0:
    print("Positive even")
elif num > 0 and num %2 != 0:
    print("Positive odd")
elif num < 0 and num % 2 == 0:
    print("Non Positive even")
elif num < 0 and num %2 != 0:
    print("Non Positive odd")
else:
    print("Zero")