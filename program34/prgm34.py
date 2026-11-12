class bank:
    def __init__(self,acc_no,name,type,bal):
        (self.acc_no)=acc_no
        (self.name)=name
        (self.type)=type
        (self.bal)=bal
    def deposit(self,amt):
        if amt<=0:
            print("it should be an postive number")
        else:
            self.bal+=amt
            print("your current balence is ",self.bal)
    def withdraw(self,amt):
        if amt<=0:
            print("it should be an postive number")
        elif amt > self.bal:
            print("insufficient balance")
        else:
           self.bal-=amt
           print("your current balence is ",self.bal)
    def display(self):
        print(f"account number:{self.acc_no}")
        print(f"account holder:{self.name}")
        print(f"account type:{self.type}")
        print(f"Current balance:{self.bal}")

no=int(input("enter your account number:"))
name=input("enter your name:")
type=input("enter your account type")
bal=int(input("enter your balance"))
usr1=bank(no,name,type,bal)
while True:
   print("\n1)DEPOSIT\n2)WITHDRAWAL\n3)ACCOUNT INFORMATION\n4)EXIT\n")
   opt=int(input("Enter your option:"))
   if opt == 1:
      amt=int(input("enter your amount:"))
      usr1.deposit(amt)
   elif opt == 2:
      amt=int(input("enter your withdrwawal amount"))
      usr1.withdraw(amt)
   elif opt == 3:
      usr1.display()
   elif opt == 4:
      exit(0)
   else:
      print("invalid option")
