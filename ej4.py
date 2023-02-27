import random
import time

FILAS = 4
COLUMNAS = 4
class Entorno4:
    recompensa = 0

    def __init__(self,id,acciones:dict):
        self.id = id

        #Creación de la cuadrícula
        self.cuadricula = []
        for i in range(FILAS):
            self.cuadricula.append([])
            for j in range(COLUMNAS):
                self.cuadricula[i].append(0)


        self.acciones = acciones
        #Se añaden a la cuadrícula números para no empezar de vacío
        self._anyadirNumero()
        self._anyadirNumero()
        self.estado_actual = self.cuadricula

    """
    Función que añade un número (2 o 4) a la cuadrícula
    """
    def _anyadirNumero(self):
        casilla = [0,0]
        casilla[0] = random.randint(0, FILAS-1)
        casilla[1] = random.randint(0, COLUMNAS-1)
        #Se añade siempre y cuando la casilla este vacía
        while(self.cuadricula[casilla[0]][casilla[1]] != 0):
            casilla[0] = random.randint(0, FILAS-1)
            casilla[1] = random.randint(0, COLUMNAS-1)

        self.cuadricula[casilla[0]][casilla[1]] = random.choice([2,4])

    """
    Función que comprueba si se ha acabado el juego (se obtiene la ficha con valor 2048)
    """
    def ganador(self):
        for i in range(len(self.cuadricula)):
            for j in range(len(self.cuadricula[0])):
                if self.cuadricula[i][j] == 2048:
                    return True
        return False
    

    """
    Función que comprueba si el usuario no puede realizar más movimientos
    """
    def sin_movimientos(self):
        final = True

        #Se comprueba si hay dos casillas iguales que estén al lado
        for y in range(len(self.cuadricula)):
            for x in range(len(self.cuadricula)-1):
                if self.cuadricula[y][x] == self.cuadricula[y][x+1]:
                    final = False

        for y in range(len(self.cuadricula)-1):
            for x in range(len(self.cuadricula)):
                if self.cuadricula[y][x] == self.cuadricula[y+1][x]:
                    final = False

        return final

    """
    Función que realiza el movimiento hacia la derecha
    """
    def mover_derecha(self):
        #Se ejecuta la acción de mover a la derecha
        for y in range(len(self.cuadricula)):
            mezclas = []
            for i in range(len(self.cuadricula)-1):
                for x in range(-2, -len(self.cuadricula)-1, -1): #se empieza a recorrer por el penúltimo elemento
                    if self.cuadricula[y][x] != 0 and self.cuadricula[y][x+1] == 0: #caso en el que el último este vacío
                        self.cuadricula[y][x+1] = self.cuadricula[y][x]
                        self.cuadricula[y][x] = 0
                    elif self.cuadricula[y][x] != 0 and self.cuadricula[y][x] == self.cuadricula[y][x+1] and \
                        x not in mezclas and x-1 not in mezclas: #Caso en el que hay que mezclar
                        self.cuadricula[y][x+1] *= 2
                        self.recompensa += self.cuadricula[y][x+1]
                        self.cuadricula[y][x] = 0
                        mezclas.append(x)

    """
    Función que realiza el movimiento hacia la izquierda
    """
    def mover_izquierda(self):
        for y in range(len(self.cuadricula)):
            mezclas = []
            for i in range(len(self.cuadricula)-1):
                for x in range(1, len(self.cuadricula)): #En este caso, se empieza a recorrer el segundo elemento (al ser movimiento a la izquierda)
                    if self.cuadricula[y][x] != 0 and self.cuadricula[y][x-1] == 0:
                        self.cuadricula[y][x-1] = self.cuadricula[y][x]
                        self.cuadricula[y][x] = 0
                    elif self.cuadricula[y][x] != 0 and self.cuadricula[y][x] == self.cuadricula[y][x-1] and \
                        x not in mezclas and x+1 not in mezclas:
                        self.cuadricula[y][x-1] *= 2
                        self.recompensa += self.cuadricula[y][x-1]
                        self.cuadricula[y][x] = 0
                        mezclas.append(x)
        

    """
    Función que realiza el movimiento hacia abajo
    """
    def mover_abajo(self):
        for x in range(len(self.cuadricula)):
            mezclas = []
            for i in range(len(self.cuadricula)-1):
                for y in range(-2, -len(self.cuadricula)-1, -1): #En este caso, se coge la columna en lugar de la fila como los anteriores (penúltimo)
                    if self.cuadricula[y][x] != 0 and self.cuadricula[y+1][x] == 0:
                        self.cuadricula[y+1][x] = self.cuadricula[y][x]
                        self.cuadricula[y][x] = 0
                    elif self.cuadricula[y][x] != 0 and self.cuadricula[y][x] == self.cuadricula[y+1][x] and \
                        y not in mezclas and y-1 not in mezclas:
                        self.cuadricula[y+1][x] *= 2
                        self.recompensa += self.cuadricula[y+1][x]
                        self.cuadricula[y][x] = 0
                        mezclas.append(y)
        

    """
    Función que realiza el movimiento hacia arriba
    """
    def mover_arriba(self):
        for x in range(len(self.cuadricula)):
            mezclas = []
            for i in range(len(self.cuadricula)-1):
                for y in range(1, len(self.cuadricula)):#Se coge la columna con el segundo
                    if self.cuadricula[y][x] != 0 and self.cuadricula[y-1][x] == 0:
                        self.cuadricula[y-1][x] = self.cuadricula[y][x]
                        self.cuadricula[y][x] = 0
                    elif self.cuadricula[y][x] != 0 and self.cuadricula[y][x] == self.cuadricula[y-1][x] and \
                        y not in mezclas and y+1 not in mezclas:
                        self.cuadricula[y-1][x] *= 2
                        self.recompensa += self.cuadricula[y-1][x]
                        self.cuadricula[y][x] = 0
                        mezclas.append(y)
        


    """
    Función que realiza la acción pasada por parámetros, añadiendo un número nuevo y comprobando si se ha acabado la partida.
    """
    def realizar_accion(self,accion):
        if accion == "right":
            self.mover_derecha()
        elif accion == "left":
            self.mover_izquierda()
        elif accion == "up":
            self.mover_arriba()
        elif accion == "down":
            self.mover_abajo()

        self._anyadirNumero()
        if self.ganador():
            print("Ha ganado el juego")
            return self.cuadricula, self.recompensa, True
        if self.sin_movimientos():
            print("Ha perdido, se ha quedado sin movimientos")
            return self.cuadricula, self.recompensa, False
        return self.cuadricula, self.recompensa, False
    
    """
    Función que muestra el estado de la cuadrícula (casillas llenas)
    """
    def renderizar(self):
        for i in self.cuadricula:
            for j in i:
                    print("\t", j, end=" ")
            print()
        print()


acciones = {"left":0,"right":1,"up":2,"down":3}

"""
entorno = Entorno4("ejercicio4", acciones)
print(entorno.realizar_accion(1))

for i in range(5):

    accion = random.choices(list(acciones), k=1)[0]
    entorno.realizar_accion(accion)
    print(accion)
    entorno.renderizar()
    
print(entorno.recompensa)
"""