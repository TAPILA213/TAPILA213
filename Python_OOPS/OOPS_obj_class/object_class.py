class A:
    "Class is plan/bule print . it contais the properties and methods of physical existance of obj"
print(A.__doc__) # it will document of class
obj = A()

# Types of variables
"""
1.instance variables
2.Static Varibles
3.Local Varibles    """

# Types of methods
"""
1. instance method 
2.class method
3.static method
"""


class office:
    def __init__(self):
        self.emp_name = "Pavan"
        self.emp_id = "SIM001"
        self.manager ="subhashini"
    def performance(self):
        print("hell0",self.emp_name)
        print("my emp_id",self.emp_id)
        print("my manger",self.manager)
of1 = office()
"By using this reference varible we can Acesse the varibles & methods in the class"
print(of1.emp_name)
print(of1.emp_id)
print(of1.manager)
of1.performance()







