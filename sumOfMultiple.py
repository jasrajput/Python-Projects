
def sum_of_multiple(limit):
    summation = 0
    if limit:
        for i in range(limit):
            summation += i
            print(summation)
        return summation


summing = sum_of_multiple(20)
print(summing)
