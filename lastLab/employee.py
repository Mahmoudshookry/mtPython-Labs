from person import Person
from car import Car


class Employee(Person):
    def __init__(self, name, money, mode, id, car, email, distanceToWork):
        super(Employee, self).__init__(name, money, mode)
        self.id = id
        self.car = car
        self.email = email
        self.__salary = 1000
        self.distanceToWork = distanceToWork

    def setSalary(self, val):
        if val >= 1000:
            self.__salary = val

    def getSalary(self):
        return self.__salary

    def work(self, hours):
        if hours == 8:
            self.mode = self.moods[0]
            print(self.mode)
        if hours > 8:
            self.mode = self.moods[1]
            print(self.mode)
        if hours < 8:
            self.mode = self.moods[2]
            print(self.mode)

    def drive(self, distance):
        self.car.run(self.car.velocity, distance)

    def refule(self, gasAmount=100):
        self.car.fuleRate += gasAmount

    def send_mail(self, to, subject, msg, receiver_name):
        print(to + " " + subject + " " + msg + " " + receiver_name)


