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

        self.cuadricula[0][0] = 4
        self.cuadricula[2][0] = 2
        self.acciones = acciones
        #self._anyadirNumero()
        #self._anyadirNumero()
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


    def comprimir_casillas(self,i1,j1,i2,j2,i3,j3):
        if self.cuadricula[i1][j1] == self.cuadricula[i2][j2]:
            self.cuadricula[i3][j3] = self.cuadricula[i1][j1] + self.cuadricula[i2][j2]
        

    def desplazar_casillas_right(self,i,j):
        aux1 = j
        aux2 = j +1
        while aux2 < COLUMNAS and self.cuadricula[i][aux2] == 0:
            self.cuadricula[i][aux2] = self.cuadricula[i][aux1]
            self.cuadricula[i][aux1] = 0
            aux1 += 1
            aux2 += 1  

    def desplazar_casillas_left(self,i,j):        
        aux1 = j
        aux2 = j -1
        while aux2 >= 0 and self.cuadricula[i][aux2] == 0:
            self.cuadricula[i][aux2] = self.cuadricula[i][aux1]
            self.cuadricula[i][aux1] = 0
            aux1 -= 1
            aux2 -= 1  

    def desplazar_casillas_up(self,i,j):        

        aux1 = i
        aux2 = i -1
        while aux2 >= 0 and self.cuadricula[aux2][j] == 0:
            self.cuadricula[aux2][j] = self.cuadricula[aux1][j]
            self.cuadricula[aux1][j] = 0
            aux1 -= 1
            aux2 -= 1 

    def desplazar_casillas_down(self,i,j):
            aux1 = i
            aux2 = i +1
            while aux2 < FILAS and self.cuadricula[aux2][j] == 0:
                self.cuadricula[aux2][j] = self.cuadricula[aux1][j]
                self.cuadricula[aux1][j] = 0
                aux1 += 1
                aux2 += 1 

    def realizar_accion(self,accion):
        if accion == "right":
            for i in range(len(self.cuadricula)):
                for j in reversed(range(len(self.cuadricula[i]))):
                    if self.cuadricula[i][j] != 0:
                        self.desplazar_casillas_right(i,j)
        elif accion == "left":
            for i in range(len(self.cuadricula)):
                for j in range(len(self.cuadricula[i])):
                    if self.cuadricula[i][j] != 0:
                        self.desplazar_casillas_left(i,j)
        elif accion == "up":
            for i in range(len(self.cuadricula)):
                for j in range(len(self.cuadricula[i])):
                    if self.cuadricula[i][j] != 0:
                        self.desplazar_casillas_up(i,j)
        elif accion == "down":
            for i in reversed(range(len(self.cuadricula))):
                for j in reversed(range(len(self.cuadricula[i]))):
                    if self.cuadricula[i][j] != 0:
                        self.desplazar_casillas_down(i,j)
                        
                        
        #self._anyadirNumero()
    
    def renderizar(self):
        for i in self.cuadricula:
            for j in i:
                    print("\t", j, end=" ")
            print()


acciones = {"left":0,"right":1,"up":2,"down":3}


entorno = Entorno("ejercicio4", acciones)
entorno.renderizar()
entorno.realizar_accion("down")
print()
entorno.renderizar()
