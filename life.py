from random import random, seed
import numpy as np

from os import system, name
  
# import sleep to show output for some time period
from time import sleep

seed(1)


print('Insert the width and length!')
col = int(input('Colunas: '))
lin = int(input('Linhas: '))

matrix = np.random.randint(2, size=(lin, col)) 
newmatrix = matrix

#print('Before State:')
#print(matrix)
#print(matrix[1][1])

def neighbours(matrix, coord, columns, lines):
    alive = 0
    for i in range(3):
        for j in range(3):
            if not(i == 1 and j == 1):
                #print('(' + str(i - 1 + coord[0]) + ',' + str(j - 1 + coord[1]) + ')')
                x = i - 1 + coord[0]
                y = j - 1 + coord[1]
                if (x >= 0 and x < columns and y >= 0 and y < lines):
                    neighbour = (x, y)
                    #print(neighbour)
                    if (matrix[x][y] == 1):
                        alive += 1
    #print('Number of Alive Neighbours in ' + str(coord) + ': ' + str(alive))
    return alive

def changeState(matrix, columns, lines):
    for i in range(lines):
        for j in range(columns):
            neighborhood = neighbours(matrix,(i,j), columns, lines)
            if (neighborhood == 3):
                    newmatrix[i][j] = 1 #Revive
            elif (neighborhood == 2):
                if (matrix[i][j] == 1):
                    newmatrix[i][j] = 1
            else:
                newmatrix[i][j] = 0
    return newmatrix

#print('After State: ')

#newmatrix = changeState(matrix, col, lin)

#print(newmatrix)


#while(1):
#    newmatrix = changeState(matrix, col, lin)
#    print(newmatrix)
#    matrix = newmatrix
#    system('clear')
