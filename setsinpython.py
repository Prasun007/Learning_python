s = set(["One", "Two", "Three", 1, 2, 3])# Use set() and insert elements for creating a set.
# Or you can insert elements in the way
l = [4, 5, 6]
s1 = set(l)
s1.add(72)# Only unique elements can be inserted in set
s1.add(72)
print(s1)
# Where as in list one element can be inserted more than once.
l2 = []
l2.append(89)
l2.append(89)
print(l2)
s1.remove(5)
print(s1)

