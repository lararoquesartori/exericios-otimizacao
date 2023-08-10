from mip import Model, xsum, maximize, INTEGER, BINARY, LinExpr
import numpy as np



#LETRA A

print("Letra A:")

#ENTRADA
valorVertices = [5, 10, 10, 15, 20, 15]
G = np.zeros((6,6), dtype=np.int64)
G[0][1] = 1
G[0][2] = 1
G[1][2] = 1
G[1][3] = 1
G[1][5] = 1
G[2][5] = 1
G[3][5] = 1
G[3][4] = 1
G[4][5] = 1

numVertices = 6

#MODELO

m = Model("Ex1 - Avaliacao Pratica - Parte 5")


X = [m.add_var(var_type=BINARY) for i in range(numVertices)]

m.objective = maximize(xsum(X[i] * valorVertices[i] for i in range(numVertices)))

#esse subconjunto tem que ter apenas dois vertices
m += xsum(X[i] for i in range(numVertices)) == 2

#se os vertices são adjacentes so um deles pertence ao conjunto
for u in range(numVertices):
  for v in range(numVertices):
    m += G[u][v] + G[u][v]*X[u] + G[u][v]*X[v] <= 2

m.optimize() #aqui ele vai chamar o B&B

print("Uma solução otima é: ")
for i in range(numVertices):
    if valorVertices[i] != 0:
      print("Vertice {}: {}".format(i , X[i].x)) #imprimindo os valores da variaveis

print("Valor otimo: {}\n".format(m.objective_value)) #valor otimo da funcao objetivo



print("\n\n_______________________________________________________\n\n")



#LETRA B

print("Letra B:")

#ENTRADA
valorVertices = [5, 10, 20, 10, 5, 15, 10, 25, 15, 5]
G = np.zeros((10,10), dtype=np.int64)
G[0][1] = 1
G[0][8] = 1
G[1][2] = 1
G[1][3] = 1
G[2][6] = 1
G[2][7] = 1
G[3][5] = 1
G[4][6] = 1
G[4][9] = 1

numVertices = 10

#MODELO

m = Model("Ex2 - Avaliacao Pratica - Parte 5")


X = [m.add_var(var_type=BINARY) for i in range(numVertices)]

m.objective = maximize(xsum(X[i] * valorVertices[i] for i in range(numVertices)))

#esse subconjunto tem que ter apenas dois vertices
m += xsum(X[i] for i in range(numVertices)) == 2

#se os vertices são adjacentes so um deles pertence ao conjunto
for u in range(numVertices):
   for v in range(numVertices):
      m += G[u][v] + G[u][v]*X[u] + G[u][v]*X[v] <= 2
      #a multiplicação da aresta pelo vertice garante os casos de aresta = 0 

m.optimize() #aqui ele vai chamar o B&B

print("Uma solução otima é: ")
for i in range(numVertices):
    if valorVertices[i] != 0:
      print("Vertice {}: {}".format(i , X[i].x)) #imprimindo os valores da variaveis

print("Valor otimo: {}".format(m.objective_value)) #valor otimo da funcao objetivo


