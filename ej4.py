import random

FILAS = 4
COLUMNAS = 4
class Entorno:
    recompensa = 0

    def __init__(self,id,acciones:dict):
        self.id = id

        self.cuadricula = []
        for i in range(FILAS):
            self.cuadricula.append([])
            for j in range(COLUMNAS):
                self.cuadricula[i].append(0)

        self.acciones = acciones
        self._anyadirNumero()
        self._anyadirNumero()
        #self.estado_actual[0] = random.randint(0, FILAS)
        #self.estado_actual[1] = random.randint(0, COLUMNAS)


    def _anyadirNumero(self):
        #Se anyade nuevo numero a la cuadricula (2 o 4)
        casilla = [0,0]
        casilla[0] = random.randint(0, FILAS-1)
        casilla[1] = random.randint(0, COLUMNAS-1)
        while(self.cuadricula[casilla[0]][casilla[1]] != 0):
            casilla[0] = random.randint(0, FILAS-1)
            casilla[1] = random.randint(0, COLUMNAS-1)

        self.cuadricula[casilla[0]][casilla[1]] = random.choice([2,4])

    def realizar_accion(self,accion):
        self._anyadirNumero()


    
    def renderizar(self):
        for i in self.cuadricula:
            for j in i:
                    print("\t", j, end=" ")
            print()


acciones = {"left":0,"right":1,"up":2,"down":3}




"""
Para mostrar la matriz:
    for fila in estados:
        for valor in fila:
            print("\t", valor, end=" ")
        print()
"""
entorno = Entorno("ejercicio4", acciones)
entorno.renderizar()
#entorno.realizar_accion("right")