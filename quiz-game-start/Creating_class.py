class User :
    #DECLEARING ATTRIBUTES
    def __init__(self,user_id,username):
        self.id=user_id
        self.name=username

#INTIALIZING ATTRIBUTES
user_1=User("001","harish")
user_2=User("002","tej")
print(f"{user_1.name},{user_1.id}")
print(f"{user_2.name},{user_2.id}")