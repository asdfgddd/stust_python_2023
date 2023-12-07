class Sport:
    def __init__(self, name):
        self.name = name

class LandSport(Sport):
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type

class WaterSport(Sport):
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type

# Create instances of LandSport
basketball = LandSport("Basketball", "Ball Game")
athletics = LandSport("Athletics", "Non-Ball Game")

# Create instances of WaterSport
swimming = WaterSport("Swimming", "Swimming")
sailing = WaterSport("Sailing", "Sea")

print(basketball.name, basketball.type)
print(athletics.name, athletics.type)
print(swimming.name, swimming.type)
print(sailing.name, sailing.type)
