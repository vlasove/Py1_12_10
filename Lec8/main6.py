# D3-4: S solution
first_walk = set() # Множество номеров автобусов на пути от дома до парка
second_walk = set() # Множество номеров автобусов на обратном пути

while True:
    message = input()
    if message == "":
        break 
    else:
        first_walk.add(message)

while True:
    message = input()
    if message == "":
        break 
    else:
        second_walk.add(message)

total_bus = first_walk.intersection(second_walk)
print(len(total_bus))