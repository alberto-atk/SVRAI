import random

FILAS = 9
COLUMNAS = 9
class Entorno3:
    estado_actual = [-1,-1]
    recompensa = 0
    estado_recompensa = False

    def __init__(self,id,cuadricula:dict, acciones:dict):
        self.id = id
        self.cuadricula = cuadricula
        self.acciones = acciones
        #self.estado_actual[0] = random.randint(0, FILAS)
        #self.estado_actual[1] = random.randint(0, COLUMNAS)
        self.estado_actual[0] = 7
        self.estado_actual[1] = 7

    def realizar_accion(self,accion):
        pesos = []
        if accion in acciones:
            if self.estado_recompensa:
                #Se suma la recompensa en el siguiente estado
                self.recompensa += self.cuadricula[self.estado_actual[0]][self.estado_actual[1]]
                self.estado_recompensa = False
                #Se mueve a una esquina
                nueva_casilla = random.choice([(0,0),(FILAS,0),(0,COLUMNAS),(FILAS,COLUMNAS)])
                self.estado_actual[0] = nueva_casilla[0]
                self.estado_actual[1] = nueva_casilla[1]
            else:
                #Generacion de los pesos para realizar un movimiento u otro
                for i in (list(self.acciones)):
                    if i == accion:
                        pesos.append(0.7)
                    else:
                        pesos.append(0.1)

                #Obtencion de la accion
                #print(self.estado_actual)
                auxEstado = self.estado_actual.copy()
                accionFinal = random.choices(population=list(acciones),k=1,weights=pesos)[0]
                #print(accionFinal)
                if accionFinal == "up" and self.estado_actual[0] > 0:
                    self.estado_actual[0] -= 1
                elif accionFinal == "right" and self.estado_actual[1] < COLUMNAS:
                    self.estado_actual[1] += 1
                elif accionFinal == "left" and self.estado_actual[1] > 0:
                    self.estado_actual[1] -= 1
                elif accionFinal == "down" and self.estado_actual[0] < FILAS:
                    self.estado_actual[1] += 1
                
                if auxEstado == self.estado_actual:
                    self.recompensa -= 1
                elif self.cuadricula[self.estado_actual[0]][self.estado_actual[1]] < 0:
                    self.recompensa += self.cuadricula[self.estado_actual[0]][self.estado_actual[1]]
                else:
                    self.estado_recompensa = True
                #print(self.recompensa)
                #print(self.estado_actual)
    
    def renderizar(self):
        for i in range(len(self.cuadricula)):
            for j in range(len(self.cuadricula[i])):
                if i == self.estado_actual[0] and j == self.estado_actual[1]:
                    print("\t", "*", end=" ")
                else:
                    print("\t", self.cuadricula[i][j], end=" ")  
            print()

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


"""
Para mostrar la matriz:
    for fila in estados:
        for valor in fila:
            print("\t", valor, end=" ")
        print()
"""
entorno = Entorno3("ejercicio3",cuadricula, acciones)
entorno.renderizar()
entorno.realizar_accion("right")
print()
entorno.renderizar()
entorno.realizar_accion("up")
print()
print(entorno.recompensa)
print()
entorno.renderizar()