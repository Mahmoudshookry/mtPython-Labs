class Office:
    employeesNum = 20
    def __init__(self, name, employees):
        self.name = name
        self.employees = employees

    def get_all_employess(self):
        return self.employees

    def get_employee(self, empId):
        lenthOfEmp = len(self.employees)
        for i in range(lenthOfEmp):
            if self.employees[i].id == empId:
                return self.employees[i]

    def hire(self, Employee):
        newEmployee = Employee(Employee)
        self.employees.append(newEmployee)

    def fire(self, empId):
        lenthOfEmp = len(self.employees)
        for i in range(lenthOfEmp):
            if self.employees[i].id == empId:
                del self.employees[i]
                return

    @staticmethod
    def calculate_lateness(targetHour , moveHour, distance, velocity):
        travellingTime = velocity / distance
        if moveHour + travellingTime > targetHour:
            return False
        else:
            return True

    def check_lateness (self, empId, moveHour):
        emp = self.get_employee(empId)
        distance = emp.distanceToWork
        vel = emp.car.velocity
        if Office.calculate_lateness(9, moveHour, distance, vel) == True:
            emp.money += 10
        else:
            emp.money -= 10

    def deduct(self, empId, deduction):
        lenthOfEmp = len(self.employees)
        for i in range(lenthOfEmp):
            if self.employees[i].id == empId:
                self.employees[i].money -= deduction
                return

    def reward(self, empId, reward):
        lenthOfEmp = len(self.employees)
        for i in range(lenthOfEmp):
            if self.employees[i].id == empId:
                self.employees[i].money -= reward
                return

    @classmethod
    def change_emps_num(num):
        employeesNum = num