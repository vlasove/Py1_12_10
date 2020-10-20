a_list = [0,1,2,3,4,5,6,7,8,9,10]
b_tuple = (0,1,2,3,4,5,6,7,8,9,10)
c_set = set([0,1,2,3,4,5,6,7,8,9,10])
d_str = "0,1,2,3,4,5,6,7,8,9,10"

print("Collect:", type(a_list), "Size:", a_list.__sizeof__(), "Bytes")
print("Collect:", type(b_tuple), "Size:", b_tuple.__sizeof__(), "Bytes")
print("Collect:", type(c_set), "Size:", c_set.__sizeof__(), "Bytes")
print("Collect:", type(d_str), "Size:", d_str.__sizeof__(), "Bytes")