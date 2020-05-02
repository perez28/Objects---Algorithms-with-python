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