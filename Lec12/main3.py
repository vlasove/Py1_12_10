# D6: B pre-solution
n = int(input())

queue = []

for _ in range(n):
    command = input()
    if "Кто послед" in command:
        #Кто последний? Я - Кузнецов.
        lastname = ..... 
        queue.append(lastname)
    elif "Я только спро" in command:
        #Я только спросить! Я - Иванова.
        ....
        lastname = ...
        queue.insert(0, lastname)
    else:
        # "Следующий!"
        if len(queue) > 0:
            user = queue.pop(0)
            print("Заходит", user + "!")
        else:
            print("В очереди никого нет.")