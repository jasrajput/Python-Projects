class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def customer_number(self):
        print("Number of customer served: " + str(self.number_served))

    def set_number_served(self, number):
        if number > self.number_served:
            self.number_served = number
            print("Number of customer served: " + str(self.number_served))
        else:
            print("sorry, you cant change it")

    def describe_restaurant(self):
        print("Restaurant name is: " + self.restaurant + " and cuisine type is: " + self.cuisine_type)

    def open_restaurant(self):
        """Initiating a message that restaurant is open"""
        print(self.restaurant.title() + " Restaurant is open")

    def increment_customer(self, how_much):
        self.number_served = self.number_served + how_much
