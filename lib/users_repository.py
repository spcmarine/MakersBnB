from lib.users import User

class UserRepository:
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        UserList = []
        user = self.connection.execute("SELECT * FROM users")
        for i in user:
            item = User(i['id'], i['username'], i['fullname'], i['password'])
            UserList.append(item)
        return UserList

    
    def create(self, user):
        self.connection.execute('INSERT INTO users (username, fullname, password) VALUES (%s, %s, %s)', [user.username, user.fullname, user.password])

    def delete(self, id):
        self.connection.execute(
            'DELETE FROM users WHERE id = %s', [id])
        
    