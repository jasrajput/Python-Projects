class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def detail(self):
        print("This car has " + str(self.odometer) + " mileage on it")
        return "Make in: " + str(self.make), "Model: " + str(self.model), "Year " + str(self.year)

    def update_odometer(self, mileage):
        """Print a statement showing the car's mileage"""
        if mileage > self.odometer:
            self.odometer = mileage
            return self.odometer
        else:
            return "you can't rolled back an odometer"

    def increment_odometer(self, mileage):
        print("Incremented by: " + str(mileage))
        self.odometer += mileage
        return self.odometer


class Battery:
    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
        self._range = 0

    def describe_battery(self):
        print("This car has battery size of " + str(self.battery_size) + " KWh")

    def get_range(self):
        if self.battery_size == 70:
            self._range = 240
        elif self.battery_size == 85:
            self._range = 270

        message = 'This car can go approx. ' + str(self._range)
        message += " miles on a full charge"
        print(message)

    def upgrade_battery(self):
        if self.battery_size:
            self.battery_size = 85


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
