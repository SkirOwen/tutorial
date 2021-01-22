class Car:
    def __init__(self, model, colour, kpl, tank_level):
        self.model = model
        self.colour = colour
        self.kpl = kpl
        self.tank_level = tank_level

    def travel(self, distance):
        travel_range = self.tank_level * self.kpl
        if travel_range < distance:
            print("You will need more fuel")
            print("Refill first")
        else:
            used_fuel = distance / self.kpl
            left_fuel = self.tank_level - used_fuel
            print("You will use ", used_fuel)
            print("You have ", left_fuel, "left")
            return self

    def refuel(self, amount):
        self.tank_level += amount
        return self
