#1
age = int(input("n:"))
vote = ("yes","no")[age < 18]
print(vote)

#2
  def sum(a, b):
    sum = a + b
    print(sum)

sum(1 , 2)

#3
hero = ["thor" ,"ironman" ,"hulk"]
def print_len(list):
    print(len(list))
def printl(list):
    for item in list:
        print(item, end=" ")
printl(hero)
