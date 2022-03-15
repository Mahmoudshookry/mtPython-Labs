from person import Person
from car import Car
from employee import Employee
from office import Office

c1 = Car("car1")
c1.set_fuelRate(80)
c1.set_velocity(50)

c2 = Car("car2")
c2.set_fuelRate(90)
c2.set_velocity(60)

c3 = Car("car3")
c3.set_fuelRate(100)
c3.set_velocity(70)

emp1 = Employee("hossam", 2000, "happy", 1, c1, "hossam@gmail.com", 10)
emp1.setSalary(2000)
print("before spending money the emp had : " ,emp1.money)
emp1.buy(6)
print("after spending: ", emp1.money)

print("befor eating 1 meals :",emp1.getHealth())
emp1.eat(1)
print("After eating the meals the health is :",emp1.getHealth())


emp1.send_mail("shokry@gmail.com","data","the message","shokry")






emp2 = Employee("mohamed", 2000, "happy", 1, c2, "mohamed@gmail.com", 10)
emp2.setSalary(3000)
emp3 = Employee("hasssan", 2000, "happy", 1, c3, "hasssan@gmail.com", 10)
emp2.setSalary(4000)

office1 = Office("Office",[emp1,emp2,emp3])

emp1.sleep(8)
emp2.work(8)
