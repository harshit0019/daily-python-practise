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

#2 
def checkl():
    word = "am"
    with open("practise/practise.text", "r") as f:
        data = f.read()
        if word in data:
            print("found")
        else:
            print("not found")

def checkf():
    word = "am"
    data = True
    line_no = 1
    with open("practise/practise.text", "r") as f:
        while data:
            data = f.readline()
            if word in data:
                print(line_no)
                return  # Exits the function once the word is found
            line_no += 1
    return -1  # Only reached if the word is not found after reading the whole file

result = checkf()
print(result)  # To see the result of the function

