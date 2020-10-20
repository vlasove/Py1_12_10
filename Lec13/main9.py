# D6:D pre-solution

birth_calendar = {}

n = int(input())
for _ in range(n):
    message = input() # Витя 12 дек
    words = message.split()
    name, month = (words[0], words[-1])

    if month in birth_calendar.keys():
        birth_calendar[month].append(name)
    else:
        birth_calendar[month] = [name]

# Считать месяцы и вывести в отсортированном порядке имена людей
    
