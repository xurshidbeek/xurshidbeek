
class Employee:
    def __init__(self, name, birth_date):
        self.__name = name
        self.__birth_date = birth_date

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,new_name):
        #try:
            if len(new_name) > len(self.__name) :
                raise NameError("Ism juda uzun eskisiga qaraganda")
            self.__name = new_name
        #except NameError:
            #print("Ism uzun emas")


foydalanuvchi = Employee("xurwid,","12.02.20221")
print(foydalanuvchi.name)
foydalanuvchi.name = "loy"
print(foydalanuvchi.name)
        