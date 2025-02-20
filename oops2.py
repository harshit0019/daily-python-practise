#1
class student:
    def __init__(self, name):
        self.name = name
s1 = student("ram")   
del s1
print(s1.name)   

#2
class car:
    @staticmethod
    def start():
        print("car started")
class toyata(car):
    def __init__(self,name):
        self.name = name
car1 = toyata("fortuner")
car2 = toyata("supra")

print(car1.start())
#3
class car:
    def __init__(self,type):
        self.type = type
    @staticmethod
    def start():
        print("car started")
class toyata(car):
    def __init__(self,name ,type):
        super().__init__(type)
        self.name = name
        super().start()
car1 = toyata("fortuner","ele")
print(car1.type)

#3
class person :
    name = "anamoyus"
    @classmethod
    def changeName(cls, name):
        cls.name = name 
p1 = person()
p1.changeName("ranul")
print(p1.name)
print(person.name)

#4

