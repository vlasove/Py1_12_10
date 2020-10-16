# D5 : H solution
valid_set = set(["Да", "ДА", "дА", "да"])

message = input()
#
if ((message[0] + message[-1] ) in valid_set)or ((message[-1] + message[0] ) in valid_set ):
    print("СОГЛАСЕН")
else:
    print("НЕ СОГЛАСЕН")