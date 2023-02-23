from ej1 import *
from ej2 import *
from ej3 import *
from ej4 import *

def ejercicio1():

    acciones = {"no_gira":0,"gira":1} #no gira y gira
    estados = {"bajo":Estado("bajo"), "medio": Estado("medio"),"alto": Estado("alto") }

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
    estados = [Estado("bajo"),Estado("medio"),Estado("alto"),Estado("superior")]

    entorno = Entorno2("ejercicio2",estados, acciones)

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

def ejercicio4():
    acciones = {"left":0,"right":1,"up":2,"down":3}


    entorno = Entorno4("ejercicio4", acciones)

