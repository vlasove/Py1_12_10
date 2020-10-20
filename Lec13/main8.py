# Freq Analysis - сколько раз каждое слово входит в строку message
message = "hello bob bob hello world bob hello world bob kek kek bob world"

counter = {}
for word in message.split():
    if word in counter.keys():
        counter[word] += 1 # Значения по ключу изменяемы
    else:
        counter[word] = 1

print(counter)

