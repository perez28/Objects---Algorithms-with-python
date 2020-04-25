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

