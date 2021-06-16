#class declaration
class User:
    def __init__(self , user_id,user_name):
        self.id = user_id
        self.name=user_name



user_1 = User(1,"Walid")

print(user_1.name)
