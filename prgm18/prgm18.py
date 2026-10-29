a=int(input("Type the first number:"))
b=int(input("Type the second number:"))
while b !=0:
    r= a % b
    a=b
    b=r
print("the GCD of the numbers is",a)