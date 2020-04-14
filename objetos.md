# Objects & Algorithms (Objetos y Algoritmos)
---





## Que es un Objeto

Los objetos son tipos de datos de datos personalizados que se pueden crear.
estos tipos de datos son llamados **Clases**.
una de las mayores ventajas de la programación orientada a objetos es que podemos crear progrmas que imitan la forma como pensamos sobre las cosas en el mundo real.

### Clases
Las clases son MOLDES de donde salen los objetos,
podemos tener la clase persona, que tiene atributos como nombre, peso, color de pelo, color de ojos, numero de contacto, dirección de correo olectronico. 
* tambien se define como un clase del estructufa genérica para cierto tipo de datos.
* son la descripción general de los tipos de variables asociadas con ese tipo.

### Instancia tambien llamado Objeto

si seguimos hablando de personas, la instancia, es la creacion de un apersona, con cada uno de sus atributos definidos.


* llamada tambien istancia de clase es un ejemplo particular de un objeto de ese tipo.
  * nombre = jona
  * peso = 20
  * color de pelo = negro
  * color de ojos = cafes

* *jona es una instancia de un objeto tipo persona*
* jona es un ejemplo de una instancia de una persona.

Asi es como se declara una clase en python:

```python
#clase name
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

```

*  los funciones declaradas dentro de una clase son llamados métodos como: `def __init__ (self)`

* hay un metodo especial que tienen la siguiente estructura ` def __init__ (self)`, mas adelante se hablará mas especificamente de el, pero si se puede decir que este método es llamado cuando creamos por primera vez una nueva instancia de clase.

*  es imortarte que los atributos tengan nombres por defecto: `self.Lastname = "[no Last name ]"`

* `self` le dice a python que defina dichas varialbes para su conjunto. es como para estar seguros que al  llamar a una varible dentro de una clase estemos seguros que es esa misma clase en realidad. un poco enrredado pero se aclarará con mas practica.

* la variable declarada con `self` existe mientras exista la clase o la instancia de la clase
* Cada método definido dentro de una clase
debe tener self como primer parámetro.

### Metodos y Encapsulación
La encapsulacón: es la capacidad de combinar variables y métodos en definiciones de clase en programación orientada a objetos. Ayuda a evitar la modificación o el mal uso de los datos por otras funciones o programas.

Metodo:Un método es una función definida dentro de una clase.

* Los métodos son los que hacen la encapsulación
verdaderamente poderoso en las clases.
* Tiene las mismas características: un nombre,
una lista de parámetros, algo de código y, opcionalmente,una declaración de devolución.

Alcance de un metodo:se define como el alcance normal de una función para ese idioma más cualquier variable que son visibles en la instancia de la clase en su conjunto. `confuso`.



### Metodos comunes en python

#### Metodo constructor
Un constructor contiene código que
ejecutar cada vez que se crea una nueva instancia de esa clase.
* Es como un método de configuración.
* Por ejemplo, si una clase tiene una lista,
la lista probablemente necesita ser inicializada
antes de que realmente pueda usarse.
Esto se hace en el constructor porque garantiza que es realizado antes de que sea necesario.

un ejemplo de esto es si tenemos una clase  llamada cuenta bancaria, normalmente de supondría que cada banco recién creado La cuenta no tiene saldo. (inicialmente la cuenta no tiene saldo por defecto = constructor).

`def __init__ (parametros del constructor) :`

```python
class Person :
    def __init__ (self,nombre,apellido) :
        self.firstname = nombre #usar los argumentos
        self.lastname = apellido
        self.eyecolor = "[no eye color]"
        self.age = -1
```
En el codigo anterior, si al declara una instancia no ponemos los argumetnos, el programa se detendra, es por esto que se recomiento poner valores por defecto en el constructor. Asi:
`def __init__ (self,nombre = "[no name]",apellido = "[no apellido") :`
```python
#constructor con valores inicializados
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
#[no name]
print (myPerson2.lastname )
#jimenez
```


#### Metodo Destructor
Este es un metodo que elimina la instancia. son normalmente aplicables cuando se manejan grandes contidades de datos, pala liberar memoria en la computadora.
un tipo de método común en las clases de escritura que especifica cómo se destruirá la instancia de una clase, como liberar su memoria a la computadora.


### Metodos Getters y Setters

Getters y setters son estructuras de métodos simples. que permiten que el código interactúe con una variable dentro de una instancia.

#### Getters

Un Getter simplemente devuelve el valor de una determinada variable.Se usan comúnmente para permitir que ocurra otro procesamiento cada vez que se accede a la variable, como el registro.


#### Setters


Un tipo común de método en clases de escritura que establece una variable contenida dentro de la clase en un nuevo valor. Se usan comúnmente
para permitir que ocurra otro procesamiento cada vez que se cambia la variable, como el registro.


#### Por que hacer esto, cambiar variables por medio de estos metodos?.

¿No podemos acceder directamente a esas variables directamente?
Muchas veces, es mejor diseñar nuestro código de manera que las variables dentro no pueden modificarse directamente.
Por ejemplo, imagine nuevamente que estamos escribiendo una clase para representar una cuenta bancaria.

Imagina que esta clase va a ser
Accedido por diferentes bancos y diferentes clientes. No queremos que todos solo sean
capaz de cambiar el valor del saldo a voluntad.
Solo deberían poder cambiarlo de ciertas maneras,
como procesar una transacción.Métodos como getters y setters permiten dictamos las reglas bajo las cuales las variables de clase pueden
ser accedido y cambiado.

Tenga en cuenta que en Python, en realidad, es relativamente raro usar getters y setters. Si bien estos son obligatorios o altamente recomendados en algunos lenguajes (como Java), en realidad a menudo se desaconseja en Python para mantener el enfoque "Pythonic" de mantener un fácil acceso a las variables y los datos. A menos que realmente vaya a utilizar una de las ventajas asociadas con getters y setters, puede ser mejor omitir su uso.

Aún así, es importante saber cómo funcionan cuando los encuentra, y conocer sus ventajas para saber cuándo usarlos.

Ejemplo getters y setterts

```python
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
#20.0
myBankAccount.withdraw(10.0)
#10.0
print(myBankAccount.getBalance())
```
