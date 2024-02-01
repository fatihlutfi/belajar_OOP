# inheritance, extend, override, polymorphism
class Employee:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        
    def work (self):
        return f"{self.name} sedang bekerja"
    
class Programmer(Employee):
    def __init__(self, name, email, level):
        super().__init__(name, email)
        self.level = level
        
    def debug(self):
        return "debugging"
    
    def work(self):
        return f"{self.name} is writing code"
    
class UiDesigner(Employee):
    def __init__(self, name, email, level, tools):
        super().__init__(name, email)
        self.level = level
        self.tools = tools
        
    def work (self):
        return f"{self.name} is designing some new cool product"

employee = Employee("Fatih","Fatih@gmail")
programmer = Programmer("Lutfi", "lutfi@gmail", "junior")
ui_designer = UiDesigner("Andi", "bambang@fmail", "junior", "PS")

def working(system):
    print(system.work())
    
working(programmer)
        