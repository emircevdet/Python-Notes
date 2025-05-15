# instance methods - class methods - static methods

# objects must be created to run an instance method
# instance methods take self parameter and are associated with the object

# there is no need to create any object to run class method
# class methods take cls parameter and are associated with the class

from datetime import date

class product:
    customs_code = "3924.90.00" # class variable
    total_stock = 0

    def __init__(self, id, name, exp_date=date.today().year+10):
        self.id = id # these are instance variables (left ones, not right ones)
        self.name = name
        self.exp_date = exp_date
        product.total_stock += 1

    def product_info(self): # instance method
        return f"Product ID: {self.id}, Product Name: {self.name}"
    
    @classmethod
    def total_stock_info(cls):
        return cls.total_stock
    
    @classmethod # mainly used as a constructor
    def edit_string(cls, str):
        id, name = str.split("-")
        return cls(id, name) # first edit, then create
    
    # free to input any parameter
    # does not take a parameter related to object or class
    @staticmethod
    def exp_date_info(any_product):
        return any_product.exp_date - date.today().year


product1 = product("101", "Scoops_Green", 2045)
product2 = product("102", "Scoops_Pink")
print(product1.id, product1.name)
print(product2.__dict__)
# error, name attribute (variable) does not belong to class
# but belongs to instance
# print(product.name)

print(product.customs_code)
print(product1.customs_code)
print(product.__dict__)
print(product1.__dict__)

print(product.total_stock)

print(product1.product_info())

print(product.total_stock_info())

product3 = product.edit_string("103-Scoops_Blue")
print(product.total_stock_info())
print(product3.id, product3.name)
print(product3.__dict__)

print(product.exp_date_info(product1))
print(product.exp_date_info(product2))

# DB Browser for SQLite
# Download latest version with installer: https://sqlitebrowser.org/dl/

