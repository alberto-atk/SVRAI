from random import choices

class Estado:
    def __init__(self,id):
        self.id = id   
    
    def __str__(self) -> str:
        return self.id

class Entorno1:
    movimientos = {}
    estado_actual = Estado("estado_indeterminado")
    recompensa = 0

    def __init__(self,id,estados, acciones):
        self.id = id
        self.estados = estados
        self.acciones = acciones
        self.estado_actual = estados[choices(list(estados), k=1)[0]]
        self.nestados = len(estados)
        self.nacciones = len(acciones)

    def reset(self):
        acciones = {"no_gira":0,"gira":1} #no gira y gira
        estados = {"bajo":0, "medio": 1,"alto": 2 }
        self.__init__("ejercicio1",estados,acciones)
        return self.estado_actual
    
    def definir_movimientos(self,estado1,accion,estado2):
        self.movimientos[(estado1,accion)] = estado2

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
        
    def nuevo_estado(self,estado,accion):
        nuevo_estado = self.movimientos[(estado,accion)]
        if nuevo_estado == 0:
            self.recompensa -= 1
            return 1, nuevo_estado, -1
        else:
            self.recompensa += 2
            return 1, nuevo_estado, 2
    
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