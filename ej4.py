import random
import time

FILAS = 4
COLUMNAS = 4
class Entorno4:
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


    def ganador(self):
        for i in range(len(self.cuadricula)):
            for j in range(len(self.cuadricula[0])):
                if self.cuadricula[i][j] == 2048:
                    return True
        return False
    
    def sin_movimientos(self):
        final = True

        for y in range(len(self.cuadricula)):
            for x in range(len(self.cuadricula)-1):
                if self.cuadricula[y][x] == self.cuadricula[y][x+1]:
                    final = False

        for y in range(len(self.cuadricula)-1):
            for x in range(len(self.cuadricula)):
                if self.cuadricula[y][x] == self.cuadricula[y+1][x]:
                    final = False

        return final

    def mover_derecha(self):
        for y in range(len(self.cuadricula)):
            mezclas = []
            for i in range(len(self.cuadricula)-1):
                for x in range(-2, -len(self.cuadricula)-1, -1):
                    if self.cuadricula[y][x] != 0 and self.cuadricula[y][x+1] == 0:
                        self.cuadricula[y][x+1] = self.cuadricula[y][x]
                        self.cuadricula[y][x] = 0
                    elif self.cuadricula[y][x] != 0 and self.cuadricula[y][x] == self.cuadricula[y][x+1] and \
                        x not in mezclas and x-1 not in mezclas:
                        self.cuadricula[y][x+1] *= 2
                        self.recompensa += self.cuadricula[y][x+1]
                        self.cuadricula[y][x] = 0
                        mezclas.append(x)


    def mover_izquierda(self):
        for y in range(len(self.cuadricula)):
            mezclas = []
            for i in range(len(self.cuadricula)-1):
                for x in range(1, len(self.cuadricula)):
                    if self.cuadricula[y][x] != 0 and self.cuadricula[y][x-1] == 0:
                        self.cuadricula[y][x-1] = self.cuadricula[y][x]
                        self.cuadricula[y][x] = 0
                    elif self.cuadricula[y][x] != 0 and self.cuadricula[y][x] == self.cuadricula[y][x-1] and \
                        x not in mezclas and x+1 not in mezclas:
                        self.cuadricula[y][x-1] *= 2
                        self.recompensa += self.cuadricula[y][x-1]
                        self.cuadricula[y][x] = 0
                        mezclas.append(x)


    def mover_abajo(self):
        for x in range(len(self.cuadricula)):
            mezclas = []
            for i in range(len(self.cuadricula)-1):
                for y in range(-2, -len(self.cuadricula)-1, -1):
                    if self.cuadricula[y][x] != 0 and self.cuadricula[y+1][x] == 0:
                        self.cuadricula[y+1][x] = self.cuadricula[y][x]
                        self.cuadricula[y][x] = 0
                    elif self.cuadricula[y][x] != 0 and self.cuadricula[y][x] == self.cuadricula[y+1][x] and \
                        y not in mezclas and y-1 not in mezclas:
                        self.cuadricula[y+1][x] *= 2
                        self.recompensa += self.cuadricula[y+1][x]
                        self.cuadricula[y][x] = 0
                        mezclas.append(y)


    def mover_arriba(self):
        for x in range(len(self.cuadricula)):
            mezclas = []
            for i in range(len(self.cuadricula)-1):
                for y in range(1, len(self.cuadricula)):
                    if self.cuadricula[y][x] != 0 and self.cuadricula[y-1][x] == 0:
                        self.cuadricula[y-1][x] = self.cuadricula[y][x]
                        self.cuadricula[y][x] = 0
                    elif self.cuadricula[y][x] != 0 and self.cuadricula[y][x] == self.cuadricula[y-1][x] and \
                        y not in mezclas and y+1 not in mezclas:
                        self.cuadricula[y-1][x] *= 2
                        self.recompensa += self.cuadricula[y-1][x]
                        self.cuadricula[y][x] = 0
                        mezclas.append(y)



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
            return
        if self.sin_movimientos():
            print("Ha perdido, se ha quedado sin movimientos")
            return
    
    def renderizar(self):
        for i in self.cuadricula:
            for j in i:
                    print("\t", j, end=" ")
            print()
        print()


acciones = {"left":0,"right":1,"up":2,"down":3}


entorno = Entorno4("ejercicio4", acciones)
for i in range(5):

    accion = random.choices(list(acciones), k=1)[0]
    entorno.realizar_accion(accion)
    print(accion)
    entorno.renderizar()
    
print(entorno.recompensa)