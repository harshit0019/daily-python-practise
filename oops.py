#1
class student:
     name = "karan"
s1 = student()
print(s1.name)  

#2
class car:
    
        def __init__(self, fullname, price):
             self.name = fullname
             self.price = price
        def welcome(self):
             print("adding new car",self.name)
        def getmarks(self):
             return self.price
   
s1 = car("audi",23444)
#print(s1.name,s1.price)
s1.welcome()
print(s1.getmarks())
#s2 = car("royals roys",34444)
#print(s2.name,s2.price)

#3
