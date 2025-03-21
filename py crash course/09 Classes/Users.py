# ex 3,5,7 Users

class User:
    """Simulates a User on a computer"""
    def __init__(self,name,password,wallpaper,*permissions):
        # user setup[
        permissions = list(permissions)
        defaultpermissions = [
            'change wallpaper',
            'change password',
            'play music']
        self.name = name
        self.password = password
        self.wallpaper = wallpaper
        self.permissions = defaultpermissions + permissions
        self.loginAttempts = 0

    def incLoginAttempts(self,increment):
        self.loginAttempts += increment

    def resetLoginAttempts(self):
        self.loginAttempts = 0

    def greetUser(self):
        print(f"Hello there {self.name}!")

    def describeUser(self):
        print(f"{self.name}'s password is {self.password}")
        print(f"their desktop wallpaper is a {self.wallpaper}")        
        print(f"and they have permission to:")

        if self.permissions:
            for permission in self.permissions:
                print(f"\t{permission}")

class privileges:
    """Admin privileges"""
    def __init__(self):
        # Admin privileges
        self.privileges = [
            'add/remove users',
            'add/rm permissions',
            'change user passwords',
            'change user wallpapers',
            'install packages'
        ]
        
    def showPrivileges(self):
        print("Admin user has the following privileges")
        for privelege in self.privileges:
            print(f"\t-{privelege}")

class Admin(User):
    """Simulation of a computer adminstrator"""
    def __init__(self, name, password):
        # import user attributes and functions
        super().__init__(name,password,"Tux Penguin","All")
        self.privileges = privileges()

John = Admin('John','password')
John.privileges.showPrivileges()