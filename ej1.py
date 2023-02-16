from random import choices

class Estado:
    def __init__(self,id):
        self.id = id   
    
    def __str__(self) -> str:
        return self.id

class Entorno:
    movimientos = {}
    estado_actual = Estado("estado_indeterminado")
    recompensa = 0

    def __init__(self,id,estados:dict, acciones:dict):
        self.id = id
        self.estados = estados
        self.acciones = acciones
        self.estado_actual = estados[choices(list(estados), k=1)[0]]
        print(type(self.estado_actual))

    
    def definir_movimientos(self,estado1:Estado,accion,estado2:Estado):
        self.movimientos[(estado1,accion)] = estado2

    def realizar_accion(self,accion):
        self.estado_actual = self.movimientos[(self.estado_actual,accion)]




acciones = {"no_gira":0,"gira":1} #no gira y gira
estados = {"alto": Estado("alto"), "medio": Estado("medio"), "bajo":Estado("bajo")}

entorno = Entorno("ejercicio1",estados, acciones)

entorno.definir_movimientos(estados["alto"],acciones["gira"],estados["alto"])
entorno.definir_movimientos(estados["alto"],acciones["no_gira"],estados["medio"])

entorno.definir_movimientos(estados["medio"],acciones["gira"],estados["alto"])
entorno.definir_movimientos(estados["medio"],acciones["no_gira"],estados["bajo"])

entorno.definir_movimientos(estados["bajo"],acciones["gira"],estados["medio"])
entorno.definir_movimientos(estados["bajo"],acciones["no_gira"],estados["bajo"])


print(entorno.estado_actual)
entorno.realizar_accion(acciones["no_gira"])
print(entorno.estado_actual)
