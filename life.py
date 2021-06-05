from random import random
import numpy as np
from time import sleep
from os import system, name

print('Insert the width and length!')
col = int(input('Colunas: '))
lin = int(input('Linhas: '))

matrix = np.zeros((lin, col), dtype=int)
newmatrix = matrix.copy()

matrix[:][0] = 1
#print('Before State:')
# print(matrix)
# print(matrix[1][1])


def neighbours(matrix, coord, columns, lines):
    alive = 0
    for i in range(3):
        for j in range(3):
            if not(i == 1 and j == 1):
                x = i - 1 + coord[0]
                y = j - 1 + coord[1]
                if (x >= 0 and x < columns and y >= 0 and y < lines):
                    neighbour = (x, y)
                    if (matrix[x][y] == 1):
                        alive += 1
    return alive


def changeState(matrix, columns, lines):
    for i in range(lines):
        for j in range(columns):
            neighborhood = neighbours(matrix, (i, j), columns, lines)
            if (neighborhood == 3):
                newmatrix[i][j] = 1  # Revive
            elif (neighborhood == 2):
                if (matrix[i][j] == 1):
                    newmatrix[i][j] = 1
            else:
                newmatrix[i][j] = 0
    return newmatrix

#print('After State: ')

#newmatrix = changeState(matrix, col, lin)

# print(newmatrix)


def nolimit(matrix, col):
    fstcol = matrix[:][0]
    matrix[2][2] = 1
    lstcol = matrix[col-1][:]
    print('Fisrt column:')
    print(fstcol)
    print('last column:')
    print(lstcol)
    nolimit = np.zeros((lin + 2, col + 2), dtype=int)
    #nolimit = np.concatenate((lin, col), dtype=int)
    print(nolimit)
    matrix = nolimit


# while(1):
#    print(matrix)
#    newmatrix = changeState(matrix, col, lin)
#    print('New:')
#    print(newmatrix)
#    sleep(2)
#    matrix = newmatrix.copy()
#    system('clear')


print('With limits:')
print(matrix)
nolimit(matrix, 3)
print('Without limit:')
print(matrix)
