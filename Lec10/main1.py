message = "Hello world!"
#hello = message[0] + message[1] + message[2] + message[3] + message[4]
hello = message[2::3] # [start=0:stop=len(message):step=1]
print(hello)


inverse = message[::-1]
print(inverse)

for letter in message[0:8:2]:
    print(letter)