weight = int(input("Weight: "))
unit = input("(L)bs or (k)g: ")
if unit.upper() == 'K':
    converted = weight / 0.45
    print("You are " + str(converted) + " Pounds")
else:
    converted = weight * 0.45
    print("You are " + str(converted) + " Kg")

# pound to kg (mosh approach)
weight = input("What's your weight in pounds? ")
# 100
kg = int(weight) * 0.45
print(kg)

# pound to kg my Approach
weight = input("What's your weight in pounds? ")
# 100
kg = int(weight) / 2
result = kg / 10
print("Your weight in kg is: " + str(result))