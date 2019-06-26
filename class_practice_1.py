from Restaurant import Restaurant


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine):
        super().__init__(restaurant_name, cuisine)
        self.flavour = []

    def describe_flavors(self, flavour):
        self.flavour = flavour
        print("Flavors are: " + str(self.flavour))


restaurant1 = Restaurant('chawla chicken', 'tangdi')

restaurant1.describe_restaurant()
restaurant1.customer_number()
restaurant1.set_number_served(20)
restaurant1.set_number_served(100)
restaurant1.customer_number()
restaurant1.increment_customer(10)
restaurant1.customer_number()

iceCreamStand = IceCreamStand('ice cream stand', 'ice cream')
iceCreamStand.describe_restaurant()
flav = ['choco', 'kicki', 'vanila']
iceCreamStand.describe_flavors(flav[::-1])




