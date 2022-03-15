class Car:
    def __init__(self, name):
        self.name = name
        self.__fuleRate = 100
        self.__velocity = 100

    def set_fuelRate(self, val):
        if val >= 0 and val <= 100:
            self.__fuleRate = val

    def set_velocity(self, val):
        if val >= 0 and val <= 200:
            self.__velocity = val

    def get_fuelRate(self):
        return self.__fuleRate

    def get_velocity(self):
        return self.__velocity

    def run(self, velocity, distance):
        self.velocity = velocity
        while (distance > 0 and self.__fuleRate > 0):
            distance -= 1
            self.fuleRate = self.fuleRate * 0.99
        remainDistance = distance
        self.stop(remainDistance)

    def stop(self, remainDistance):
        self.velocity = 0
        if remainDistance > 0:
            print("Fuel Tank in empty, remained distance = " + str(remainDistance))
        else:
            print("You have arrived the distenation")
