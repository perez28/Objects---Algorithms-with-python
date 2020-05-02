#factorial recursivo
"""
def Factorial (n) :
    
    if n >1 :  
       return n * Factorial(n-1)        
    
    else :
        return 1
   
print(Factorial (4))
"""
#fibonacci no recursivo
"""
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
"""
#fibonacci Recursivo
"""
def fib(n):    
    if n == 1 or n == 2:
        return 1   
    else:
        return fib(n - 1) + fib(n - 2)  

print("fib(5) is", fib(5))
print("fib(10) is", fib(10))
"""
"""
def conteo_regresivo (num) :
    if num <= 0:
        print (num)
    else:
        
        conteo_regresivo (num-1)
        print(num)
conteo_regresivo(5)
"""

#Ordenamiento Burbuja
"""
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
"""
#insertion version 1 no es eficiente repite bucles sin necesidad
"""
def insersion (num) :
    
    for i in range(len(num)-1) :
        #print ('flag',flag)
        #print ('i',i)
        pibo =num [i]
        #print ('pibo 1 for',pibo)
        largo = (len(num)-1) - i
        
        #print ('largo',largo)
        for x in range(largo) :
            #print ('x',x,'num[x]=',num[x])
            #print ('hago la comparación if pibo',pibo ,'>', num [x +flag], 'num [x +1]')
            if pibo > num [x +(1+i)] :
                #print ('pibote',pibo)
                pibo = num [x + (1+i)]
                #print ('num [x +flag]',num [x +flag], '= pibo', pibo)
                ides = num.index (num[i])
                #print('ides',ides)
                #print ('pibote',pibo)
                #print('num',num)
                num.remove (pibo)
                #print ('remove',pibo,list(num))
                num.insert (ides,pibo)
                #print ('insert',ides,pibo,list(num))
            print(num)
        print('\n')
        
    return num
numero =[34, 16, 2, 78, 4, 6, 1]
numero2 = [3,2,4,5,1]
print ('insersion')
print (list(numero))
insersion(numero)  
"""
#insertion version 2 mas eficiente que la anterior
"""
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
"""

#Merge Sort  fuente: la web 
"""
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
"""

#Merge Sort  fuente: guía del curso
"""
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


print(mergesort([2, 5, 3, 8, 6]))
"""
#Busqueda lineal
"""
def linear (lista,busqueme) :
    
    for i in range(len(lista)) :
        if lista[i] == busqueme :
            return i
    return False
a_list = [5, 1, 3, 6, 7, 3, 1, 6, 7, 8, 3, 6]
print(linear(a_list, 6))
"""


