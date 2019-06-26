def speed_check(speed):
    demerit_point = 0
    total = 0
    if speed < 70:
        print('ok')
    elif speed > 70:
        demerit_point = (speed - 70) / 5
        total += demerit_point
        if demerit_point > 12:
            print("License suspended")
    else:
        print(total)
    return total


check = speed_check(200)
print(check)
