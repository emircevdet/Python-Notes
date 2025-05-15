# ValueError
# age = int(input("Enter your age: "))
# print(age)

# ZeroDivisionError
# print(1 / 0)

def divide_numbers():
    try:
        num1 = int(input("Numerator: "))
        num2 = int(input("Denomirator: "))
        result = num1 / num2
    except ValueError:
        print("Invalid input! Please enter an integer.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    else:
        print(f"Result: {result}")
    finally:
        print("Execution completed.")

# divide_numbers()

def check_password(password):
    try:
        if len(password) < 6:
            raise ValueError("Password must be at least 6 characters long.")
        if not password.isdigit():
            raise ValueError("Password must include only numbers.")
    except ValueError as VE: # optional
        print(f"Error: {VE}")
    else:
        print("Password is valid.")
    finally:
        print("Function has been executed.")

# def check_password(password):
#     if len(password) < 6:
#         raise ValueError("Password must be at least 6 characters long.")
#     if not password.isdigit():
#         raise ValueError("Password must include only numbers.")
#     print("Password is valid.")

password = input("Enter password: ")
check_password(password) # also try in the new module

# import os
# getcwd / chdir    / listdir    / rename     / stat      / walk      
# mkdir  / makedirs / rmdir      / removedirs / remove    / path


# import time
# time   / ctime     / localtime / strftime  / sleep

# import datetime
# today  / weekday   / isoweekday
