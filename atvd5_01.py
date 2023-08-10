
#LETRA B

from mip import Model, xsum, minimize, BINARY, LinExpr
import numpy as np

numLocaisPostos = 10
numZonas = 20

custoLocaisPostos = [1200, 1500, 1300, 1250, 1650, 1750, 1150, 1900, 1050, 1420]

#M == Subconjuntos de Zonas
#Mij ==> onde j-> postos, i-> zonas
# se a zona não foi numerada, ela esta como zero 
M = np.zeros((10,20), dtype=np.int64)
#posto 0 atende ao subconjunto [0,1,4]
M[0][0] = 1
M[0][1] = 1
M[0][4] = 1
#posto 1 atende ao subconjunto [5,7,9]
M[1][5] = 1
M[1][7] = 1
M[1][9] = 1
#posto 2 atende ao subconjunto [4,5,9,10]
M[2][4] = 1
M[2][5] = 1
M[2][9] = 1
M[2][10] = 1
#posto 3 atende ao subconjunto [2,3,8]
M[3][2] = 1
M[3][3] = 1
M[3][8] = 1
#posto 4 atende ao subconjunto [6,8,10,12,14]
M[4][6] = 1
M[4][8] = 1
M[4][10] = 1
M[4][12] = 1
M[4][14] = 1
#posto 5 atende ao subconjunto [11,12]
M[5][11] = 1
M[5][12] = 1
#posto 6 atende ao subconjunto [2,6,10]
M[6][2] = 1
M[6][6] = 1
M[6][10] = 1
#posto 7 atende ao subconjunto [13,19]
M[7][13] = 1
M[7][19] = 1
#posto 8 atende ao subconjunto [15,16,18]
M[8][15] = 1
M[8][16] = 1
M[8][18] = 1
#posto 9 atende ao subconjunto [14,17,19]
M[9][14] = 1
M[9][17] = 1
M[9][19] = 1


m = Model("Ex1 - Avaliacao Pratica - Parte 5")

# se o posto j atende a zona i
x = [[m.add_var(name='x', var_type=BINARY) 
    for i in range(numZonas)]  
        for j in range(numLocaisPostos)]

#se o posto da localização i foi realmente construido
y = [m.add_var(name='y', var_type=BINARY) for j in range(numLocaisPostos)]


m.objective = minimize(xsum(y[j]  * custoLocaisPostos[j] for j in range(numLocaisPostos)))

#cada zona deve ser atendida por apenas 1 posto dos que planejam ser construidos
#para a zona ser atendia pelo posto, aquela zona deve estar contida no subconjunto de zonas que aquele posto atende
# ou seja se pertence ao subconjunto M[i] para aquele  

for i in range(numZonas):
            m += xsum(M[j][i] * x[j][i] for j in range(numLocaisPostos)) == 1


#uma zona so pode ser atendida por um posto que realmente tenha sido construido 
#se y = 1 x pode ser 1 ou 0, mas se y for 0 x so pode ser 0
for j in range(numLocaisPostos):
    for i in range(numZonas):
        m +=  y[j] >= x[j][i]


m.optimize()

print("Soma dos custos dos postos(Valor otimo): {}".format(m.objective_value)) #valor otimo da funcao objetivo



