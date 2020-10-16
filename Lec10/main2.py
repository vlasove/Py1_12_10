message = "HellO"
#print(dir(message))

low = message.lower()
print("Lower:", low)
up = message.upper()
print("Upper:", up)
cap = message.capitalize()
print("Capitalize:", cap)


sample = "                  Bob               Alice           "
new_str = sample.strip()
print(new_str, len(new_str))