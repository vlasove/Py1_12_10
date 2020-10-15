# Операции над двумя множествами
a_set = set([1,2,3,4])
b_set = set([3,4,5,6])

intersec = a_set.intersection(b_set)
print("Intersection:", intersec)

uni = a_set.union(b_set)
print("Union:", uni)

diff = a_set.difference(b_set)
print("Difference:", diff)

symm_diff = a_set.symmetric_difference(b_set)
print("Symm diff:", symm_diff)