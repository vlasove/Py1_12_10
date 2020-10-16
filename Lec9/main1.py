# D5: E solution
n_days = int(input())

total = set() # множество студентов, которые были на всех занятиях

for i in range(n_days):
    # каждая итерация - отдельный день
    current_students = set() # множество студентов в i-ый день
    n_students = int(input()) # количество студентов в i-ый день
    for _ in range(n_students):
        current_students.add(input())
    
    if i == 0: # это первый день
        total = total.union(current_students) # все кто был в первый день - были во всем семсетре
    else:
        total = total.intersection(current_students) # пересекаем с множествами людей, кто были во все остальные дни

print(len(total))

