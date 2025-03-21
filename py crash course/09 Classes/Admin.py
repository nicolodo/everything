
import User

class privileges(User.User):
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

class Admin(User.User):
    """Simulation of a computer adminstrator"""
    def __init__(self, name, password):
        # import user attributes and functions
        super().__init__(name,password,"Tux Penguin","All")
        self.privileges = privileges()