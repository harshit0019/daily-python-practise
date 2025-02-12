#practise question 1

l = ["Harry", "Soham", "Sachin" ," Rahul " ]
for name in l:
   if(name.startswith( "S" ) ) :
     print(f"Hello  {name}")

#practise question 2 

n =  int(input("enter"))
for i in range(1, 11):
  print(f"{n} x {i} = {n*i}")

#practise question 3
n =  int(input("enter"))
i = 1 
while(i<11):
   print(f"{n} x {i} = {n*i}")
   i +=1
   
#4
n =  int(input("enter: "))
for i in range(2, n):
    if(n%i) == 0:
         print("not prime")
         break
else:
  print("prime")

#5
n= int(input(""))
p = 1
for i in range(1, n+1):
   p = p * i
print(p)

#6
n= int(input("enter: "))
for i in range(1,n+1):
  print(" "*(n-i),end="")
  print("*"*(2*i-1),end="")
  print("")

