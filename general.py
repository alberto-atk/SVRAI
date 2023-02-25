from ej1 import *
from ej2 import *
#from ej3 import *
from ej4 import *
import numpy as np

def ejercicio1():

    acciones = {"no_gira":0,"gira":1} #no gira y gira
    estados = {"bajo":0, "medio": 1,"alto": 2 }

    entorno = Entorno1("ejercicio1",estados, acciones)

    entorno.definir_movimientos(estados["alto"],acciones["gira"],estados["alto"])
    entorno.definir_movimientos(estados["alto"],acciones["no_gira"],estados["medio"])

    entorno.definir_movimientos(estados["medio"],acciones["gira"],estados["alto"])
    entorno.definir_movimientos(estados["medio"],acciones["no_gira"],estados["bajo"])

    entorno.definir_movimientos(estados["bajo"],acciones["gira"],estados["medio"])
    entorno.definir_movimientos(estados["bajo"],acciones["no_gira"],estados["bajo"])
    return entorno


def ejercicio2():
    acciones = {"gira_lento":0,"gira_rapido":1}
    estados = {"bajo":0, "medio": 1,"alto": 2, "superior":3}


    entorno = Entorno2("ejercicio2",estados, acciones)

    return entorno

def ejercicio3():
    acciones = {"left":0,"right":1,"up":2,"down":3}

    cuadricula = []
    for i in range(10):
        cuadricula.append([])
        for j in range(10):
            cuadricula[i].append(0)

    cuadricula[7][8] = 10
    cuadricula[2][7] = 3
    cuadricula[4][3] = -5
    cuadricula[7][3] = -10
    entorno = Entorno3("ejercicio3",cuadricula, acciones)

    return entorno

def ejercicio4():
    acciones = {"left":0,"right":1,"up":2,"down":3}


    entorno = Entorno4("ejercicio4", acciones)

    return entorno


def valueIteration():
    def lookahead(U,s,a,gamma=0.8):
        for sp in range(len(estados)):
            return R[s][a][sp] + gamma*np.sum(T[s][a][sp]*U[sp])

    def backup(env,U,estado):
        return max([lookahead(U,estado,a) for a in list(env.acciones.values())])

    env = ejercicio2()
    nS = len(env.estados)
    nA = len(env.acciones)

    estados = list(env.estados.values())
    acciones = list(env.acciones.values())
    T = np.zeros([nS, nA, nS])
    R = np.zeros([nS, nA, nS])
    for state_number,s in enumerate(estados):
        for a in acciones:
            p_trans,next_s,rew = env.nuevo_estado(s,a)
            T[state_number,a,next_s] += p_trans
            R[state_number,a,next_s] = rew
            T[state_number,a,:]/=np.sum(T[state_number,a,:])


    U = [0.0 for s in range(nS)]
    max_iters = 1000
    for i in range(max_iters):
        U = [backup(env,U,s) for s in range(nS)]
    print("U: " + str(U))

valueIteration()