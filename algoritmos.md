# Algoritmos: 

## Definición
Técnicamente, una colección de pasos que transforma la entrada en salida; comúnmente, un conjunto complejo de muchos pasos que solo es factible realizar con la eficiencia de una computadora.

## Complejidad de los algoritmos
la velocidad a la que el número de operaciones requiere ejecutar un algoritmo crece en función del valor de la entrada en la que opera.
se habla de la eficiencia del algoritmo
Imagina que tienes una lista de 500 estudiantes en tu escuela.
Tu objetivo es encontrar a David Joiner en esa lista.
¿Cuánto tiempo se tarda?
Midamos el tiempo en términos de número de comparaciones.
hay diferentes formas de hacer esta busqueda, si la lista esta ordenada, sera mas facil hacer esta busqueda, pero si no  lo esta tardaria mucho mas.

## Notación Big O (Medida de complejidad de los algoritmos)
¿Cuántas operaciones se requieren para completar este algoritmo?
 una notación para expresar la peor eficiencia de un algoritmo en términos del tamaño de la entrada.

También existe la notación Big Ω (Omega) , que expresa la eficiencia del mejor caso de un algoritmo, y la notación Big θ ( Theta), que expresa la eficiencia del caso típico de un algoritmo. Big O se usa con mayor frecuencia.

