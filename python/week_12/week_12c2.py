# class variables - instance variables

class member:
    # class variable, common for all in the class
    instance_rate = 1.05
    number_of_members = 0

    def __init__(self, name, salary):
        self.name = name # name-instance variable
        self.salary = salary # salary-instance variable
        # we haven't used "self" to update numbers in class, not in self
        member.number_of_members += 1
        # number_of_members += 1 # n = n + 1 error

member1 = member("Hakan", 50000)
member2 = member("Selin", 70000)

print(member1.name, member1.salary)
print(member2.__dict__)

print(member.instance_rate)
print(member1.instance_rate)
# the variable is first searched in the instance
# if not found, it is searched in the class
print(member.__dict__)
print(member1.__dict__)

# update class variable
member.instance_rate = 1.1 # affects all variables
print(member.instance_rate)
print(member1.instance_rate)
print(member2.instance_rate)

# update instance variable
member2.instance_rate = 1.2 # affects only the variable of member2
print(member.instance_rate)
print(member1.instance_rate)
print(member2.instance_rate)

print(member1.__dict__)
# as if instance_rate variable was created for member2
print(member2.__dict__)

print(member.number_of_members)
member3 = member("Berke", 80000)
print(member.number_of_members)