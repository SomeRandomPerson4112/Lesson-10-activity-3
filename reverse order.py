number=int(input("Enter your number: "))
print("Numbers from {0} to {1} are: ".format(number,1))
for i in range(number,0,-1):
    print(i)

for j in range(1,number+1,2):
    print(j)