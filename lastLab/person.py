class Person:
    moods = ("happy", "tired", "lazy")

    def __init__(self, name, money, mode):
        self.name = name
        self.money = money
        self.mode = mode
        self.__health = 100

    @classmethod
    def getMood(self):
        return self.moods[1]

    def setHealth(self, val):
        if val >= 0 and val <= 100:
            self.__health = val

    def getHealth(self):
        return self.__health

    def sleep(self, hours):
        if hours == 7:
            self.mode = self.moods[0]
            print(self.mode)
        elif hours < 7:
            self.mode = self.moods[1]
            print(self.mode)
        elif hours > 7:
            self.mode = self.moods[2]
            print(self.mode)

    def eat(self, meals):
        if meals == 3:
            self.health = 100
            print(str(self.health))
        elif meals == 2:
            self.health = 75
            print(str(self.health))
        elif meals == 1:
            self.health = 50
            print(str(self.health))

    def buy(self, items):
        for i in range(items):
            self.money -= 10


