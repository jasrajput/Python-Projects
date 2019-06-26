def collatz(number):
    if number % 2 == 0:
        result = number // 2
        return result
    else:
        result = 3 * number + 1
        return result


num = int(input("Enter a number"))
while num != 1:
    num = collatz(num)
    print(num)

a = 2
b = 4
a, b = b, a + b
print(a, b)
