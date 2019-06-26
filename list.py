
# 2d list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# matrix[0][1] = 20
# for row in matrix:
#     for item in row:
#         print(item)

# program to find duplicates
numbers = [2, 2, 22, 45, 12, 22]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)


lis = [1, 'jass', 'sam', 'jas', 2, 'rathore']
# print(lis[-5:-3])
# print(lis[4::-2])

a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print(a[2:-2])
# print(max(a[2:4] + ['grault']))  # output ['bar', 'baz']

x = [10, [3.141, 20, [30, 'baz', 2.718]], 'foo']
print(x[1][2])
# print(f'x: {x}')

