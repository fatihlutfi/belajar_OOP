class User:
    total = 0
    def __init__(self, name, email,role):
        self.name = name
        self.email = email
        self.__role = role
        User.total +=1
        
    def info(self):
        return f"{self.name} -{self.email} - {self.__role}"  
    
    @property
    def role(self):
        return self.__role
    
    @role.setter
    def role(self, new_role):
        if self.__role != "user":
            self.__role = new_role

    @classmethod
    def setTotal(cls, total):
       cls.total = total 
       
    @classmethod
    def from_string(cls, string_params):
        name, email, role = string_params.split("-")
        return cls(name, email, role)
            

fatih = User("Fatih","fatih@","admin")
new_var = "fatih - fatih@g - admin"

fatih_dua = User.from_string(new_var)

print(fatih_dua.info())
# print(fatih.info())
# fatih.role = "super admin"
# print(fatih.info())