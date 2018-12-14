'''
Created on 13/12/2018

@author: acer
'''

'''
https://rosettacode.org/wiki/Floyd-Warshall_algorithm#Python

'''
from math import inf
from itertools import product
 
def floyd_warshall(numVertices, pesos):
    rn = range(numVertices)
    #Prepara un arreglo infinito
    distancia = [[inf] * numVertices for i in rn] 
    siguiente  = [[0]   * numVertices for i in rn]
    for i in rn:
        distancia[i][i] = 0
    for aux1, aux2, aux3 in pesos:
        distancia[aux1-1][aux2-1] = aux3
        siguiente[aux1-1][aux2-1] = aux2-1
    for k, i, j in product(rn, repetir=3):
        sum_ik_kj = distancia[i][k] + distancia[k][j]
        if distancia[i][j] > sum_ik_kj:
            distancia[i][j] = sum_ik_kj
            siguiente[i][j]  = siguiente[i][k]
    print("par     distancia    camino")
    for i, j in product(rn, repetir=2):
        if i != j:
            path = [i]
            while path[-1] != j:
                path.append(siguiente[path[-1]][j])
            print("%d → %d  %4d       %s" 
                  % (i + 1, j + 1, distancia[i][j], 
                     ' → '.join(str(p + 1) for p in path)))
 
if __name__ == '__main__':
    floyd_warshall(4, [[1, 3, -2], [2, 1, 4], [2, 3, 3], [3, 4, 2], [4, 2, -1]])


