class Spaces():
    def __init__(self, id, space_name, description, price, userID):
        self.id = id
        self.space_name = space_name
        self.description = description
        self.price = price
        self.userID = userID

    # This method allows our tests to assert that the objects it expects
    # are the objects we made based on the database records.
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # This method makes it look nicer when we print an Artist
    def __repr__(self):
        return f"Space({self.id}, {self.space_name}, {self.description}, {self.price}, {self.userID})"