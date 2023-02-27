from random import choices

class Entorno1:
    movimientos = {}
    estado_actual = 0
    recompensa = 0


    """
    Función inicial, en la que también se declaran los movimientos posibles con sus resultados
    """
    def __init__(self,id,estados, acciones):
        self.id = id
        self.estados = estados
        self.acciones = acciones
        self.estado_actual = estados[choices(list(estados), k=1)[0]]
        self.nestados = len(estados)
        self.nacciones = len(acciones)
        
        self.definir_movimientos(estados["alto"],acciones["gira"],estados["alto"])
        self.definir_movimientos(estados["alto"],acciones["no_gira"],estados["medio"])

        self.definir_movimientos(estados["medio"],acciones["gira"],estados["alto"])
        self.definir_movimientos(estados["medio"],acciones["no_gira"],estados["bajo"])

        self.definir_movimientos(estados["bajo"],acciones["gira"],estados["medio"])
        self.definir_movimientos(estados["bajo"],acciones["no_gira"],estados["bajo"])
        self.P = self.generar_tabla_p()

    """
    Función que devuelve el entorno a condiciones iniciales
    """
    def reset(self):
        acciones = {"no_gira":0,"gira":1} #no gira y gira
        estados = {"bajo":0, "medio": 1,"alto": 2 }
        self.__init__("ejercicio1",estados,acciones)
        return self.estado_actual
    

    """
    Función que añade un movimiento al diccionario de posibilidades
    """
    def definir_movimientos(self,estado1,accion,estado2):
        self.movimientos[(estado1,accion)] = estado2


    """
    Función que realiza la acción pasada por parámetros sobre el entorno
    """
    def realizar_accion(self,accion):
        if accion in self.acciones.values():
            estado_anterior = self.estado_actual
            self.estado_actual = self.movimientos[(self.estado_actual,accion)]
            if str(self.estado_actual) == "bajo":
                self.recompensa -= 1
                return self.estado_actual, -1, False
            else:
                self.recompensa += 2
                return self.estado_actual, 2, False

    """
    Función que obtiene el estado futuro, dado un estado y una acción.
    """   
    def nuevo_estado(self,estado,accion):
        nuevo_estado = self.movimientos[(estado,accion)]
        if nuevo_estado == 0:
            self.recompensa -= 1
            return 1, nuevo_estado, -1
        else:
            self.recompensa += 2
            return 1, nuevo_estado, 2


    """
    Función para generar la tabla P necesaria en algunos algoritmos
    """  
    def generar_tabla_p(self):
        P = {}
        for i in range(len(self.estados)):
            acciones = {}
            for accion in self.acciones.values():
                acciones[accion] = self.nuevo_estado(i,accion) 
            P[i] = acciones
        return P
    
    """
    Función que muestra gráficamente el estado del entorno
    """
    def renderizar(self):
        print()
        auxDibujo = []
        for i in self.estados.values():
            if self.estado_actual == i:
                auxDibujo.append("  *")
            else:
                auxDibujo.append(" ")
        
        for i in range(len(self.estados)):
            print(auxDibujo[i], end="\t")
        print()
        for i in range(len(self.estados)):
            print(list(self.estados)[i], end="\t")
        print()



"""
acciones = [0,1] #no gira y gira
estados = [0,1,2]

entorno = Entorno1("ejercicio1",estados, acciones)

entorno.definir_movimientos(estados["alto"],acciones["gira"],estados["alto"])
entorno.definir_movimientos(estados["alto"],acciones["no_gira"],estados["medio"])

entorno.definir_movimientos(estados["medio"],acciones["gira"],estados["alto"])
entorno.definir_movimientos(estados["medio"],acciones["no_gira"],estados["bajo"])

entorno.definir_movimientos(estados["bajo"],acciones["gira"],estados["medio"])
entorno.definir_movimientos(estados["bajo"],acciones["no_gira"],estados["bajo"])


#entorno.realizar_accion(acciones["no_gira"])
entorno.renderizar()
entorno.realizar_accion(acciones["no_gira"])
entorno.renderizar()
"""