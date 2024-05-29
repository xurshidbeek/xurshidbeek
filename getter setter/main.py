# getter and setter

class User:
    def __init__(self, first_name: str, last_name: str, username: str, password: str, age: int, total_balance: float):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.__password = password
        self.__age = age
        self.__total_balance = total_balance

    def full_name(self):
        return f"{self.first_name} {self.last_name}"



    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_data):
        try:
            if new_data < 18:
                raise ValueError("Kechirasiz, foynalanuvchi yoshi 18 dan kichik bo'lishi mumkin emas")
            self.__age = new_data
        except ValueError:
            print("Kechirasiz, foynalanuvchi yoshi 18 dan kichik bo'lishi mumkin emas")

# @property
# def password(self):
#     return self.__paswword
# @password.setter
# def password(self,new_pas):

#          if len(new_pas) > 8 :
#            ValueError("password too long")
#          self.__paswword = new_pas

    def get_total_balance(self):
        return self.__total_balance

    def full_info(self):
        return f"""
            First Name: {self.first_name}
            Last Name: {self.last_name}
            Username: {self.username}
            Age: {self.age}
            Total Balance: {self.get_total_balance()}
        """


foydalanuvchi = User("John", "Smith", "john123", "1234", 29, 150000.59)
print(foydalanuvchi.age)
foydalanuvchi.age = 25
print(foydalanuvchi.age)
