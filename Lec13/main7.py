# Что можно использовать в качестве ключей и значений?
# Ключи - любые неизменяемые и УНИКАЛЬНЫЕ объекты
# Значения - любые объекты
some = {1 : "unique", 23.5 : "unique", False : "unique", None: "unique", "a": "unique", (10, 20) : "unique", 1 : "non unique"}
for k in some.keys():
    print("Key:", k, "Val:", some[k])