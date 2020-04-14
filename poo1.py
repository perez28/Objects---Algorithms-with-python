#clase name
"""
class Name :
    def __init__(self):
        self.firstname = "[no first name]"
        self.lastname = "[no lastname]"

#clase person
class Person :
    def __init__ (self) :
        self.name = Name() #este atributo llama una clase
        self.eyecolor = "[no eye color]"
        self.age = -1
#se crean instancias de la clase Person
myPerson1 = Person()
myPerson2 = Person()
print (myPerson1.eyecolor)
print (myPerson1.age)
print (myPerson1.name.firstname) #tener esto en cuenta
print (myPerson2.name.lastname) #tener esto en cuenta

#seteando el valor de la variable firstname 
myPerson1.name.firstname = "Johan"
myPerson2.name.firstname = "Yeison"
print (myPerson1.name.firstname)
print (myPerson2.name.firstname)
"""
#constructor Sin inicializar
"""
class Person :
    def __init__ (self,nombre,apellido) :
        self.firstname = nombre
        self.lastname = apellido
        self.eyecolor = "[no eye color]"
        self.age = -1
#se crean instancias de la clase Person
myPerson1 = Person("johna","jimenez")

print (myPerson1.firstname) 
print (myPerson1.lastname )
"""

#constructor con valores inicializados
"""
class Person :
    def __init__ (self,nombre = "[no name]",apellido = "[no apellido") :
        self.firstname = nombre
        self.lastname = apellido
        self.eyecolor = "[no eye color]"
        self.age = -1
#se crean instancias de la clase Person
myPerson1 = Person()
myPerson2 = Person(apellido='jimenez')
print (myPerson1.firstname) 
print (myPerson2.lastname )
"""
# getters and setters
class BankAccount:
    def __init__(self, name, balance = 0.0):
        self.log("Account created!")
        self.name = name
        self.balance = balance

    def getBalance(self):
        self.log("Balance checked at " + str(self.balance))
        return self.balance
    #aunque no esta explicitamente deposito es un setter, 
    #esto es ejemplo de que poner set no es necesario y no va con python
    def deposit(self, amount): 
        self.balance += amount
        self.log("+" + str(amount) + ": " + str(self.balance))

    def withdraw(self, amount):
        self.balance -= amount
        self.log("-" + str(amount) + ": " + str(self.balance))

    def log(self, message): 
        mylog = open ("log.txt" , "a")
        print (message,file = mylog) # escriba los datos (mensaje) dentro del archivo (mylog)
        mylog.close()
        
myBankAccount = BankAccount("David Joyner")
myBankAccount.deposit(20.0)
print(myBankAccount.getBalance())
myBankAccount.withdraw(10.0)
print(myBankAccount.getBalance())

