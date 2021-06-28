# Creating a bubble sort function  
def bubblesort(lista):
    #outer for loop
    for i in range(0,len(lista)-1):
        for j in range(len(lista)-1):
            if(lista[j]>lista[i]):
                temp = lista[j]
                lista[j]=lista[j+1]
                lista[j+1]=temp
    return lista

lista=[12,42,8,33,15]
print("The unsorted list is : ",lista)
print("The sorted list is",bubblesort(lista))
