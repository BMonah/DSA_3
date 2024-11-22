# Classes allow us to logically group our data functions and data in a way
# that is easy to reuse and easy to build upon
# Data and functions associated with classes are referred to as attributes and methods
# A class is a blueprint for creating instances
# Each unique employee that we create in the class are called Employee instances
class Employee:

    raise_amount = 1.5

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        return self.pay


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Bonny', 'Monah', 60000)


print(emp_1)
print(emp_2)
print(emp_1.fullname())
print(emp_1.apply_raise())
print(Employee.apply_raise(emp_2))
# print(Employee.pay(emp_1))

print('{} {}'.format(emp_2.first, emp_2.last))

print(emp_1.email)
print(emp_2.email)
