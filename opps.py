class BankAccount:
    def __init__(self, name, userId, password, pin):
        self.name = name
        self.userId = userId
        self.password = password
        self.pin = pin
    
class Bank:
    def __init__(self,name,pin,id,password,balance):
        self.name = name
        self.pin = pin
        self.id = id
        self.password = password
        self.balance = balance
    def showBal(self):
            print(self.balance)
            
    def addBal(self,am):
         print(f"Amount Was {self.balance} and added {am} = {self.balance + am}")
         self.balance += am
         
    def withD(self,am):
         print(f"Amount Was {self.balance} and Deducted {am} = {self.balance - am}")
         self.balance -= am
         
    def trasfer(self,acc,am):
         print(f"Your Amount Was {self.balance} and Transferred {am} = {self.balance - am}")
         self.balance -= am
         print(f"{acc.name} Amount Was {acc.balance} and Recieved {am} = {acc.balance + am}")
         acc.balance += am
         
         
data ={}
while True:
     selected = None
     print("----Login Now-----")
     inp = input("Enter Your Name : ")
     if inp in data:
       print(f'Welcome {inp}')
       n_in = input("press 0 for check history\npress 1 for transfer\npress 2 for deposit\npress 3 for withdraw: " )
       selected = data[inp]
       selected.showBal()
       if(n_in == '0'):selected.showBal()
       
       elif(n_in == '2'):
           am = int(input("Enter Amount to add : "))
           selected.addBal(am)
           
       elif(n_in == '3'):
           am = int(input("Enter Amount to Withdraw : "))
           selected.withD(am)
           
       elif (n_in == '1'):
           am = int(input("Enter Amount to Transfer : "))
           acc = input("Enter Account Name to Transfer : ")
           if acc in data:
               selected.trasfer(data[acc],am)
           else:
               print("Account Not Found")
     else:
        print(f"Not found , adding {inp} as a new person")
        bal = int(input("enter Opening Balance : "))
        pin = int(input("enter Pin : "))
        id = input("enter Id : ")
        passw = input("enter Password : ")
        data[inp]=Bank(inp,pin, id, passw, bal,)





