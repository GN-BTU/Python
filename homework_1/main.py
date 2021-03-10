'''
დავალება - https://classroom.btu.edu.ge/uploads/14/14612.pdf
'''

class Calculator:
    @staticmethod
    def add(num_1, num_2):
        return num_1 + num_2

    @staticmethod
    def subtract(num_1, num_2):
        return num_1 - num_2

    @staticmethod
    def divide(num_1, num_2):
        return num_1 / num_2

    @staticmethod
    def multiply(num_1, num_2):
        return num_1 * num_2


print(Calculator.add(1, 2), Calculator.subtract(5, 3))


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return Calculator.multiply(self.width, self.height)

    def perimeter(self):
        return Calculator.multiply(2, Calculator.add(self.width, self.height))

    def print_info(self):
        print(
            f'მართკუთხედის სიგანეა {self.width}, სიგრძე {self.height},ფართობი {self.area()}, პერიმეტრი {self.perimeter()}')


class Employee:
    def __init__(self, name, surname, age, salary):
        self.name, self.surname, self.age, self.salary = name, surname, age, salary

    def info(self):
        return f'სახელი {self.name}, გვარი {self.surname}, ასაკი {self.age}, ხელფასი {self.salary}'


employees = []

with open("dataset1.csv", "r") as dataset:
    data = [line.split(",") for line in dataset.read().split("\n")][1:-1]
    employees = [Employee(name, surname, age, salary) for [name, surname, age, salary] in data]

print(f'თანამშრომელი ყველაზე დაბალი ხელფასით - {min(employees, key=lambda employee: employee.salary).info()}')
print(f'თანამშრომელი ყველაზე მაღალი ასაკით - {max(employees, key=lambda employee: employee.age).info()}')

