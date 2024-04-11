class Player: 
    def __init__(self, User, Class):
        self.User = User
        self.Class = Class
    def __str__(self):
        return f"{self.User}, {self.Class}"
    
