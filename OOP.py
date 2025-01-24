class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species

    def speak(self):
            return f"{self.name} makes noise."

dog=Animal("Tom","Dog")
cat=Animal("Whiskers","Cat")

print(dog.name)
print(cat.speak())

#Encapsulation
class bank_account:
    def __init__(self,account_holder,balance):
         self.account_holder=account_holder
         self.__balance=balance #private variable

    def deposit(self,amount):
        self.__balance +=amount

    def get_balance(self):
        return self.__balance

account=bank_account("Duke",10000)
account.deposit(5000)
print(account.get_balance())  
print(f"The holder of this account is {account.account_holder}")     

#practice exercise 1
class Vehicle:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        
    def start_engine(self):
        return "I started the engine"
        
class Car(Vehicle):
    def start_engine(self):
        return f" {self.model} started  engine"
class MotorCylce(Vehicle):
    def start_engine(self):
        return f" {self.model} started  engine"
        
car1= Car("Toyota", "Hilux",2017)
car2= Car("Mazda","Atenza",2018)

car3=MotorCylce("Boxer", "motobiker", 2023)

print(car2.start_engine())
print(car3.start_engine())

#Bank Account
class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.__balance=balance  #This is a private variable
        
    def deposit(self,amount):
        if self.__balance <0:
            return "Amount not allowed"
        else:
            self.__balance+=amount
            return f"{self.account_holder} deposited successifuly"
            
    def withdraw(self,amount):
        self.amount= amount
        if self.__balance <amount:
            return"Insufficient funds!"
        else:
            return f" {self.account_holder} has completed withdrawal of {self.amount} successful!"
        self.__balance-=amount        
            
    def get_balance(self):
        return self.__balance
        
account1=BankAccount("Duke Mochama", 1000)

print(account1.deposit(5000))
print(account1.withdraw(4500))
print(account1.get_balance())

