# superclass
class employee():
    rate = 1.1
    def __init__(self, f_name, l_name, salary):
        self.f_name = f_name
        self.l_name = l_name
        self.salary = salary
        self.mail = f_name.lower() + "." + l_name.lower() + "@example.com"

    def show_info(self):
        return f"Name: {self.f_name} - Surname: {self.l_name} - Salary: {self.salary} - Mail: {self.mail}"

employee1 = employee("EMP1_first", "EMP1_last", 40000)
employee2 = employee("EMP2_first", "EMP2_last", 80000)

print(employee1.__dict__)
print(employee1.mail)

# subclass
class software_developer(employee):
    # pass
    def __init__(self, f_name, l_name, salary, p_language):
        # self.f_name = f_name
        # self.l_name = l_name
        # self.salary = salary
        # self.mail = f_name.lower() + "." + l_name.lower() + "@example.com"
        # self.p_language = p_language
        super().__init__(f_name, l_name, salary)
        self.p_language = p_language
        
    rate = 1.2
    def show_info(self):
        # return "I'm a software developer."
        return f"Name: {self.f_name} - Surname: {self.l_name} - Salary: {self.salary} - Mail: {self.mail} - Language: {self.p_language}"

    def return_language(self):
        return f"Programming Language: {self.p_language}"

developer1 = software_developer("DEV1_first", "DEV1_last", 90000, "Python")
developer2 = software_developer("DEV2_first", "DEV2_last", 110000, "Java")

print(developer1.mail)

print(employee1.rate)
print(developer1.rate)

print(employee1.show_info())
print(developer1.show_info())

print(developer1.return_language())

# subclass
class manager(employee):

    def __init__(self, f_name, l_name, salary, employees = None):
        super().__init__(f_name, l_name, salary)
    
        if employees == None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def show_employees(self):
        for emp in self.employees:
            print(emp.show_info())

manager1 = manager("MAN1_first", "MAN1_last", 150000)
print(manager1.__dict__)

manager1.add_employee(employee1)
manager1.add_employee(developer1)
manager1.show_employees()
print("*"*30)
manager1.remove_employee(employee1)
manager1.show_employees()
print("*"*30)
manager2 = manager("MAN2_first", "MAN2_last", 120000, [employee2, developer2])
manager2.show_employees()

# isinstance() / issubclass()
print(isinstance(employee1, employee))
print(isinstance(developer1, employee))
print(isinstance(manager1, employee))
print(isinstance(manager1, software_developer))
print("*"*30)
print(issubclass(software_developer, employee))
print(issubclass(software_developer, manager))