Sin embargo, estos diversos valores existen porque algunos algoritmos son generalmente muy eficientes, pero son muy ineficientes con ciertos tipos de datos. Por ejemplo, existe un algoritmo de clasificación llamado QuickSort que generalmente es extremadamente eficiente, pero cuya eficiencia se desploma si hay muchos valores duplicados en el conjunto de datos que está clasificando.
un video que nos puede sacar de la duda pra entende esto mejor es el que  se expresa [Aquí](https://www.youtube.com/watch?v=HEISXs0wYlM&t=3s)

[Este](https://www.youtube.com/watch?v=HdZbPqYKafU) es otro video que explica muy bien como calcular y de donde sale el bigO.

una clave para entender el crecimietento de calda valor bigO es repasar las funciones que se ven en el  cuadro, funcion lineal, cuadratica, logaritmica,etc. y ver como crecen

un complemento al video anterior es [Este otro](https://www.youtube.com/watch?v=Sibd8jSTdUQ),  explica paso a paso como llenar el BigO (de donde e toman sus insumos  directamente desde el codigo)

un video aun mas claro es [Esta lista de reproducción](https://www.youtube.com/watch?v=vEbgtkA4Ums)

en la siguiete imagen podemos ver los tipos de notaciones BigO






 

![BigO](/imagenes/Big%20O.png)



### Recursión  o Recursividad
Esto sucede cuando una función se llama a sí misma.un método de programación caracterizado por funciones que, durante su operación, llaman copias adicionales de sí mismos; ver también, recursión. La recursión implica dividir un problema en instancias más pequeñas de forma recursiva hasta que cada una de ellas pueda resolverse de forma independiente. Las soluciones a estas instancias más pequeñas se combinan para formar la solución para el problema original.(Esta definición es de la academia)
no es eficiente usar recursividad, gasta mucha memoria, pero se usa cuando con ciclos for se torna muy complicado

### Recursión simple (ejercicio de factorial)
el siguiente es un ejemplo de recursividad, en el codigo se ve muy faciel de entender, pero realmente es un poco mas complicado de lo que parece.

en [Este](https://www.youtube.com/watch?v=vjjw8Xp8rII)  y en [Este](https://www.youtube.com/watch?time_continue=822&v=cIRzX8gEOf4) otro Link se encuentran unos videos en los cuales se encuentran una explicación muy clara de la recursión.
temas claves para entender la recursividad
call stack, cada llamada a una funcion se almacena en la pila, esto tiende a confundir un poco.

Ejemplo Factorial:

```python
def Factorial (n) :
    
    if n >1 :  
       return n * Factorial(n-1)        
    
    else :
        return 1
   
print(Factorial (4))
```
mas ejemplos:
conteo regresivo recursivo
```python
def conteo_regresivo (num) :
    if nun <= 0:
        print (num)
    else:
        print(num)
        conteo_regresivo (num-1)
conteo_regresivo(5)
```
conteo regresivo no  recursivo
```python
def conteo_regresivo (num) :
    for numero in sorted(range(num + 1),reverse=True)
    print (numero)
```
Fibonacci Recursivo:
```python
  #fibonacci Recursivo
def fib(n):    
    if n == 1 or n == 2:
        return 1   
    else:
        return fib(n - 1) + fib(n - 2)  

print("fib(5) is", fib(5))
print("fib(10) is", fib(10))
```
Fibonacci No recursivo
```python
def fibonaci (num) :
    result = [0,1]
    conta = 0
    for salto in range(num +1) :
              
        if conta >=2:            
            result.append(result[conta-1] + result[conta-2]) 
        
        conta =conta +1
        
    return result[num]
            
    
fibo = input ('Igrese el numero de suceciones de fibonacci que desea calcular: ')  
print(fibonaci(abs(int(float(fibo)))))  

```

### Algoritmos de clasificación
Algoritmos que toman como entrada una lista y producen como salida una versión ordenada de esa lista. Los ejemplos incluyen clasificación de burbujas, clasificación de inserción, clasificación de selección, clasificación de fusión, clasificación de shell, clasificación rápida y clasificación de montón.

### Burbuja

```python
def sort_with_bubbles(lst):    
    swap_occurred = True    
    while swap_occurred:        
        swap_occurred = False      
        
        for i in range(len(lst) - 1):            
            if lst[i] > lst[i + 1]:
                
                temp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = temp
                print (lst)
                swap_occurred = True
    return lst
print(sort_with_bubbles([34, 16, 2, 78, 4, 6, 1]))
```

### Insertion sort
En el siguiente [video](https://www.youtube.com/watch?v=ROalU379l3U) se explica la dinamica del de este algoritmo. el siguiente codigo materializa lo que se ve en el video, puede ser mejorado reduciendo las lineas de codigo con funciones propias de python como `insert()`, y `del`

```python
def inser (lista) :
    pibo =0
    for i in range(len(lista)-1) :
        if lista [i] > lista [i +1] :
            pibo = lista [i +1]
            lista [i +1] = lista [i ]
            lista[i] = pibo
            
            
        count = i
        while lista [count] < lista [count -1 ] and count >0 :
            
            pibo = lista [count]
            lista [count] = lista [count - 1]
            lista[count -1 ] = pibo
            count = count -1
            
        print (lista)     
        
numero =list(range (1000,1,-1))
numero2 = [3,2,4,5,1]
print ('insersion', list(numero))
inser(numero) 
```

El siguiente es la solución de la guia del curso.
en cada iteración del bucle exterior el bucle mas interno se encarga de buscar el indice que contenga el valor mas pequeño y lo para al indice i.
```python
def sort_with_select(a_list):
    
    for i in range(len(a_list)):
        
        minIndex = i

        for j in range(i + 1, len(a_list)):
                     
            if a_list[j] < a_list[minIndex]:
            minIndex = j

        minValue = a_list[minIndex]
        
        del a_list[minIndex]
        
        a_list.insert(i, minValue)
        print (a_list)
    
    return a_list
	


print(sort_with_select([5, 3, 1, 2, 4]))

```
### Merge Sort
Debo decir que me costo bastante entenderlo como trabaja completamente, el siguiente es un algoritmo que encontre en la red y fue el que estaba analizando, por cierto [Este](http://www.pythontutor.com/visualize.html#mode=edit) es un buen sitio para ver paso a paso como se ejecuta tu codigo en python.

```python
#Merge Sort  fuente: la web 
def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2       
        left = myList[:mid]        
        right = myList[mid:]        
        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)
        # Two iterators for traversing the two halves
        i = 0
        j = 0        
        # Iterator for the main list
        k = 0       
        while i < len(left) and j < len(right):            
            if left[i] < right[j]:               
                # The value from the left half has been used
                myList[k] = left[i]          
                # Move the iterator forward
                i += 1                
            else:
                
                myList[k] = right[j]               
                j += 1                
            # Move to the next slot
            k += 1
        # For all the remaining values
        while i < len(left):                       
            myList[k] = left[i]                    
            i += 1            
            k += 1
        while j < len(right):            
            
            myList[k]=right[j]            
            j += 1           
            k += 1       

myList = list(range (5,0,-1))
mergeSort(myList)
print(myList)

```
Este otro ejemplo de codigo es tomado del curso guía

```python
def mergesort(lst):    
    
    if len(lst) <= 1:
        return lst
    
  
    else:

        midpoint = len(lst) // 2        
        left = mergesort(lst[:midpoint])
       
        right = mergesort(lst[midpoint:])       
        newlist = []
        while len(left) and len(right) > 0:
            
            if left[0] < right[0]:
                newlist.append(left[0])
                del left[0]            
            else:
                newlist.append(right[0])
                del right[0]       

        newlist.extend(left)
        newlist.extend(right)       

        return newlist


print(mergesort([2, 5, 3, 82, 6, 9, 1, 4, 7]))
```
### Algoritmos de Busqueda
 Algoritmos que toman como entrada una lista y un valor para buscar, y producen como salida el índice o índices donde se encontró ese valor en la lista. es realmente sencilo.

 ```python
 def linear (lista,busqueme) :
    
    for i in range(len(lista)) :
        if lista[i] == busqueme :
            return i
    return False
a_list = [5, 1, 3, 6, 7, 3, 1, 6, 7, 8, 3, 6]
print(linear(a_list, 6))

 ```

 Busqueda Binaria
 ```python
 def binaria (lista,buscame) :
    final =  len (lista)-1
    inicio = 0
    if buscame == lista [inicio] :
        return inicio
    elif buscame == final :
        return final
    while inicio <= final :        
        m = (inicio+ final)//2
        if buscame == lista[m] :
            return m
        elif buscame  > lista [m ]:
            inicio = m +1
            
        else:
            final = m-1
            
    return False 
lis = list(range (50,100,1))
print (lis)
print (binaria (lis,50))
 ```
 

