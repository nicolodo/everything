


class Employee:
    """Models an employee"""
    
    def __init__(self,fname,lname,salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def give_raise(self,salaryRaise=5000):
        print(f"I'm giving you a raise {self.fname} {self.lname}!")
        self.salary += salaryRaise
        print(f"Your new salary is {self.salary}")



# John = Employee("John", "Holmes", 25000)
# John.give_raise()
# John.give_raise(10000)



