class User:
    def __init__(self, id, username, fullname, password):
        self.id = id
        self.username = username
        self.fullname = fullname
        self.password = password
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"User({self.id}, {self.username}, {self.fullname}, {self.password})"