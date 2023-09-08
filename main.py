import numpy as np
from array import array

#Inicio da função
def sort(array):

    for final in range(len(array), 0, -1):
        exchanging = False

        for current in range(0, final - 1):
                
    #Compara se o elemento atual é maior que o próximo elemento
            if array[current] > array[current + 1]:
                #Caso verdade, os elementos trocam de posição
                array[current], array[current + 1] = array[current + 1], array[current]
                exchanging = True
            
        if not exchanging:
            break


file = open("1000_numbers.txt", "r")

line = file.readlines()

arrayFinal = np.array(line)

sort(arrayFinal)
print(arrayFinal)