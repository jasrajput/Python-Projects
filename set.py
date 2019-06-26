# Don’t forget that set elements must be immutable. For example, a tuple may be included in a set:
# But lists and dictionaries are mutable, so they can’t be set elements:
# operators: &(intersection), - (difference), | (union), ^(symmetric difference)
x = {'jas', 'yash', 'samar', 30, 20, 30 ,'yash', 'YASH', 'Yash'}
print(type(x))

x1 = {'boo', 'ball', 'taker'}
x2 = {'boo', 'brock', 'rock'}
x3 = {'so', 'bo'}
print(x1 | x2 | x3)  # operator {operand both should be sets}
print(x1.union(x2, x3))  # method {union method take any iterable as an arg convert it into set}
print(x1 & x2)
print(x1.intersection(x2))
print(x1 - x2)
print(x1.difference(x2))
print(x1 ^ x2)
print(x1.symmetric_difference(x2))
print(x1.isdisjoint(x2))  # x1.isdisjoint(x2) returns True if x1 and x2 have no elements in common:


