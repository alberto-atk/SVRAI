import random

FILAS = 10
COLUMNAS = 10
class Entorno3:
    posicion_actual = [-1,-1]
    recompensa = 0

    """
    Función inicial, en la que también se declaran los movimientos posibles con sus resultados
    """
    def __init__(self,id,cuadricula:dict, acciones:dict):
        self.id = id
        self.cuadricula = cuadricula
        self.acciones = acciones
        self.nestados = FILAS*COLUMNAS
        self.nacciones = len(acciones)
        self.estado_actual = random.randint(0, FILAS*COLUMNAS-1)
        self.P = self.generar_tabla_p()


    """
    Función que devuelve el entorno a condiciones iniciales
    """
    def reset(self):
        acciones = {"left":0,"right":1,"up":2,"down":3}

        cuadricula = []
        k = 0
        for i in range(FILAS):
            cuadricula.append([])
            for j in range(COLUMNAS):
                cuadricula[i].append(k)
                k += 1 #A cada cuadricula se le asigna un estado
        self.__init__("ejercicio3",cuadricula, acciones)
        return self.estado_actual

    """
    Función que realiza la acción pasada por parámetros sobre el entorno
    """
    def realizar_accion(self,accion):
        pesos = []
        if accion in self.acciones.values():
            if self.estado_actual == 42: #El número del estado(casilla) en el que se encuentran las recompensas
                self.recompensa = 5
                self.estado_actual = random.choice([0,9,90,99])
                return self.estado_actual,self.recompensa, False
            elif self.estado_actual == 73:
                self.recompensa = -10
                self.estado_actual = random.choice([0,9,90,99])
                return self.estado_actual,self.recompensa, False
            elif self.estado_actual == 78:
                self.recompensa = 10
                self.estado_actual = random.choice([0,9,90,99])
                return self.estado_actual,self.recompensa, False
            elif self.estado_actual == 27:
                self.recompensa = 3
                #Se mueve a una esquina
                self.estado_actual = random.choice([0,9,90,99])
                return self.estado_actual,self.recompensa, False

            #Generacion de los pesos para realizar un movimiento u otro
            for i in (list(self.acciones)):
                if i == accion:
                    pesos.append(0.7)
                else:
                    pesos.append(0.1)

            #Obtencion de la accion
            auxEstado = self.estado_actual
            accionFinal = random.choices(population=list(self.acciones.values()),k=1,weights=pesos)[0]
            self.estado_actual = self.obtener_nuevo_estado(self.estado_actual,accionFinal)
            
            if auxEstado == self.posicion_actual:
                self.recompensa -= 1
            return self.estado_actual,self.recompensa, False


    """
    Función auxiliar para generar las el contenido (acciones) de la tabla p 
    """  
    def nuevo_estado_tabla_p(self,estado,accion):
        if accion in self.acciones.values():
            recompensa = 0
            if estado == 42:
                recompensa = 5
                return [(0.25,j,recompensa) for j in [0,9,90,99]]
            elif estado == 73:
                recompensa = -10
                return [(0.25,j,recompensa) for j in [0,9,90,99]]
            elif estado == 78:
                recompensa = 10
                return [(0.25,j,recompensa) for j in [0,9,90,99]]
            elif estado == 27:
                recompensa = 3
                #Se mueve a una esquina
                return [(0.25,j,recompensa) for j in [0,9,90,99]]

            fila_tabla = []
            nuevoEstado = 0

            for i in self.acciones.values():
                nuevoEstado = self.obtener_nuevo_estado(estado,i)
                if i == accion:
                    fila_tabla.append((0.7,nuevoEstado,-1 if estado == nuevoEstado else 0))
                else:    
                    fila_tabla.append((0.1,nuevoEstado,-1 if estado == nuevoEstado else 0))
            return fila_tabla

    """
    Función que obtiene el estado futuro, dado un estado y una acción.
    """  
    def obtener_nuevo_estado(self,estado,accion):
        if estado+10 >= 100 and accion == 3:
            return estado
        elif estado-10 < 0 and accion == 2:
            return estado
        elif estado % 10 == 0 and accion == 0:
            return estado 
        elif estado % 10 == 9 and accion == 1:
            return estado

        if accion == 0:
            return estado - 1
        if accion == 1:
            return estado + 1
        if accion == 2:
            return estado - 10
        if accion == 3:
            return estado + 10

    """
    Función para generar la tabla P necesaria en algunos algoritmos
    """       
    def generar_tabla_p(self):
        P = {}
        for i in range(COLUMNAS*FILAS):
            acciones = {}
            for accion in self.acciones.values():
                acciones[accion] = self.nuevo_estado_tabla_p(i,accion) 
            P[i] = acciones
        return P


    """
    Función que muestra gráficamente el estado del entorno
    """  
    def renderizar(self):
        for i in range(len(self.cuadricula)):
            for j in range(len(self.cuadricula[i])):
                if i == self.posicion_actual[0] and j == self.posicion_actual[1]:
                    print("\t", "*", end=" ")
                else:
                    print("\t", self.cuadricula[i][j], end=" ")  
            print()
"""
acciones = {"left":0,"right":1,"up":2,"down":3}

cuadricula = []
k = 0
for i in range(FILAS):
    cuadricula.append([])
    for j in range(COLUMNAS):
        cuadricula[i].append(k)
        k += 1
    #k += 1


for i in range(FILAS):
    for j in range(COLUMNAS):
            print("\t", cuadricula[i][j], end=" ")  
    print()


entorno = Entorno3("ejercicio3",cuadricula, acciones)
print(entorno.generar_tabla_p())
"""