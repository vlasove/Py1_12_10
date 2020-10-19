# Вложенные списки
vec = [[1,2,3], [4,5,6]]
print("vec:", vec, "len:", len(vec))
print(vec[1][-1])


for inner_vec in vec:
    for elem in inner_vec:
        print(elem)


# Преобразование коллекций
message = "Hello world"
message_list = list(message)
print(message_list)
message_form_list = str(message_list) # Преобразует элементы к сстроковым типам?
print(message_form_list)

print(set(message))