#parti2

file = open("inputExemple.txt","r")
file = open("input.txt","r")
data = file.read()

datalist = data.split("\n")

import math


####

def app(ch,b,x=1):
    ch = list(ch)
    for e in b:
        ch[e] += x
    
    return tuple(ch)

def valid(ch,ob):
    for i in range(len(ch)):
        if ch[i] > ob[i]:
            return False
    return True
 

import numpy as np
import pulp

cpt = 0
for l in datalist:

    l = l.split(" ")

    ch = tuple([a for a in l[0][1:-1]])
    ex = tuple(map(int,l[-1][1:-1].split(",")))

    l = l[1:-1]

    b = list(map(lambda x: x[1:-1].split(","),l))

    for i in range(len(b)):
        b[i] = list(map(int,b[i]))
    
    newnode = [(tuple([0 for i in range(len(ch))]),[])]
    oldnode = set()
    futnode = []
    showstate = set(newnode[0][0])
    p = 0

    curelem = tuple([0 for i in range(len(ch))])

    m = []
    for ii in range(len(b)):
        m.append([])
        for jj in range(len(ex)):
            if jj in b[ii]:
                m[ii].append(1)
            else:
                m[ii].append(0)
    
    m = np.array(m).T

    sib = np.array(ex)

    ##
    num_eqs, num_vars = m.shape

    # Définir le problème
    prob = pulp.LpProblem("IntegerSystemMinSum", pulp.LpMinimize)

    # Définir les variables entières POSITIVES
    x = [pulp.LpVariable(f"x{i}", lowBound=0, cat='Integer') for i in range(num_vars)]

    # Objectif : minimiser la somme des variables
    prob += pulp.lpSum(x)

    # Ajouter les contraintes
    for i in range(num_eqs):
        # it = [m[i][j] * x[j] for j in range(num_vars)]
        prob += pulp.lpSum(m[i][j] * x[j] for j in range(num_vars)) == sib[i]

    # Résoudre
    prob.solve(pulp.PULP_CBC_CMD(msg=False))


    # Afficher la solution
    solution = [int(var.value()) for var in x]
    # print("Solution entière :", solution)
    ##


    p = sum(solution)
    print(p)
    cpt +=p
    # print(ch)
    # print(b)
    # print(ex)

print(cpt)
