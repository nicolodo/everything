
# ex 3 Users

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


brian = User('brian','password','cat','delete sys32')
brian.greetUser()
brian.describeUser()
brian.loginAttempts += 10
print(f"{brian.name} has tried to login {brian.loginAttempts} times")
brian.resetLoginAttempts()
print(f"{brian.name} has tried to login {brian.loginAttempts} times")