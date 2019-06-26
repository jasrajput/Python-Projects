from ecommerce.shipping import cal_shipping
import ecommerce.shipping
from ecommerce import shipping
from largestNumber import find_max
from class_practice_2 import *

numbers = [20, 2, 4, 12, 10]
number = find_max(numbers)
print(number)

ship = cal_shipping()
print(ship)

ecommerce.shipping.cal_shipping()
shipping.cal_shipping()

car1 = Car('Audi', 2018, 1980)
print(car1.detail())
print(car1.update_odometer(23500))
print(car1.increment_odometer(20))
print(car1.detail())

myCar = ElectricCar(1990, 'Tesla', 2019)
print(myCar.detail())
myCar.battery.describe_battery()
myCar.battery.get_range()
myCar.battery.upgrade_battery()
myCar.battery.get_range()