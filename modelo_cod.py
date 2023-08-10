from mip import Model, xsum, minimize, INTEGER, LinExpr
import numpy as np

#ENTRADAS:
componentes = 4 #componentes
maquinas = 6    #maqui   2.47, 4.40, 1.90] #custo de fabricação
c = [3.10, 2.60, 4.50, 2.25] #custo de compra

t = [
    [0.04, 0.02, 0.02, 0.00, 0.03, 0.06],
    [0.00, 0.01, 0.05, 0.15, 0.09, 0.06],
    [0.02, 0.06, 0.00, 0.06, 0.20, 0.20],
    [0.06, 0.04, 0.15, 0.00, 0.00, 0.05]
]   #tempo que cada maquina leva para cada componente

#VARIÁVEL MODELO
m = Model("Trabalho 4")  

#VARIÁVEIS

# Xij = 1, se a componente i foi fabricada, para todo i ={1,2,3,4} , 0 c.c
x = [m.add_var(name='x', var_type=INTEGER, lb=0, ub=30)for i in range(componentes)] 

# Yi = 1, se a componente i foi comprada, para todo i ={1,2,3,4}, 0 c.c
y = [m.add_var(name='y', var_type=INTEGER, lb=0, ub=30)for i in range(componentes)]   

# F.O.
m.objective = minimize(150 * (xsum(f[i] * x[i] for i in range(componentes)) + xsum(c[i] * y[i] for i in range(componentes))))

# S.A.

# Se foi produzido, não será comprado e vice versa
for i in range(componentes):
    m += x[i] + y[i] == 1
# cada máquina funciona até  40h/semana
for j in range(maquinas):
    m += xsum(150 * t[i][j] * x[i] for i in range(componentes)) <= 40
#as 4 componentes tem que ter na empresa, sendo comprados ou fabricados
    m += xsum(x[i] + y[i] for i in range(componentes)) == 4

m.optimize()
print("Componente(s) fabricada(s): ")
for i in range(componentes):
    if x[i].x == 1:
        print(f"{i + 1}")
print("Componente(s) comprada(s): ")
for i in range(componentes):
    if y[i].x == 1:
        print(f"{i + 1}")

# RESULTADO ÓTIMO
print("\nResultado otimo: {}".format(m.objective_value))